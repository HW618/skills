---
name: ucloud-product-learning
description: Generate Chinese Markdown learning manuals for UCloud products from official UCloud and Alibaba Cloud documentation. Use when the user wants to learn a UCloud product, create a UCloud product study guide, prepare UCloud presales product materials, or compare a UCloud product with a confirmed Alibaba Cloud competitor.
---

# UCloud Product Learning

## Workflow

Use this skill to create a UCloud product learning manual for presales study. The output must be grounded in official documentation and written in Chinese.

Before generating the manual, confirm the Alibaba Cloud competitor product name.

1. Parse the user request and identify:
   - UCloud product name, abbreviation, or product family.
   - Alibaba Cloud competitor product name, if the user supplied one.
2. If the user supplied the competitor name, treat it as confirmed and continue.
3. If the user did not supply the competitor name:
   - Search or infer one Alibaba Cloud competitor from the UCloud product name and official product category.
   - Ask the user to confirm that single Alibaba Cloud product name.
   - Do not generate the full manual until the user confirms.
4. After confirmation, research both products from official documentation:
   - UCloud docs: `https://docs.ucloud.cn/`
   - Alibaba Cloud docs: `https://help.aliyun.com/`
5. Read [references/research-rules.md](references/research-rules.md) before researching and filtering sources.
6. Read [references/manual-template.md](references/manual-template.md) before drafting the final Markdown manual.

## Source Rules

- For UCloud products, first open the product README index page when the product path is known, using `https://docs.ucloud.cn/{product-path}/README`, for example `https://docs.ucloud.cn/ufs/README`.
- Use the README page as the product documentation table of contents. Follow its page links to product overview, features, specifications, limits, performance, FAQ, and scenarios.
- Prefer official product overview, introduction, architecture, feature, advantage, specification, performance, limit, usage note, FAQ, and application scenario pages.
- For UCloud sources, cite page-level official documentation URLs under `https://docs.ucloud.cn/`, for example `https://docs.ucloud.cn/ufs/ufs_manual_instruction/limit`.
- Do not use UCloud `mdToPdf` PDF links as the normal citation source when an equivalent HTML documentation page exists.
- Ignore configuration guides, operation guides, quick starts, step-by-step tutorials, and test procedures unless they contain product specifications, limits, performance data, or important usage notes.
- Preserve official links for key facts, specifications, restrictions, performance claims, and comparison points.
- If official documentation does not clearly state a fact, write `官方文档中未找到明确说明`.

## Competitor Confirmation

If the user gives both products, continue directly:

```text
学习 UHost，对标阿里云 ECS
```

If the user gives only the UCloud product, pause after proposing one Alibaba Cloud competitor:

```text
我建议将 UCloud UFile 对标阿里云 OSS。请确认是否使用阿里云 OSS 作为竞品产品；确认后我再生成学习手册。
```

Only compare against the confirmed Alibaba Cloud product. Do not build a multi-competitor matrix unless the user explicitly asks.

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
- Separate official facts from presales analysis in comparison sections:
  - Use `官方文档事实` for statements directly supported by documentation.
  - Use `售前分析` for reasoned interpretation based on documented facts.
- Include official source links in the relevant bullets or tables, not only at the end.
