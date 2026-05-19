# Codex Skills

This repository stores reusable Codex skills for local workflows and domain-specific assistant behavior.

## Skills

| Skill | Purpose | Key files |
| --- | --- | --- |
| `rclone-cloud-storage` | Use `rclone` for cloud storage workflows such as remote configuration, uploads, directory listing, and small text previews. | `skills/rclone-cloud-storage/SKILL.md`, `skills/rclone-cloud-storage/references/rclone-official-notes.md` |
| `ucloud-product-learning` | Generate and reuse Chinese UCloud product learning manuals for presales study, including confirmed Alibaba Cloud competitor mapping, verified official-document citations, scenarios, selection advice, and follow-up Q&A from saved manuals. | `skills/ucloud-product-learning/SKILL.md`, `skills/ucloud-product-learning/references/manual-template.md`, `skills/ucloud-product-learning/references/research-rules.md`, `skills/ucloud-product-learning/references/ucloud-aliyun-product-map.md` |

## Repository Layout

```text
skills/
├── rclone-cloud-storage/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/rclone-official-notes.md
└── ucloud-product-learning/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
        ├── manual-template.md
        ├── research-rules.md
        └── ucloud-aliyun-product-map.md
```

## UCloud Product Learning

The `ucloud-product-learning` skill is designed for becoming a stronger UCloud presales specialist.

It supports two request types:

- **Generate a product manual**: Given a UCloud product, confirm the Alibaba Cloud competitor first, then generate a Chinese Markdown learning manual from official UCloud and Alibaba Cloud documentation.
- **Answer follow-up questions**: For questions about product features, specifications, pricing, scenarios, selection advice, or Alibaba Cloud comparison, first read the saved manual in `references/ucloud-{product_name}.md`.

Important behavior:

- Checks `references/ucloud-aliyun-product-map.md` before live searching for Alibaba Cloud competitor suggestions.
- Uses UCloud product README pages such as `https://docs.ucloud.cn/ufs/README` as documentation indexes.
- Requires cited links to be verified and working; guessed or 404 links are not allowed.
- Saves generated manuals as `skills/ucloud-product-learning/references/ucloud-{product_name}.md`.
- Prompts the user to generate a manual first when a follow-up question references a product without a saved manual.

## Rclone Cloud Storage

The `rclone-cloud-storage` skill provides a cautious workflow for cloud storage tasks:

- Install or verify `rclone`
- Configure remotes interactively
- Store Codex-specific upload defaults outside this repository
- Upload files or folders
- List remote directories
- Preview small remote text files

The skill intentionally avoids destructive operations unless the user explicitly requests them.

## Safety

Do not commit credentials, local configuration, generated secrets, or machine-specific files.

Never commit:

- `~/.config/rclone/rclone.conf`
- `~/.config/rclone/codex-defaults.json`
- WebDAV usernames, passwords, app passwords, tokens, or API keys
- Cloud access keys or temporary credentials

Generated UCloud product manuals may be committed when they are intended to become reusable reference material.

## Maintenance

When updating or adding skills:

- Keep `SKILL.md` concise and procedural.
- Put reusable templates, rules, and mappings in `references/`.
- Keep UI metadata in `agents/openai.yaml`.
- Prefer official documentation links and verify links before using them as citations.
- Avoid adding auxiliary docs unless they directly support skill execution.
