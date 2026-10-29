# 产品索引模板

Use this template when creating `index-{product_name}.md`. The index is a verified URL map used before generating a product learning manual.

## Metadata

| Field | Value |
| --- | --- |
| UCloud product |  |
| UCloud navigation URL |  |
| Alibaba Cloud product |  |
| Alibaba Cloud navigation URL |  |
| Last verified |  |

## UCloud

| 模块 | URL | 验证状态 | 备注 |
| --- | --- | --- | --- |
|  |  | verified |  |

## 阿里云

| 模块 | URL | 验证状态 | 备注 |
| --- | --- | --- | --- |
|  |  | verified |  |

## Rules

- Only record URLs that have been opened or otherwise confirmed accessible.
- Do not record guessed URLs.
- Apply the same completeness standard to both UCloud and Alibaba Cloud navigation pages.
- Record parent modules, child modules, repeated modules, learning-path modules, billing modules, specification modules, feature modules, limit modules, architecture modules, selection-guidance modules, scenario-overview modules, developer-reference overview modules, and official external entry links when they appear in the navigation.
- For Alibaba Cloud, do not index FAQ modules, practice/tutorial modules, experience-lab modules, quick-start walkthroughs, or pure console/SDK/CLI/Terraform operation steps.
- If a module is visible in the navigation but the URL cannot be verified, keep the module name and set `验证状态` to `未记录：URL未验证`; do not use that row as a citation source.
- Use this file as the first source map when generating a manual.
- Refresh invalid or stale URLs before drafting.
