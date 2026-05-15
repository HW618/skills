# UCloud 产品学习资料检索规则

## Research Order

1. Confirm the Alibaba Cloud competitor product before drafting the manual.
2. Resolve the UCloud product documentation path.
   - If the product abbreviation maps directly to a docs path, use that path, for example UFS -> `ufs`.
   - Open the product README index page: `https://docs.ucloud.cn/{product-path}/README`.
   - Example: `https://docs.ucloud.cn/ufs/README`.
   - Treat the README page as the product documentation table of contents and extract the relevant page URLs from it.
3. Search UCloud official docs for the confirmed UCloud product by following README links first:
   - Product overview or introduction.
   - Feature and advantage pages.
   - Specification, performance, quota, limit, or restriction pages.
   - Application scenario, solution, FAQ, and usage note pages.
   - Page-level HTML URLs under the product path, such as `https://docs.ucloud.cn/ufs/ufs_manual_instruction/limit`.
4. If the README page is unavailable or does not contain the needed section, then use targeted web search scoped to `docs.ucloud.cn/{product-path}`.
5. Search Alibaba Cloud official docs for the confirmed competitor product:
   - Product overview or introduction.
   - Feature and advantage pages.
   - Specification, performance, limit, or scenario pages.
6. **Fast-track concept pages:** When searching Alibaba Cloud docs, priority access pages whose URLs contain `what-is` or `product-overview` path segments for concept extraction:
   - Example matching URLs: `https://help.aliyun.com/document-detail/what-is-ecs.html`, `https://help.aliyun.com/ecs/product-overview`
   - Extract pre-requisite concepts from these pages first before expanding to feature/specification pages.
7. Prefer current HTML documentation pages. For UCloud, do not cite `mdToPdf` PDF URLs when a matching HTML documentation page exists. Use official PDFs only as a last resort when HTML pages do not expose the needed product information, and state that the PDF was used because no page-level URL was found.

## Include

- Product positioning and definitions.
- Core concepts and architecture-level descriptions.
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
- For Alibaba Cloud citations, use the specific page URL whose path contains `what-is` or `product-overview` for concept definitions, and feature/specification page URLs for functional details.
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

For each scenario, synthesize UCloud and Alibaba Cloud documentation into presales language:

- Describe the scenario characteristics.
- Identify customer needs.
- Identify likely customer pain points.
- Name the selection concerns: performance, availability, scalability, compatibility, security, cost, operations, or compliance.
- Explain how the UCloud product fits the scenario.
- Mention product limits that may affect fit.
