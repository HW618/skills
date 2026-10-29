#!/usr/bin/env python3
"""Regression checks for the offline-downloader Bugbot findings."""

import os
import stat
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import aria2_env  # noqa: E402
import init  # noqa: E402


class Aria2EnvTests(unittest.TestCase):
    def test_pip_install_uses_current_interpreter(self):
        cmd = aria2_env.pip_install_argv()
        self.assertEqual(cmd[:4], [sys.executable, "-m", "pip", "install"])
        self.assertNotIn("--force-reinstall", cmd)
        forced = aria2_env.pip_install_argv(force=True)
        self.assertEqual(forced[0], sys.executable)
        self.assertIn("--force-reinstall", forced)

    def test_open_rpc_without_our_process_is_refused(self):
        self.assertEqual(
            aria2_env.classify_daemon(False, True, True),
            "refuse",
        )
        self.assertEqual(aria2_env.classify_daemon(True, True, True), "use")
        self.assertEqual(aria2_env.classify_daemon(True, True, False), "wait")
        self.assertEqual(aria2_env.classify_daemon(False, False, False), "start")

    def test_start_daemon_does_not_adopt_foreign_listener(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = {
                "skill_dir": aria2_env.skill_dir,
                "process": aria2_env._process_lines,
                "ready": aria2_env.rpc_ready,
                "open": aria2_env.rpc_endpoint_open,
                "run": aria2_env.subprocess.run,
            }
            launched = []

            def refuse_launch(argv, **kwargs):
                launched.append(argv)
                raise AssertionError("refused listener must not be replaced by a new aria2c")

            aria2_env.skill_dir = lambda: tmp
            aria2_env._process_lines = lambda: [
                "aria2c --enable-rpc --rpc-listen-all=true --daemon=true"
            ]
            aria2_env.rpc_ready = lambda secret, port=6800: True
            aria2_env.rpc_endpoint_open = lambda port=6800: True
            aria2_env.subprocess.run = refuse_launch
            try:
                ok, message = aria2_env.start_daemon()
            finally:
                aria2_env.skill_dir = original["skill_dir"]
                aria2_env._process_lines = original["process"]
                aria2_env.rpc_ready = original["ready"]
                aria2_env.rpc_endpoint_open = original["open"]
                aria2_env.subprocess.run = original["run"]
            self.assertFalse(ok)
            self.assertIn("不能当作本技能的守护进程", message)
            self.assertEqual(launched, [])

    def test_conf_path_download_does_not_block_our_daemon(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = {
                "skill_dir": aria2_env.skill_dir,
                "process": aria2_env._process_lines,
                "ready": aria2_env.rpc_ready,
                "open": aria2_env.rpc_endpoint_open,
                "run": aria2_env.subprocess.run,
            }
            launched = []

            class _Result:
                returncode = 1
                stderr = "stopped in test"
                stdout = ""

            def record_launch(argv, **kwargs):
                launched.append(list(argv))
                return _Result()

            aria2_env.skill_dir = lambda: tmp
            aria2_env._process_lines = lambda: [
                "aria2c --conf-path=/tmp/downloads.conf --dir=/tmp/out"
            ]
            aria2_env.rpc_ready = lambda secret, port=6800: False
            aria2_env.rpc_endpoint_open = lambda port=6800: False
            aria2_env.subprocess.run = record_launch
            try:
                self.assertFalse(
                    aria2_env.foreign_rpc_daemon("/tmp/skill/.aria2-rpc.conf")
                )
                ok, message = aria2_env.start_daemon()
            finally:
                aria2_env.skill_dir = original["skill_dir"]
                aria2_env._process_lines = original["process"]
                aria2_env.rpc_ready = original["ready"]
                aria2_env.rpc_endpoint_open = original["open"]
                aria2_env.subprocess.run = original["run"]
            self.assertFalse(ok)
            self.assertNotIn("不能当作本技能的守护进程", message)
            self.assertEqual(len(launched), 1)
            self.assertEqual(launched[0][0], "aria2c")

    def test_explicit_rpc_flags_still_count_as_foreign(self):
        original = aria2_env._process_lines
        aria2_env._process_lines = lambda: [
            "aria2c --enable-rpc --rpc-listen-all=false --daemon=true"
        ]
        try:
            self.assertTrue(aria2_env.foreign_rpc_daemon("/tmp/skill/.aria2-rpc.conf"))
        finally:
            aria2_env._process_lines = original

    def test_daemon_command_is_loopback_config_not_open_rpc(self):
        argv = aria2_env.daemon_argv("/tmp/skill/.aria2-rpc.conf")
        joined = " ".join(argv)
        self.assertIn("--conf-path=/tmp/skill/.aria2-rpc.conf", joined)
        self.assertNotIn("rpc-listen-all=true", joined)
        self.assertNotIn("--rpc-secret", joined)

    def test_rpc_conf_stays_on_loopback_and_private(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = aria2_env.skill_dir
            aria2_env.skill_dir = lambda: tmp
            try:
                path, secret = aria2_env.ensure_rpc_conf()
                text = Path(path).read_text(encoding="utf-8")
                self.assertIn("rpc-listen-all=false", text)
                self.assertNotIn("rpc-listen-all=true", text)
                self.assertIn(f"rpc-secret={secret}", text)
                self.assertNotIn("/Users/houston", text)
                mode = stat.S_IMODE(os.stat(path).st_mode)
                self.assertEqual(mode, 0o600)
                again, same_secret = aria2_env.ensure_rpc_conf()
                self.assertEqual(again, path)
                self.assertEqual(same_secret, secret)

                Path(path).write_text(
                    "enable-rpc=true\nrpc-listen-all=true\nrpc-secret=kept-secret\n",
                    encoding="utf-8",
                )
                os.chmod(path, 0o644)
                _, repaired = aria2_env.ensure_rpc_conf()
                repaired_text = Path(path).read_text(encoding="utf-8")
                self.assertEqual(repaired, "kept-secret")
                self.assertIn("rpc-listen-all=false", repaired_text)
                self.assertNotIn("rpc-listen-all=true", repaired_text)
                self.assertEqual(stat.S_IMODE(os.stat(path).st_mode), 0o600)
            finally:
                aria2_env.skill_dir = original


class InitFlowTests(unittest.TestCase):
    def setUp(self):
        self._argv = sys.argv[:]
        self._checks = (
            init.check_aria2c,
            init.check_aria2p,
            init.create_download_dir,
            init.start_aria2c_daemon,
            init.install_aria2,
            init.install_aria2p,
            init.check_and_install_all,
        )

    def tearDown(self):
        sys.argv = self._argv
        (
            init.check_aria2c,
            init.check_aria2p,
            init.create_download_dir,
            init.start_aria2c_daemon,
            init.install_aria2,
            init.install_aria2p,
            init.check_and_install_all,
        ) = self._checks

    def test_daemon_start_failure_fails_init(self):
        init.check_aria2c = lambda: (True, "/usr/bin/aria2c", "aria2 version")
        init.check_aria2p = lambda: (True, "0.12.0")
        init.create_download_dir = lambda: True
        init.start_aria2c_daemon = lambda: False
        self.assertFalse(init.check_and_install_all())

    def test_force_is_honored_and_failure_exits_nonzero(self):
        seen = {}

        def fake(force=False):
            seen["force"] = force
            return False

        init.check_and_install_all = fake
        sys.argv = ["init.py", "--force"]
        with self.assertRaises(SystemExit) as raised:
            init.main()
        self.assertEqual(raised.exception.code, 1)
        self.assertTrue(seen["force"])

    def test_success_exits_zero(self):
        init.check_and_install_all = lambda force=False: True
        sys.argv = ["init.py"]
        with self.assertRaises(SystemExit) as raised:
            init.main()
        self.assertEqual(raised.exception.code, 0)


class DocPathTests(unittest.TestCase):
    def test_skill_docs_and_scripts_have_no_personal_or_open_rpc_path(self):
        docs = [
            ROOT / "SKILL.md",
            ROOT / "references" / "usage.md",
        ]
        scripts = [
            ROOT / "scripts" / "download.py",
            ROOT / "scripts" / "init.py",
            ROOT / "scripts" / "cleanup.py",
            ROOT / "scripts" / "aria2_env.py",
        ]
        for path in docs + scripts:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("/Users/houston", text, path.name)
        for path in scripts:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("rpc-listen-all=true", text, path.name)


if __name__ == "__main__":
    unittest.main()
