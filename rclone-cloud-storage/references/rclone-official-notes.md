# Rclone Official Notes

These notes summarize the rclone official documentation for this skill. Use the official docs for provider-specific setup details and current command behavior.

## Sources

- Install: https://rclone.org/install/
- General usage and configuration: https://rclone.org/docs/
- `rclone config`: https://rclone.org/commands/rclone_config/
- `rclone config file`: https://rclone.org/commands/rclone_config_file/
- `rclone config create`: https://rclone.org/commands/rclone_config_create/
- `rclone listremotes`: https://rclone.org/commands/rclone_listremotes/
- `rclone copy`: https://rclone.org/commands/rclone_copy/
- `rclone copyto`: https://rclone.org/commands/rclone_copyto/
- `rclone mkdir`: https://rclone.org/commands/rclone_mkdir/
- `rclone lsjson`: https://rclone.org/commands/rclone_lsjson/
- `rclone lsf`: https://rclone.org/commands/rclone_lsf/
- `rclone cat`: https://rclone.org/commands/rclone_cat/

## Installation

rclone is distributed as a single Go binary. The official quickstart is: download the binary, extract the `rclone` executable, then run `rclone config`.

Common official installation paths:

- macOS Homebrew: `brew install rclone`
- macOS MacPorts: `sudo port install rclone`
- Linux official script: `sudo -v ; curl https://rclone.org/install.sh | sudo bash`
- Windows: precompiled archive, Winget, Chocolatey, or Scoop.
- Docker, Snap, source, Ansible, and portable installs are also documented.

Always verify with `rclone version`.

## Configuration

Initial setup is normally interactive:

```bash
rclone config
```

The config session creates and manages remotes. Remote auth varies by backend, so guide the user through provider prompts instead of inventing credentials.

Useful config commands:

```bash
rclone config file
rclone listremotes
rclone listremotes --json
rclone config create name type key value
```

`rclone config create` can be useful for scripted setup, but if the backend needs additional questions, rclone may take defaults or return a non-interactive continuation flow. Prefer `rclone config` for normal user-guided setup.

Default config file lookup order includes the executable directory, `%APPDATA%/rclone/rclone.conf` on Windows, `$XDG_CONFIG_HOME/rclone/rclone.conf`, `~/.config/rclone/rclone.conf`, and `~/.rclone.conf`. Use `rclone config file` to show the active path.

## Path Syntax

rclone commands use:

```text
rclone subcommand [options] <parameters>
remote:path/to/item
/local/path/to/item
```

The remote name is the name chosen in the config file, followed by `:` and an optional path, for example `drive:Reports`.

## Copying and Uploading

Use `copy` for normal uploads. It skips identical files and does not delete destination files.

```bash
rclone copy "/local/path/file.pdf" "remote:path" -P
rclone copy "/local/path/folder" "remote:path/folder" -P
```

Important behavior: when copying a directory, rclone copies the directory contents into the destination path. To preserve the folder name, include that folder name in the destination.

Use `copyto` when the destination file name must be explicit:

```bash
rclone copyto "/local/path/file.pdf" "remote:path/new-name.pdf" -P
```

Useful flags:

- `-P` or `--progress`: show transfer progress.
- `--dry-run`: test without permanent changes.
- `--interactive` or `-i`: confirm actions interactively.
- `--metadata`: preserve metadata where supported.

Use `mkdir` to create a remote path:

```bash
rclone mkdir "remote:path"
```

## Listing

Prefer `lsjson` for machine-readable results:

```bash
rclone lsjson "remote:path"
rclone lsjson "remote:path" --recursive
```

`lsjson` returns items with fields such as `Name`, `Path`, `Size`, `ModTime`, `MimeType`, `IsDir`, and hashes when requested.

Use `lsf` for lightweight parseable listings:

```bash
rclone lsf "remote:path"
rclone lsf "remote:path" --format "pst"
```

`lsf` does not recurse by default; pass `--recursive` or `-R` when needed. `ls` and `lsl` recurse by default; use `--max-depth 1` to limit them.

## Reading Remote File Contents

Use `cat` only for file-content previews or explicit file-content requests:

```bash
rclone cat "remote:path/file.txt" --head 4000
rclone cat "remote:path/file.txt" --tail 4000
```

Bound output with `--head`, `--tail`, `--offset`, or `--count` unless the user explicitly requests the whole file.
