# Custom Codex Skills

Private repository for reusable Codex skills.

## Contents

- `skills/rclone-cloud-storage`: install, configure, upload, list, and preview cloud files with rclone.

## Safety

Do not commit local cloud credentials or machine-specific configuration, including:

- `~/.config/rclone/rclone.conf`
- `~/.config/rclone/codex-defaults.json`
- WebDAV usernames, passwords, app passwords, tokens, or API keys

The included rclone skill contains workflow instructions only. It does not include configured remotes or credentials.
