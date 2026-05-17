# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目定位

高玮课程 LLM Wiki。原始资料位于 `D:\Space\notes\HomeSpace\Finance\Gao\Business Logic\LectureText`，本仓库只存放编译后的知识页面和来源索引，不存放大文件。

## 五层架构

| 层 | 目录 | 职责 |
|---|---|---|
| 来源层 | `sources/` | 来源卡片：路径、讲次、格式、状态，不承担解释 |
| 课程层 | `courses/` | 按讲次组织：摘要、知识点、问答、复习材料 |
| 知识层 | `wiki/` | 跨课程沉淀：概念、框架、案例、行业、组织问题 |
| 应用层 | `applications/` | 分析工具箱、AI 上下文索引、个人工具 |
| 维护层 | `schema/` | 页面规范、命名约定、lint 规则 |

辅助目录：`scripts/`（可重复脚本）、`maps/`（课程/概念地图）、`log.md`（变更日志）。

详见 [建设计划](docs/plans/2026-05-14-gao-course-llm-wiki-build-plan.md) 和 [背景上下文](docs/context/2026-05-14-background.md)。

## 项目约定

- 项目名：`gao-course-wiki`，不再更改。
- 大文件（视频、PDF、音频）长期存放于 HomeSpace，wiki 只记录路径引用。
- 展示软件：Obsidian，vault 已指向本目录，插件已配置。

## 来源类型

所有来源必须在 `source_card` 的 `source_type` 字段中标注类型：

| source_type | 说明 |
|---|---|
| `course-transcript` | 课程文字稿 |
| `course-slide` | 课件或 PDF |
| `course-video` | 视频 |
| `personal-note` | 个人观点、笔记、感悟 |
| `external-reference` | 外部资料、书籍、文章 |
| `agent-synthesis` | Agent 综合产物（必须追溯来源） |

wiki 页面正文中引用个人观点时用 **[个人]** 标注，引用外部资料时用 **[外部]** 标注，便于与课程来源区分。

## 页面 YAML frontmatter 规范

稳定页面必须包含：

```yaml
---
id: concept-first-principles
type: concept          # source-card | lecture-note | concept | framework | case
status: draft          # draft | reviewed
source_scope:
  - course: business-logic
    lecture_id: "042"
review:
  human_checked: false
  last_reviewed: null
---
```

未经人工确认的页面使用 `status: draft`。

## 写作规则

- 调研结论区分**事实**、**推断**、**待验证**三类。
- Agent 生成的综合结论必须追溯到来源讲次或人工确认记录。
- 有来源冲突时记录冲突，不直接覆盖原始来源。
- `courses/business-logic/lectures/` 的讲次编号必须与 `HomeSpace\Finance\Gao\Business Logic\LectureText` 中原始文字稿编号严格对应。
- 每次重要摄入或结构调整更新 `log.md`。
- 文档不能出现 emoji，代码注释使用中文。

## 脚本

- `scripts/inventory_sources.py` — 扫描原始资料目录，生成来源卡片草稿
- `scripts/lint_wiki.py` — 验证页面 frontmatter schema 合规性

运行环境：Python 3.10+，使用 `uv`。

## 提炼工作流

详细执行规范见 `docs/workflows/lecture-extraction-workflow.md`。该文档是单篇和批量提炼的准入流程，agent 执行提炼任务时必须优先遵守。

### 触发口令

- 单篇：`提炼讲次 042`
- 批量：`批量提炼 001 020 034 042 044`

### 每篇提炼的最小闭环

1. 检查 git 状态，避免混入无关改动。
2. 读取来源卡片，取得并核验 `source_path`。
3. 读取原始 txt 全文，核对讲次编号、文件名标题和正文开场主题；如有错位必须记录。
4. 填充或更新讲次页面（`courses/business-logic/lectures/`）所有提炼段落。
5. 更新来源卡片：`status` 改为 `summarized`，填充事实摘录、推断和待验证项。
6. 填充或更新对应 wiki 页面（`wiki/frameworks/`、`wiki/concepts/` 等），并保留来源证据。
7. 必要时更新课程索引、wiki 索引和 AI 上下文入口。
8. 运行 `python scripts/lint_wiki.py`，确认通过。
9. 在 `log.md` 追加提炼记录。
10. 只暂存本讲相关文件并提交 git。

### 内容写作要求

- 讲次页面：保留课程原始逻辑顺序，用自己的语言提炼，不逐字复制。
- wiki 页面：只写跨讲次稳定结论；单讲专有内容留在讲次页，不搬到 wiki。
- 事实 / 推断 / 待验证三类结论必须明确标注。
- 文件名、正文主题、来源卡片标题不一致时，不能删除错位说明，必须保留处理依据。

## 最小闭环（第一版目标）

1. 登记来源卡片
2. 处理 5-10 篇商业逻辑讲次
3. 生成讲次摘要
4. 抽取概念/框架/案例写入 `wiki/`
5. 建立 `applications/ai-context/` 入口
6. 运行 lint
7. 更新 `log.md`
