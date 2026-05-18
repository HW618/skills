# UCloud 产品学习手册模板

Use this structure for the final Chinese Markdown manual after the Alibaba Cloud competitor product has been confirmed.

```markdown
# {UCloud产品名} 产品学习手册

## 1. 产品概述

- 产品定位：
- 解决的问题：
- 核心用户/业务类型：
- 关键概念：

## 2. 前置概念

Only generate this chapter when Alibaba Cloud documentation contains a matching pre-requisite concept section. If no matching section exists, omit this chapter entirely and renumber the later chapters.

| 概念 | 概念说明 |
| --- | --- |
|  | [说明文本](阿里云文档链接) |

## 3. 产品功能

| 功能 | 说明 | 售前关注点 | 来源 |
| --- | --- | --- | --- |
|  |  |  |  |

## 4. 产品特点

- 特点一：
- 特点二：
- 特点三：

## 5. 产品优势

- 优势一：
- 优势二：
- 优势三：

## 6. 产品性能

| 性能维度 | UCloud 文档信息 | 售前解读 | 来源 |
| --- | --- | --- | --- |
| 计算/存储/网络/吞吐/延迟等 |  |  |  |

## 7. 产品规格

| 规格维度 | UCloud 文档信息 | 选型意义 | 来源 |
| --- | --- | --- | --- |
|  |  |  |  |

## 8. 计费方式

| 计费模式 | 说明 | 适用场景 | 来源 |
| --- | --- | --- | --- |
|  |  |  |  |

## 9. 使用限制与使用说明

| 限制/说明 | 影响 | 售前提醒 | 来源 |
| --- | --- | --- | --- |
|  |  |  |  |

## 10. 应用场景

### 10.1 UCloud 文档中的应用场景

#### 场景一：{UCloud场景名称}

- 场景特点：
- 客户需求：
- 客户痛点：
- 选型关注点：
- UCloud 产品适配点：
- 选型建议：
- 来源：

### 10.2 阿里云文档中的应用场景

#### 场景一：{阿里云场景名称}

- 场景特点：
- 客户需求：
- 客户痛点：
- 选型关注点：
- 对 UCloud 售前定位的启发：
- 选型建议：
- 来源：

## 11. 与阿里云 {阿里云竞品名} 的对比

| 对比维度 | UCloud {产品名} | 阿里云 {竞品名} | 售前分析 | 来源 |
| --- | --- | --- | --- | --- |
| 产品定位 |  |  |  |  |
| 核心功能 |  |  |  |  |
| 性能/规格 |  |  |  |  |
| 使用限制 |  |  |  |  |
| 应用场景 |  |  |  |  |

## 12. UCloud 实操实验建议

这些是学习验证建议，不写具体操作步骤。

| 实验方向 | 学习目标 | 建议观察点 |
| --- | --- | --- |
|  |  |  |

## 13. 术语与英文缩写

| 缩写/术语 | 英文全称 | 中文说明 |
| --- | --- | --- |
|  |  |  |

## 14. 参考资料

- UCloud：
- 阿里云：
```

## Drafting Notes

- Keep each section concise but complete enough for presales study.
- Put source links close to the claim they support.
- Only include verified working URLs. Do not generate, guess, or cite links that return 404 or cannot be opened. If no valid official URL is found, write `官方文档中未找到有效来源链接`.
- Chapter 2 `前置概念` should prioritize Alibaba Cloud candidate pages whose URLs contain `what-is` or `product-overview`, then extract only from a `<section>` whose title is `前置概念` and whose content contains `阅读本文前，您可能需要了解如下概念：`. From that `<section>`, extract its `<li>` items. For each `<li>`, put the concept name in the `概念` column and put the linked description text in the `概念说明` column as a Markdown link using the `<a href>` URL from Alibaba Cloud, for example `[什么是云计算？](https://www.aliyun.com/getting-started/what-is/what-is-cloud-computing)`. Do not include a `来源` column for this chapter. If no matching section is found, omit chapter 2 entirely and renumber subsequent chapters.
- For UCloud sources, cite page-level official docs URLs whenever possible, such as `https://docs.ucloud.cn/ufs/ufs_manual_instruction/limit`; avoid `mdToPdf` PDF links unless no equivalent HTML page exists.
- In chapter 10, include both UCloud and Alibaba Cloud application scenarios as separate subsections and add selection advice for each scenario.
- Do not include long operational procedures.
- If a section has no official information, keep the section and write `官方文档中未找到明确说明`.
- Save the final manual in the skill's `references/` directory with the exact filename pattern `ucloud-{product_name}.md`, for example `ucloud-ufs.md`, and provide a clickable local file link to the user.
