# UCloud 产品学习资料检索规则

## Research Order

1. Confirm the Alibaba Cloud competitor product before drafting the manual.
2. Before searching for an Alibaba Cloud competitor, check [ucloud-aliyun-product-map.md](ucloud-aliyun-product-map.md):
   - Match by UCloud product name, alias, or docs path.
   - Use the mapped Alibaba Cloud product as the first recommendation.
   - Use the mapped UCloud navigation page URL and Alibaba Cloud navigation page URL as the starting pages.
   - If the user rejects the mapping, perform fresh official-doc search and propose one revised competitor.
3. Read or build `references/index-{product_name}.md`:
   - If the index exists, use it as the first source URL map.
   - If the index is missing, open the UCloud and Alibaba Cloud navigation page URLs from the product mapping table.
   - Traverse the navigation pages and extract module or section names with their hyperlinks.
   - Save the verified URLs into `index-{product_name}.md`, split into `## UCloud` and `## 阿里云` sections.
   - For UHost, the UCloud navigation page should be `https://docs.ucloud.cn/uhost/README`; the Alibaba Cloud ECS navigation page should be a verified `https://help.aliyun.com/zh/ecs/` product page URL.
4. Use only verified URLs from `index-{product_name}.md` for detailed research:
   - Product overview or introduction.
   - Feature and advantage pages.
   - Specification, performance, quota, limit, or restriction pages.
   - Application scenario, solution, and usage note pages.
   - Billing pages.
   - For Alibaba Cloud, skip FAQ pages and practice-operation tutorials even if they appear in the navigation.
5. If the index file is stale, missing a needed section, or contains invalid URLs, refresh the index from the navigation pages before drafting.
6. For chapter 2 pre-requisite concepts, use Alibaba Cloud indexed pages whose URLs contain `what-is` or `product-overview` as the priority search candidates:
   - These URL patterns are search-entry conditions, not extraction conditions.
   - Example matching paths: `.../what-is-...`, `.../product-overview/...`.
7. Extract chapter 2 pre-requisite concepts from the prioritized Alibaba Cloud candidate pages only when the source page contains a `<section>` element that matches both conditions:
   - The section title is `前置概念`.
   - The section content contains `阅读本文前，您可能需要了解如下概念：`.
   - Use only the `<li>` items listed in that `<section>` for chapter 2. Do not synthesize chapter 2 concepts from unrelated Alibaba Cloud overview text.
   - For each `<li>`, extract linked `<a href>` items and preserve the Alibaba Cloud link in the chapter 2 table's `概念说明` column.
   - If no matching `<section>` exists, omit chapter 2 entirely and renumber later chapters.
8. Prefer current HTML documentation pages. For UCloud, do not cite `mdToPdf` PDF URLs when a matching HTML documentation page exists. Use official PDFs only as a last resort when HTML pages do not expose the needed product information, and state that the PDF was used because no page-level URL was found.

## Product Mapping Table Rules

- Product mapping rows must include:
  - UCloud product name and aliases.
  - UCloud navigation page URL, usually `https://docs.ucloud.cn/{product-path}/README`.
  - Alibaba Cloud competitor product name.
  - Alibaba Cloud navigation page URL, for example `https://help.aliyun.com/zh/ecs/`.
  - Validation status or notes.
- Navigation page URLs are starting points for building product indexes; they are not enough for final manual citations when a more specific indexed URL exists.
- Verify navigation URLs before using them. If a navigation URL is invalid, refresh the mapping row before continuing.

## Product Index File Rules

- Name each product index file `index-{product_name}.md`, for example `index-uhost.md`.
- Split each index file into two sections: `## UCloud` and `## 阿里云`.
- Traverse both navigation pages and record every module that has a discoverable and verified URL, not only product-introduction modules.
- Record parent modules, child modules, and repeated modules when they appear in the navigation. If several child modules are sections of the same page, reuse the verified parent page URL and note the relationship in `备注`.
- For UCloud UHost, include every module from the product navigation that has a verified URL, including product introduction, host, feature, disk, image, network, monitoring, purchase guidance, quick start, operation guide, metadata, key pair, isolation group, performance data, and pricing modules.
- For Alibaba Cloud products, apply the same completeness rule as UCloud:
  - Record all parent modules, child modules, repeated modules, learning-path modules, billing modules, specification modules, feature modules, limit modules, architecture modules, selection-guidance modules, scenario-overview modules, developer-reference overview modules, and external official ecosystem links that appear in the product navigation page.
  - For Alibaba Cloud ECS, include modules from the ECS navigation page that help product learning and presales analysis, including product introduction, billing, instance specification, creation and purchase overview, login concept overview, instance management overview, block storage, image and snapshot, network and security group, developer documentation overview, and price or purchase entry links.
  - Do not index Alibaba Cloud FAQ modules, practice/tutorial modules, experience-lab modules, quick-start walkthroughs, or pure console/SDK/CLI/Terraform operation steps.
  - Links that redirect to login pages, external console pages, or non-document official pages may be recorded for completeness, but mark their purpose in `备注` and do not use them as product-learning citation sources unless the content itself is accessible and relevant.
- Every recorded URL must be verified as accessible before it is written into the index file.
- Do not write guessed URLs into an index file. If a module name is visible but the URL cannot be verified, omit it or mark it as `未记录：URL未验证`.

## Manual Storage And Reuse

- Save generated manuals in this skill's `references/` directory.
- Use the filename pattern `ucloud-{product_name}.md`, for example `ucloud-ufs.md`, `ucloud-uhost.md`, or `ucloud-ulb.md`.
- Normalize `{product_name}` to lowercase ASCII when possible. Keep common product abbreviations as lowercase, for example `UFS` -> `ufs`.
- When answering user follow-up questions about product features, specifications, pricing, application scenarios, selection advice, or Alibaba Cloud comparison, read the matching manual first.
- If the matching manual does not exist, prompt the user to generate it before answering.

## Include

- Product positioning and definitions.
- Core concepts and architecture-level descriptions.
- Alibaba Cloud `前置概念` sections only when the `<section>` title and marker sentence match the chapter 2 rule.
- Functional capabilities.
- Product advantages and differentiators stated by the vendor.
- Customer usage contexts implied by UCloud product advantages, especially scenarios tied to customer needs, pain points, or selection concerns.
- Performance parameters, instance families, capacity limits, quotas, and specifications.
- Usage restrictions, compatibility notes, region/zone constraints, billing-relevant constraints, and operational caveats that affect presales advice.
- Application scenarios and solution descriptions.

## Exclude

- Console operation steps.
- SDK/API operation procedures.
- Quick start walkthroughs.
- Installation or configuration commands.
- Step-by-step testing procedures.
- Troubleshooting flows, unless they reveal product limits or usage constraints.

## Citation Rules

- Validate every URL before citing it in the final manual:
  - Open the URL or otherwise confirm it resolves to an accessible official documentation page.
  - Do not cite URLs that return 404, redirect to unrelated content, require unavailable access, or were guessed from a URL pattern but not opened.
  - Do not fabricate page paths. URL patterns such as UCloud README paths and Alibaba Cloud `what-is`/`product-overview` paths are search hints, not citations until verified.
  - If a mapped product URL in [ucloud-aliyun-product-map.md](ucloud-aliyun-product-map.md) is invalid, search the official documentation site for a valid current URL before citing.
  - If a URL in `index-{product_name}.md` is invalid, refresh that index before using it.
  - If no valid official URL can be found for a claim, write `官方文档中未找到有效来源链接` or omit the claim.
- Cite official source links for:
  - Product definitions.
  - Key features.
  - Advantages.
  - Performance and specification values.
  - Limits and restrictions.
  - Comparison claims.
- For UCloud citations, use the most specific page-level `docs.ucloud.cn` URL available:
  - Use the product README URL only for table-of-contents or product-documentation-entry claims.
  - Use the linked section page URL for actual facts.
  - Good index: `https://docs.ucloud.cn/ufs/README`
  - Good: `https://docs.ucloud.cn/ufs/ufs_manual_instruction/limit`
  - Avoid: `https://docs.ucloud.cn/ufs/mdToPdf/ufs.pdf`
- For Alibaba Cloud concept definitions, prefer specific page URLs whose paths contain `what-is` or `product-overview`; for chapter 2, still require the matched `前置概念` `<section>` and marker sentence before extracting concepts.
- For chapter 2 `前置概念`, extract concept links from the matched `<section>`'s `<li>` items. The chapter 2 table must have only `概念` and `概念说明` columns; put the `<a href>` URL in the `概念说明` Markdown link. If no matching section is found, omit chapter 2 entirely.
- If a UCloud PDF contains the needed fact, search for the corresponding HTML page before citing it.
- If no equivalent UCloud HTML page can be found, cite the PDF only as a fallback and add `未找到对应官网页面级链接`.
- Do not cite search result snippets as final evidence when the source page can be opened.
- If only a source page summary is available, say so plainly and avoid over-specific claims.

## Comparison Rules

- Compare only the confirmed Alibaba Cloud product.
- Separate direct documentation facts from presales interpretation.
- Do not claim that one product is better unless official evidence or clear scenario logic supports the conclusion.
- Phrase uncertain findings as:
  - `官方文档中未找到明确说明`
  - `基于已检索文档，暂未发现...`
  - `售前分析：在该场景下更应关注...`

## Scenario Analysis Rules

When explaining UCloud product advantages outside the application scenarios chapter, add a brief likely-usage-scenario note for each advantage:

- Identify what kind of customer or workload would benefit from the advantage.
- Tie the advantage to a concrete business or technical need.
- Keep the note short; the full scenario expansion belongs in chapter 10.

For the application scenarios chapter, use both vendors' documentation and split the content into two subsections:

- `### 10.1 UCloud 文档中的应用场景`
- `### 10.2 阿里云文档中的应用场景`

For each vendor scenario, synthesize the official documentation into presales language:

- Describe the scenario characteristics.
- Identify customer needs.
- Identify likely customer pain points.
- Name the selection concerns: performance, availability, scalability, compatibility, security, cost, operations, or compliance.
- Explain how the UCloud product fits the scenario.
- For Alibaba Cloud scenarios, explain what the scenario reveals about the general product category and how it should inform UCloud positioning.
- Add product selection advice for each scenario, including when to recommend the UCloud product, when to be cautious, and what technical or commercial details to confirm before committing.
- Mention product limits that may affect fit.
