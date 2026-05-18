# UCloud 产品学习资料检索规则

## Research Order

1. Confirm the Alibaba Cloud competitor product before drafting the manual.
2. Before searching for an Alibaba Cloud competitor, check [ucloud-aliyun-product-map.md](ucloud-aliyun-product-map.md):
   - Match by UCloud product name, alias, or docs path.
   - Use the mapped Alibaba Cloud product as the first recommendation.
   - If the user rejects the mapping, perform fresh official-doc search and propose one revised competitor.
3. Resolve the UCloud product documentation path.
   - If the product abbreviation maps directly to a docs path, use that path, for example UFS -> `ufs`.
   - Open the product README index page: `https://docs.ucloud.cn/{product-path}/README`.
   - Example: `https://docs.ucloud.cn/ufs/README`.
   - Treat the README page as the product documentation table of contents and extract the relevant page URLs from it.
4. Search UCloud official docs for the confirmed UCloud product by following README links first:
   - Product overview or introduction.
   - Feature and advantage pages.
   - Specification, performance, quota, limit, or restriction pages.
   - Application scenario, solution, FAQ, and usage note pages.
   - Page-level HTML URLs under the product path, such as `https://docs.ucloud.cn/ufs/ufs_manual_instruction/limit`.
5. If the README page is unavailable or does not contain the needed section, then use targeted web search scoped to `docs.ucloud.cn/{product-path}`.
6. Search Alibaba Cloud official docs for the confirmed competitor product:
   - Product overview or introduction.
   - Feature and advantage pages.
   - Specification, performance, limit, or scenario pages.
7. For chapter 2 pre-requisite concepts, use Alibaba Cloud pages whose URLs contain `what-is` or `product-overview` as the priority search candidates:
   - These URL patterns are search-entry conditions, not extraction conditions.
   - Example matching paths: `.../what-is-...`, `.../product-overview/...`.
8. Extract chapter 2 pre-requisite concepts from the prioritized Alibaba Cloud candidate pages only when the source page contains a `<section>` element that matches both conditions:
   - The section title is `前置概念`.
   - The section content contains `阅读本文前，您可能需要了解如下概念：`.
   - Use only the `<li>` items listed in that `<section>` for chapter 2. Do not synthesize chapter 2 concepts from unrelated Alibaba Cloud overview text.
   - For each `<li>`, extract linked `<a href>` items and preserve the Alibaba Cloud link in the chapter 2 table's `概念说明` column.
   - If no matching `<section>` exists, omit chapter 2 entirely and renumber later chapters.
9. Prefer current HTML documentation pages. For UCloud, do not cite `mdToPdf` PDF URLs when a matching HTML documentation page exists. Use official PDFs only as a last resort when HTML pages do not expose the needed product information, and state that the PDF was used because no page-level URL was found.

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
