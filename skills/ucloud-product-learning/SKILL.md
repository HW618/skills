---
name: ucloud-product-learning
description: Generate and reuse Chinese Markdown learning manuals for UCloud products from official UCloud and Alibaba Cloud documentation. Use when the user wants to learn a UCloud product, create a UCloud product study guide, prepare UCloud presales product materials, compare a UCloud product with a confirmed Alibaba Cloud competitor, or ask follow-up questions about UCloud product features, specifications, pricing, scenarios, or Alibaba Cloud comparisons.
---

# UCloud Product Learning

## Workflow

Use this skill to create a UCloud product learning manual for presales study. The output must be grounded in official documentation and written in Chinese.

## Request Types

- **Generate manual**: The user asks to learn a UCloud product or create a product learning manual.
- **Answer from manual**: The user asks follow-up questions about a UCloud product's features, specifications, pricing, application scenarios, selection advice, or comparison with Alibaba Cloud.

For answer-from-manual requests, read the matching product manual in `references/ucloud-{product_name}.md` first. If the manual does not exist, tell the user that the product manual needs to be generated before answering from this skill.

## Generate Manual Workflow

Before generating the manual, confirm the Alibaba Cloud competitor product name.

1. Parse the user request and identify:
   - UCloud product name, abbreviation, or product family.
   - Alibaba Cloud competitor product name, if the user supplied one.
2. If the user supplied the competitor name, treat it as confirmed and continue.
3. If the user did not supply the competitor name:
   - Read [references/ucloud-aliyun-product-map.md](references/ucloud-aliyun-product-map.md) first.
   - Search the mapping file for the UCloud product name, alias, or docs path.
   - If a mapping exists, recommend the mapped Alibaba Cloud product and ask the user to confirm.
   - If the user rejects the mapping or no mapping exists, then search official UCloud and Alibaba Cloud docs and recommend one alternative Alibaba Cloud product.
   - Do not generate the full manual until the user confirms.
4. After confirmation, research both products from official documentation:
   - UCloud docs: `https://docs.ucloud.cn/`
   - Alibaba Cloud docs: `https://help.aliyun.com/`
5. Read [references/research-rules.md](references/research-rules.md) before researching and filtering sources.
6. Read [references/manual-template.md](references/manual-template.md) before drafting the final Markdown manual.
7. Save every completed learning manual under this skill's `references/` directory as `ucloud-{product_name}.md`, where `{product_name}` is the normalized lowercase UCloud product name, for example `ucloud-ufs.md`.
8. Send the user a clickable local file link to the generated manual.

## Answer From Manual Workflow

Use this workflow when the user asks about an already learned/generated UCloud product:

1. Identify the UCloud product name in the question.
2. Look for `references/ucloud-{product_name}.md`.
3. If the manual exists:
   - Answer primarily from that manual.
   - Cite the relevant manual sections or source links already preserved in the manual.
   - If the user asks for a comparison, use the manual's Alibaba Cloud comparison and application scenario sections first.
4. If the manual does not exist:
   - Do not answer from memory or start broad live research.
   - Tell the user: `当前 reference 目录中还没有该产品的学习手册，需要先生成 ucloud-{product_name}.md 后再进行问答。`

## Source Rules

- For UCloud products, first open the product README index page when the product path is known, using `https://docs.ucloud.cn/{product-path}/README`, for example `https://docs.ucloud.cn/ufs/README`.
- Use the README page as the product documentation table of contents. Follow its page links to product overview, features, specifications, limits, performance, FAQ, and scenarios.
- Prefer official product overview, introduction, architecture, feature, advantage, specification, performance, limit, usage note, FAQ, and application scenario pages.
- For UCloud sources, cite page-level official documentation URLs under `https://docs.ucloud.cn/`, for example `https://docs.ucloud.cn/ufs/ufs_manual_instruction/limit`.
- Do not use UCloud `mdToPdf` PDF links as the normal citation source when an equivalent HTML documentation page exists.
- Ignore configuration guides, operation guides, quick starts, step-by-step tutorials, and test procedures unless they contain product specifications, limits, performance data, or important usage notes.
- Preserve official links for key facts, specifications, restrictions, performance claims, and comparison points.
- Verify every cited URL before including it in the manual. Do not invent URLs, guess URL paths, or cite links that return 404, redirect to an unrelated page, require unavailable access, or cannot be opened.
- If a likely source URL is invalid, search for a valid official replacement. If no valid official URL is found, keep the claim only when it is clearly supported by another verified source, or write `官方文档中未找到有效来源链接`.
- If official documentation does not clearly state a fact, write `官方文档中未找到明确说明`.

## Competitor Confirmation

If the user gives both products, continue directly:

```text
学习 UHost，对标阿里云 ECS
```

If the user gives only the UCloud product, pause after proposing one Alibaba Cloud competitor:

```text
我在映射表中查到 UCloud UFile 建议对标阿里云 OSS。请确认是否使用阿里云 OSS 作为竞品产品；确认后我再生成学习手册。
```

Only compare against the confirmed Alibaba Cloud product. Do not build a multi-competitor matrix unless the user explicitly asks.

If the user says the mapped competitor is not correct, do not argue from the mapping file. Search official docs again, propose one revised Alibaba Cloud competitor, and ask for confirmation.

## Output Rules

- Write the manual in Chinese Markdown.
- Keep English product names and technical terms when useful.
- Expand English abbreviations on first use, for example `ECS（Elastic Compute Service）`.
- Make the application scenarios presales-oriented:
  - Scenario characteristics.
  - Customer needs.
  - Customer pain points.
  - Selection concerns.
  - UCloud product fit.
  - Alibaba Cloud scenario reference.
  - Product selection recommendation.
- Separate official facts from presales analysis in comparison sections:
  - Use `官方文档事实` for statements directly supported by documentation.
  - Use `售前分析` for reasoned interpretation based on documented facts.
- Include official source links in the relevant bullets or tables, not only at the end.
- Include only verified, working links. Invalid or guessed links are forbidden.
- After drafting, create a Markdown file in `references/` named with the exact pattern `ucloud-{product_name}.md`.
- Send the user the generated file link in the final response.
