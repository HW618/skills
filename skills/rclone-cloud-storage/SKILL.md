---
name: rclone-cloud-storage
description: Install and use rclone for cloud storage workflows. Use when the user asks Codex to install rclone, configure rclone remotes, set or inspect a default cloud drive and default upload directory, upload local files or folders to a cloud drive with rclone, list files in a default or specified remote directory, or preview small remote text file contents through rclone.
---

# Rclone Cloud Storage

## Workflow

Use rclone as the implementation tool for cloud-drive operations. Prefer official rclone commands over provider-specific CLIs.

Read [references/rclone-official-notes.md](references/rclone-official-notes.md) when you need command details, install variants, or official documentation links.

## Safety Rules

- Treat cloud storage as user data. Do not delete, purge, sync, move, or overwrite intentionally unless the user explicitly asks.
- For first-time transfers, use `--dry-run` or `--interactive` when the requested action is broad, ambiguous, or may affect many files.
- Do not print secrets, OAuth tokens, or full decrypted rclone config content. Avoid `rclone config show` unless a narrow diagnostic requires it, and redact sensitive values.
- Ask before installing dependencies or running commands that require network or elevated permissions.
- Quote local paths and rclone paths in shell commands.

## Install

1. Check whether rclone is already available:

```bash
command -v rclone
rclone version
```

2. If missing, choose the platform-appropriate official path:

- macOS with Homebrew: `brew install rclone`
- macOS with MacPorts: `sudo port install rclone`
- Linux official script: `sudo -v ; curl https://rclone.org/install.sh | sudo bash`
- Windows: use the official installer/archive, Winget, Chocolatey, or Scoop as appropriate.

3. Verify after installation:

```bash
rclone version
```

## Configure

Use rclone's interactive configuration unless the user requests a scripted setup and has supplied all required backend details.

```bash
rclone config
```

Guide the user to:

1. Create a new remote.
2. Choose the storage provider.
3. Complete provider-specific OAuth or credentials prompts.
4. Name the remote clearly, for example `drive`, `onedrive`, `s3-work`, or `dropbox`.
5. Confirm available remotes:

```bash
rclone listremotes
rclone listremotes --json
```

Show the config file path, if useful, with:

```bash
rclone config file
```

## Defaults

Because rclone itself does not define a "default upload directory" for Codex workflows, store Codex-specific defaults in:

```text
~/.config/rclone/codex-defaults.json
```

Use this shape:

```json
{
  "default_remote": "drive",
  "default_upload_dir": "CodexUploads"
}
```

Interpret the default destination as:

```text
<default_remote>:<default_upload_dir>
```

When setting defaults:

- Ensure the selected remote exists with `rclone listremotes`.
- Normalize a trailing colon away in `default_remote`; store `drive`, not `drive:`.
- Store remote paths without a leading slash unless the backend documentation requires it.
- Create the remote directory when the user wants it prepared:

```bash
rclone mkdir "drive:CodexUploads"
```

When showing defaults, read `codex-defaults.json` and report the resolved destination, for example `drive:CodexUploads`. If the defaults file is missing or incomplete, ask the user which remote and upload directory to use, then save it.

## Upload

Resolve the destination:

- If the user specifies a remote path like `onedrive:Reports/2026`, use it.
- If the user specifies only a remote name like `onedrive`, combine it with the default upload directory.
- If the user does not specify a destination, use `<default_remote>:<default_upload_dir>`.

Check that every local source exists before uploading.

Upload files or folder contents:

```bash
rclone copy "/local/path/file.pdf" "drive:CodexUploads" -P
rclone copy "/local/path/folder" "drive:CodexUploads/folder" -P
```

Use `copyto` only when the destination file name must be explicit:

```bash
rclone copyto "/local/path/file.pdf" "drive:CodexUploads/custom-name.pdf" -P
```

After upload, verify with `lsjson` or `lsf` and summarize the uploaded destination to the user.

## List Remote Files

Resolve the target directory the same way as uploads. Prefer JSON for robust parsing:

```bash
rclone lsjson "drive:CodexUploads"
rclone lsjson "drive:CodexUploads" --recursive
```

Return a concise table with name, type, size, modification time, and path. Use `lsf` when a lighter parseable listing is enough:

```bash
rclone lsf "drive:CodexUploads" --format "pst"
```

If the user asks to view the contents of a specific small text file, use `rclone cat` with a bounded read:

```bash
rclone cat "drive:CodexUploads/notes.txt" --head 4000
```

Do not stream large remote files into chat unless the user explicitly requests it.
