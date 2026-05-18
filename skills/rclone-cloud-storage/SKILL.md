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
- Do not print secrets, OAuth tokens, environment variable values, or full decrypted rclone config content. Avoid `rclone config show` unless a narrow diagnostic requires it, and redact sensitive values.
- Ask before installing dependencies or running commands that require network or elevated permissions.
- Quote local paths and rclone paths in shell commands.
- Never enable shell tracing (`set -x`) when reading or using `RSKILL_` environment variables.

## Preflight Before Any User Operation

Before upload, list, preview, default inspection, or configuration work, check the skill reference default file:

```text
skills/rclone-cloud-storage/references/rclone-defaults.json
```

Use this shape:

```json
{
  "default_remote": "teracloud",
  "default_upload_dir": "CodexUploads"
}
```

Preflight flow:

1. Read `references/rclone-defaults.json` if it exists.
2. If `default_remote` exists, confirm that it is still configured:

```bash
rclone listremotes
```

3. Normalize remote names without trailing colons in the JSON file. Interpret `teracloud` as `teracloud:`.
4. Validate the default remote before using it with a low-impact list command:

```bash
rclone lsf "teracloud:" --max-depth 1
```

5. If the defaults file is missing or has no valid `default_remote`, run:

```bash
rclone listremotes
```

Then select the first configured remote as `default_remote`, write it to `references/rclone-defaults.json`, and use `CodexUploads` as `default_upload_dir` unless the user specifies another directory.

6. If the default remote is configured but invalid, unavailable, or fails validation:
   - Do not silently switch remotes.
   - Show the available remote names only, without secrets.
   - Ask whether to use the next configured remote or create a new remote configuration.
   - If the user chooses the next remote, validate it before saving it as the new default.

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

When the user runs first-time setup or asks for `rclone config`, first check whether `RSKILL_` environment variables provide a complete WebDAV or S3 configuration. If they do, create or update the remote from environment variables without printing their values. If they do not, use rclone's interactive configuration unless the user requests a scripted setup and has supplied all required backend details.

Supported environment variables:

Common:

- `RSKILL_REMOTE_NAME`: remote name to create or update.
- `RSKILL_REMOTE_TYPE`: `webdav` or `s3`.
- `RSKILL_DEFAULT_UPLOAD_DIR`: optional default upload directory.

WebDAV:

- `RSKILL_WEBDAV_URL`
- `RSKILL_WEBDAV_VENDOR`: optional rclone vendor value, for example `other`, `nextcloud`, or `owncloud`.
- `RSKILL_WEBDAV_USER`
- `RSKILL_WEBDAV_PASS`

S3:

- `RSKILL_S3_PROVIDER`: optional provider, for example `AWS`, `Minio`, or `Other`.
- `RSKILL_S3_ACCESS_KEY_ID`
- `RSKILL_S3_SECRET_ACCESS_KEY`
- `RSKILL_S3_ENDPOINT`: optional custom endpoint.
- `RSKILL_S3_REGION`: optional region.

Environment setup rules:

- Treat all `RSKILL_` values as secrets or sensitive configuration.
- Do not echo, print, log, or summarize the values.
- It is acceptable to report which variable names are present or missing.
- Use shell variable references, not literal values, when showing example commands to the user.
- After creating the remote, validate it with a low-impact list command and save `references/rclone-defaults.json` with the remote name and default upload directory.

Example command shapes, with values referenced from the environment:

```bash
rclone config create "$RSKILL_REMOTE_NAME" webdav \
  url "$RSKILL_WEBDAV_URL" \
  vendor "${RSKILL_WEBDAV_VENDOR:-other}" \
  user "$RSKILL_WEBDAV_USER" \
  pass "$RSKILL_WEBDAV_PASS"
```

```bash
rclone config create "$RSKILL_REMOTE_NAME" s3 \
  provider "${RSKILL_S3_PROVIDER:-Other}" \
  access_key_id "$RSKILL_S3_ACCESS_KEY_ID" \
  secret_access_key "$RSKILL_S3_SECRET_ACCESS_KEY" \
  endpoint "$RSKILL_S3_ENDPOINT" \
  region "$RSKILL_S3_REGION"
```

If rclone requires an obscured password for a backend field, use official rclone behavior or commands without printing the raw value.

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

Because rclone itself does not define a "default upload directory" for Codex workflows, store Codex-specific defaults in this skill reference file:

```text
skills/rclone-cloud-storage/references/rclone-defaults.json
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
- Validate the selected remote with `rclone lsf "<remote>:" --max-depth 1` before saving when possible.
- Normalize a trailing colon away in `default_remote`; store `drive`, not `drive:`.
- Store remote paths without a leading slash unless the backend documentation requires it.
- Create the remote directory when the user wants it prepared:

```bash
rclone mkdir "drive:CodexUploads"
```

When showing defaults, read `references/rclone-defaults.json` and report the resolved destination, for example `drive:CodexUploads`. If the defaults file is missing or incomplete, use the preflight flow to select the first configured valid remote and save it.

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
