# 高玮课程 LLM Wiki Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 建设一个以高玮课程为来源、以个人长期知识体系为目标的 LLM Wiki，使课程资料能够被持续摄入、编译、追溯、复习、分析和供 Agent 使用。

**Architecture:** 采用“来源层、课程层、知识层、应用层、维护层”五层结构。原始资料不直接等同于 wiki 页面，Agent 先登记来源，再按课程讲次提炼，最后沉淀为跨课程概念、框架、案例和应用入口。

**Tech Stack:** Markdown、Git、Obsidian 兼容双链、YAML frontmatter、PowerShell、Python 3.10+、uv、可选的后续静态站点工具或 RAG 索引。

---

## 1. 背景和目标

### 1.1 事实

- 目标项目目录是 `D:\Project\Lecture\gao-course-wiki`。
- 第一批资料位于 `D:\Space\notes\HomeSpace\Finance\Gao\Business Logic\LectureText`。
- `Gao` 指高玮，是课程主讲老师。
- 当前资料主要是商业逻辑课文字稿，未来可能加入 AI、产品、操盘手等课程。
- 当前资料目录中已经存在 `Readme.md`，记录资料来源、下载过程、文件结构和缺失编号。
- 未来资料可能扩展为视频、PDF、课件、截图、音频和补充资料。
- 用户目标同时包括学习内化、商业分析工具箱、AI 可读知识底座、个人第二大脑。

### 1.2 推断

- 不应使用多个 git 分支分别承载四类目标；这些目标应是同一个知识底座上的多个视图。
- 项目应以“高玮课程体系”为一级边界，而不是以“商业逻辑课”为一级边界。
- `D:\Project\Lecture\gao-course-wiki` 适合作为正式工程化 wiki；HomeSpace 更适合作为个人入口和原始资料存放地。
- 第一版应先跑通一个最小闭环，再逐步扩展到完整自动化。

### 1.3 待确认问题

- 是否将 Obsidian 作为第一展示软件。
- 是否将大视频和 PDF 保留在 HomeSpace，wiki 中只记录引用。
- 是否需要为课程内容、个人观点、外部资料分别建立来源类型。
- 第一批摄入是处理全部商业逻辑文字稿，还是先选样本验证流程。

## 2. 目标目录结构

第一版建议创建以下结构：

```text
gao-course-wiki/
├── AGENTS.md
├── README.md
├── sources/
│   ├── index.md
│   ├── raw-paths.md
│   └── cards/
├── courses/
│   ├── index.md
│   └── business-logic/
│       ├── index.md
│       ├── lectures/
│       ├── summaries/
│       └── questions/
├── wiki/
│   ├── index.md
│   ├── concepts/
│   ├── frameworks/
│   ├── cases/
│   ├── industries/
│   └── people-org/
├── applications/
│   ├── index.md
│   ├── analysis-toolkit/
│   ├── personal-use/
│   └── ai-context/
├── schema/
│   ├── source-card.md
│   ├── lecture-note.md
│   ├── wiki-page.md
│   └── lint.md
├── scripts/
│   ├── inventory_sources.py
│   └── lint_wiki.py
├── maps/
│   └── index.md
└── log.md
```

### 2.1 层级职责

- `sources/`：记录来源，不承担解释任务。每个来源卡片描述原始文件、课程、讲次、格式、路径、状态和可信度。
- `courses/`：保留课程原有顺序和学习路径。这里适合放讲次摘要、知识点、问题、复习材料。
- `wiki/`：沉淀跨课程稳定知识。这里不按讲次组织，而按概念、方法、案例、行业和组织问题组织。
- `applications/`：面向实际使用。这里可以形成商业分析工具箱、个人成长工具箱、AI 上下文索引和 Prompt。
- `schema/`：约束 Agent 怎么写、怎么命名、怎么判断内容是否合格。
- `scripts/`：放可重复运行的检查、索引和摄入辅助脚本。
- `maps/`：放课程地图、概念地图和关系图。
- `log.md`：记录每次重要摄入、结构调整、人工确认和待复核问题。

## 3. 关键设计原则

### 3.1 原始资料和 wiki 分离

原始资料可以保留在 HomeSpace 或后续独立材料目录。wiki 项目只登记来源信息和稳定知识页面，不默认复制大视频和 PDF。

原因：

- 避免 git 仓库被大文件拖慢。
- 方便未来迁移 wiki 项目。
- 保留资料权限和来源边界。
- 允许同一来源被多个页面引用。

### 3.2 课程视角和知识视角分离

课程视角回答“第几讲讲了什么”。知识视角回答“这个概念、框架、案例在整个体系中意味着什么”。

例子：

- `courses/business-logic/lectures/042-first-principles-1.md` 记录第 42 讲。
- `wiki/frameworks/first-principles.md` 沉淀第一性原理作为方法论。
- `applications/analysis-toolkit/first-principles-analysis.md` 将方法论变成可复用分析模板。

### 3.3 人读和 Agent 读同时保留

人读页面要有叙述性、解释性和复习价值。Agent 读索引要有稳定 ID、标签、来源路径和结构化字段。

建议每个稳定页面包含：

```markdown
---
id: concept-first-principles
type: concept
status: draft
source_scope:
  - course: business-logic
    lecture_id: "042"
review:
  human_checked: false
  last_reviewed: null
---
```

### 3.4 先最小闭环，再扩展

第一版只需要跑通：

1. 登记来源。
2. 处理 5 到 10 篇讲次。
3. 生成讲次摘要。
4. 抽取概念、框架、案例。
5. 写入跨课程 wiki 页面。
6. 建立应用入口。
7. 运行一次 lint。
8. 记录日志。

不需要第一版就完成所有课程、所有自动化和所有展示软件集成。

## 4. 实施任务

### Task 1: 初始化项目说明和 Agent 规则

**Files:**

- Create: `AGENTS.md`
- Modify: `README.md`
- Modify: `log.md`

- [ ] **Step 1: 创建项目级 `AGENTS.md`**

写入以下内容：

```markdown
# Codex 项目配置

## 语言规则

- 回答始终使用简体中文。
- 项目文档不能出现 emoji。
- 代码注释始终使用中文。

## 项目目标

本项目用于建设高玮课程 LLM Wiki。它不是原始资料备份目录，而是一个将课程资料持续编译为个人知识体系的 Markdown 知识库。

## 内容分层

- `sources/`：来源索引和来源卡片。
- `courses/`：按课程和讲次组织的学习层。
- `wiki/`：跨课程概念、框架、案例、行业和组织问题。
- `applications/`：商业分析、个人使用和 AI 上下文入口。
- `schema/`：摄入、页面和维护规则。
- `scripts/`：可重复运行的索引和检查脚本。
- `maps/`：课程地图、概念地图和关系图。

## 写作规则

- 调研结论必须区分事实、推断和待验证问题。
- 涉及来源时保留本地路径、课程、讲次和文件名。
- 不直接覆盖原始来源观点；有冲突时记录冲突和来源差异。
- Agent 生成的综合结论必须能追溯到来源。
- 每次重要摄入或结构调整都更新 `log.md`。

## 资料治理

- 大视频、PDF、音频默认不进入 git。
- 原始资料优先通过来源卡片登记。
- 未经人工确认的页面使用 `status: draft`。
```

- [ ] **Step 2: 更新 `README.md`**

保留已有项目定位，并补充“第一阶段目标”：

```markdown
## 第一阶段目标

第一阶段不追求完整整理全部课程，而是跑通一个最小可维护闭环：

1. 建立来源卡片 schema。
2. 对商业逻辑课文字稿做来源盘点。
3. 选取 5 到 10 篇讲次生成课程层页面。
4. 从样本中抽取概念、框架和案例。
5. 形成第一批跨课程 wiki 页面。
6. 建立 AI 上下文索引和维护 lint 规则。
```

- [ ] **Step 3: 创建或更新 `log.md`**

写入：

```markdown
# 调研与建设日志

## 2026-05-14 | init-plan | 初始化建设计划

- 确定项目定位：高玮课程 LLM Wiki。
- 确定第一批资料来源：`D:\Space\notes\HomeSpace\Finance\Gao\Business Logic\LectureText`。
- 暂定正式工程目录：`D:\Project\Lecture\gao-course-wiki`。
- 暂定五层结构：来源层、课程层、知识层、应用层、维护层。
- 决定不使用 git 分支承载不同使用目标，而用目录和视图区分学习内化、商业分析工具箱、AI 知识底座和个人第二大脑。

待确认：

- 展示软件是否首选 Obsidian。
- 大文件是否长期留在 HomeSpace。
- 第一批摄入样本范围。
```

- [ ] **Step 4: 验证**

运行：

```powershell
Get-ChildItem -Force
Get-Content -Encoding UTF8 -Raw .\AGENTS.md
Get-Content -Encoding UTF8 -Raw .\README.md
Get-Content -Encoding UTF8 -Raw .\log.md
```

Expected: 三个文件均存在，内容为简体中文，不含 emoji。

- [ ] **Step 5: Commit**

```powershell
git add AGENTS.md README.md log.md
git commit -m "docs: initialize Gao course wiki project guidance"
```

### Task 2: 创建来源层 schema

**Files:**

- Create: `schema/source-card.md`
- Create: `schema/lecture-note.md`
- Create: `schema/wiki-page.md`
- Create: `schema/lint.md`

- [ ] **Step 1: 创建 `schema/source-card.md`**

```markdown
# 来源卡片 Schema

每个来源卡片记录一个原始资料或一组强绑定资料。来源卡片不负责总结全部知识，只负责说明资料是什么、在哪里、属于哪门课、处理到什么状态。

## Frontmatter

```yaml
---
id: source-business-logic-001
type: source-card
course: business-logic
lecture_id: "001"
teacher: 高玮
title: 从DAO看组织的底层逻辑与核心要素
source_format: transcript
source_path: "D:\\Space\\notes\\HomeSpace\\Finance\\Gao\\Business Logic\\LectureText\\001、从DAO看组织的底层逻辑与核心要素.txt"
status: inventoried
rights: private-reference
created: 2026-05-14
updated: 2026-05-14
---
```

## 正文结构

```markdown
## 来源说明

## 文件信息

## 已处理产物

## 事实摘录

## 推断和待验证

## 关联页面
```
```

- [ ] **Step 2: 创建 `schema/lecture-note.md`**

```markdown
# 讲次页面 Schema

讲次页面用于保留课程原始顺序和学习路径。它可以引用来源卡片，但不直接复制全文。

## Frontmatter

```yaml
---
id: lecture-business-logic-001
type: lecture-note
course: business-logic
lecture_id: "001"
teacher: 高玮
title: 从DAO看组织的底层逻辑与核心要素
source_cards:
  - source-business-logic-001
status: draft
created: 2026-05-14
updated: 2026-05-14
---
```

## 正文结构

```markdown
## 本讲定位

## 核心问题

## 主要观点

## 概念和框架

## 案例

## 可复用启发

## 待验证问题

## 关联
```
```

- [ ] **Step 3: 创建 `schema/wiki-page.md`**

```markdown
# Wiki 页面 Schema

Wiki 页面用于沉淀跨讲次、跨课程的稳定知识。

## Frontmatter

```yaml
---
id: framework-first-principles
type: framework
title: 第一性原理
status: draft
source_scope:
  - course: business-logic
    lecture_id: "042"
human_checked: false
created: 2026-05-14
updated: 2026-05-14
---
```

## 正文结构

```markdown
## 定义

## 解决什么问题

## 使用条件

## 操作步骤

## 典型案例

## 易错点

## 与其他概念的关系

## 来源和证据

## 待验证问题
```
```

- [ ] **Step 4: 创建 `schema/lint.md`**

```markdown
# 维护检查规则

## 必须检查

- 每个来源卡片必须有 `source_path`。
- 每个讲次页面必须有至少一个 `source_cards`。
- 每个 wiki 页面必须有 `source_scope` 或说明其来源缺口。
- `status: stable` 的页面必须 `human_checked: true`。
- 页面中不能出现 emoji。
- 页面不能只有总结，没有来源。
- 跨课程概念页必须链接至少一个讲次页或来源卡片。

## 建议检查

- 是否存在孤立页面。
- 是否存在多个页面表达同一概念但命名不一致。
- 是否存在过长页面需要拆分。
- 是否存在观点冲突但没有冲突记录。
```

- [ ] **Step 5: 验证**

运行：

```powershell
Get-ChildItem -Force .\schema
Select-String -Path .\schema\*.md -Pattern "TODO|TBD|emoji"
```

Expected: 四个 schema 文件存在；`TODO`、`TBD` 不应出现；`emoji` 只允许出现在规则描述中。

- [ ] **Step 6: Commit**

```powershell
git add schema
git commit -m "docs: add schemas for Gao course wiki"
```

### Task 3: 建立来源盘点脚本

**Files:**

- Create: `scripts/inventory_sources.py`
- Create: `sources/raw-paths.md`
- Create: `sources/index.md`

- [ ] **Step 1: 创建 `scripts/inventory_sources.py`**

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


RAW_ROOT = Path(r"D:\Space\notes\HomeSpace\Finance\Gao\Business Logic\LectureText")


@dataclass(frozen=True)
class SourceFile:
    course: str
    lecture_id: str
    title: str
    path: Path
    size: int


def parse_file(path: Path) -> SourceFile | None:
    if path.suffix.lower() != ".txt":
        return None
    match = re.match(r"^(\d{3})、(.+)\.txt$", path.name)
    if not match:
        return None
    lecture_id, title = match.groups()
    return SourceFile(
        course="business-logic",
        lecture_id=lecture_id,
        title=title,
        path=path,
        size=path.stat().st_size,
    )


def collect_sources(root: Path) -> list[SourceFile]:
    sources: list[SourceFile] = []
    for path in sorted(root.glob("*.txt")):
        source = parse_file(path)
        if source is not None:
            sources.append(source)
    return sources


def render_index(sources: list[SourceFile]) -> str:
    lines = [
        "# 来源索引",
        "",
        "## Business Logic",
        "",
        "| 讲次 | 标题 | 字节数 | 路径 |",
        "|---|---|---:|---|",
    ]
    for source in sources:
        lines.append(
            f"| {source.lecture_id} | {source.title} | {source.size} | `{source.path}` |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    sources = collect_sources(RAW_ROOT)
    output = Path("sources/raw-paths.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_index(sources), encoding="utf-8")
    print(f"indexed={len(sources)} output={output}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 创建 `sources/index.md`**

```markdown
# 来源层

来源层记录原始资料的位置、格式、状态和派生产物。

## 当前来源

- [原始路径盘点](raw-paths.md)
- `cards/`：来源卡片目录，后续按课程和讲次创建。

## 处理状态

- `inventoried`：已登记路径和基础信息。
- `summarized`：已生成讲次摘要。
- `linked`：已关联到 wiki 页面。
- `reviewed`：已人工复核。
```

- [ ] **Step 3: 运行脚本生成 `sources/raw-paths.md`**

```powershell
uv run python .\scripts\inventory_sources.py
```

Expected: 输出类似 `indexed=158 output=sources\raw-paths.md`。实际数量以当前目录为准。

- [ ] **Step 4: 验证索引**

```powershell
Get-Content -Encoding UTF8 -TotalCount 20 .\sources\raw-paths.md
```

Expected: 文件包含表头 `讲次 | 标题 | 字节数 | 路径`，路径指向 HomeSpace 原始资料。

- [ ] **Step 5: Commit**

```powershell
git add scripts/inventory_sources.py sources/index.md sources/raw-paths.md
git commit -m "feat: inventory Gao business logic transcripts"
```

### Task 4: 建立第一批课程层页面

**Files:**

- Create: `courses/index.md`
- Create: `courses/business-logic/index.md`
- Create: `courses/business-logic/lectures/001-dao-organization-logic.md`
- Create: `courses/business-logic/lectures/020-review-method.md`
- Create: `courses/business-logic/lectures/034-strategy-design.md`
- Create: `courses/business-logic/lectures/042-first-principles-1.md`
- Create: `courses/business-logic/lectures/044-business-full-chain-thinking.md`

- [ ] **Step 1: 创建课程入口 `courses/index.md`**

```markdown
# 课程层

课程层按高玮老师的课程体系组织内容，保留课程原有顺序和学习路径。

## 课程

- [商业逻辑](business-logic/index.md)

## 后续可能加入

- AI 课
- 产品课
- 操盘手课
```

- [ ] **Step 2: 创建商业逻辑课程入口**

```markdown
# 商业逻辑课

## 定位

商业逻辑课是高玮课程 LLM Wiki 的第一批资料来源。第一阶段用它验证来源登记、讲次摘要、概念抽取、案例沉淀和应用视图。

## 样本讲次

- [001 从 DAO 看组织的底层逻辑与核心要素](lectures/001-dao-organization-logic.md)
- [020 复盘的方法](lectures/020-review-method.md)
- [034 战略设计的核心要素、制定逻辑](lectures/034-strategy-design.md)
- [042 第一性原理 1](lectures/042-first-principles-1.md)
- [044 业务全链路思维方式](lectures/044-business-full-chain-thinking.md)

## 后续处理

样本流程验证后，再批量扩展到其余讲次。
```

- [ ] **Step 3: 创建 5 个讲次页面骨架**

每个页面采用 `schema/lecture-note.md` 的结构。以 `042-first-principles-1.md` 为例：

```markdown
---
id: lecture-business-logic-042
type: lecture-note
course: business-logic
lecture_id: "042"
teacher: 高玮
title: 第一性原理1：埃隆·马斯克的成功秘笈
source_cards:
  - source-business-logic-042
status: draft
created: 2026-05-14
updated: 2026-05-14
---

# 第一性原理1：埃隆·马斯克的成功秘笈

## 本讲定位

待从来源文字稿中提炼。

## 核心问题

待从来源文字稿中提炼。

## 主要观点

待从来源文字稿中提炼。

## 概念和框架

待从来源文字稿中提炼。

## 案例

待从来源文字稿中提炼。

## 可复用启发

待从来源文字稿中提炼。

## 待验证问题

- 本讲内容需要与后续“第一性原理2：个人运用”合并比较。

## 关联

- 来源卡片：`source-business-logic-042`
```

其他 4 个页面使用同样结构，替换 `lecture_id`、`title` 和来源卡片 ID。

- [ ] **Step 4: 验证**

```powershell
Get-ChildItem -Recurse .\courses
Select-String -Path .\courses\**\*.md -Pattern "待从来源文字稿中提炼"
```

Expected: 课程入口和 5 个讲次页面存在。骨架中的“待从来源文字稿中提炼”只允许出现在第一阶段草稿页面。

- [ ] **Step 5: Commit**

```powershell
git add courses
git commit -m "docs: add initial business logic course pages"
```

### Task 5: 创建第一批来源卡片

**Files:**

- Create: `sources/cards/source-business-logic-001.md`
- Create: `sources/cards/source-business-logic-020.md`
- Create: `sources/cards/source-business-logic-034.md`
- Create: `sources/cards/source-business-logic-042.md`
- Create: `sources/cards/source-business-logic-044.md`

- [ ] **Step 1: 创建来源卡片**

以 `source-business-logic-042.md` 为例：

```markdown
---
id: source-business-logic-042
type: source-card
course: business-logic
lecture_id: "042"
teacher: 高玮
title: 第一性原理1：埃隆·马斯克的成功秘笈
source_format: transcript
source_path: "D:\\Space\\notes\\HomeSpace\\Finance\\Gao\\Business Logic\\LectureText\\042、第一性原理1：埃隆·马斯克的成功秘笈.txt"
status: inventoried
rights: private-reference
created: 2026-05-14
updated: 2026-05-14
---

# 来源卡片：第一性原理1：埃隆·马斯克的成功秘笈

## 来源说明

本来源为高玮商业逻辑课文字稿。

## 文件信息

- 本地路径：`D:\Space\notes\HomeSpace\Finance\Gao\Business Logic\LectureText\042、第一性原理1：埃隆·马斯克的成功秘笈.txt`
- 格式：txt
- 课程：商业逻辑
- 讲次：042

## 已处理产物

- 讲次页面：`courses/business-logic/lectures/042-first-principles-1.md`

## 事实摘录

尚未摘录。

## 推断和待验证

- 需要确认本讲与第 043 讲的关系。

## 关联页面

- `wiki/frameworks/first-principles.md`
```

- [ ] **Step 2: 为其余 4 个样本讲次创建同结构来源卡片**

使用对应文件名、标题、路径和讲次编号：

- `001、从DAO看组织的底层逻辑与核心要素.txt`
- `020、复盘的方法.txt`
- `034、战略设计的核心要素、制定逻辑.txt`
- `044、业务全链路思维方式.txt`

- [ ] **Step 3: 验证**

```powershell
Get-ChildItem .\sources\cards
Select-String -Path .\sources\cards\*.md -Pattern "source_path"
```

Expected: 5 个来源卡片均包含 `source_path`。

- [ ] **Step 4: Commit**

```powershell
git add sources/cards
git commit -m "docs: add source cards for sample lectures"
```

### Task 6: 创建第一批 wiki 知识页

**Files:**

- Create: `wiki/index.md`
- Create: `wiki/frameworks/first-principles.md`
- Create: `wiki/frameworks/review-method.md`
- Create: `wiki/frameworks/business-full-chain-thinking.md`
- Create: `wiki/concepts/organization-logic.md`
- Create: `wiki/frameworks/strategy-design.md`

- [ ] **Step 1: 创建 `wiki/index.md`**

```markdown
# 高玮课程 Wiki

Wiki 层用于沉淀跨课程、跨讲次的稳定知识。它不按课程顺序组织，而按概念、框架、案例、行业和组织问题组织。

## 框架

- [第一性原理](frameworks/first-principles.md)
- [复盘方法](frameworks/review-method.md)
- [业务全链路思维](frameworks/business-full-chain-thinking.md)
- [战略设计](frameworks/strategy-design.md)

## 概念

- [组织底层逻辑](concepts/organization-logic.md)
```

- [ ] **Step 2: 创建 `wiki/frameworks/first-principles.md`**

```markdown
---
id: framework-first-principles
type: framework
title: 第一性原理
status: draft
source_scope:
  - course: business-logic
    lecture_id: "042"
human_checked: false
created: 2026-05-14
updated: 2026-05-14
---

# 第一性原理

## 定义

待从第 042 讲和第 043 讲中综合提炼。

## 解决什么问题

待从来源提炼。

## 使用条件

待从来源提炼。

## 操作步骤

待从来源提炼。

## 典型案例

待从来源提炼。

## 易错点

待从来源提炼。

## 与其他概念的关系

- 关联讲次：`courses/business-logic/lectures/042-first-principles-1.md`

## 来源和证据

- `sources/cards/source-business-logic-042.md`

## 待验证问题

- 是否需要合并第 043 讲形成完整框架。
```

- [ ] **Step 3: 创建其余 4 个 wiki 页面骨架**

使用同样结构，分别关联：

- `review-method.md` 关联第 020 讲。
- `strategy-design.md` 关联第 034 讲。
- `business-full-chain-thinking.md` 关联第 044 讲。
- `organization-logic.md` 关联第 001 讲。

- [ ] **Step 4: 验证**

```powershell
Get-ChildItem -Recurse .\wiki
Select-String -Path .\wiki\**\*.md -Pattern "source_scope|来源和证据"
```

Expected: 每个 wiki 页面都有来源范围或来源证据。

- [ ] **Step 5: Commit**

```powershell
git add wiki
git commit -m "docs: add initial cross-course wiki pages"
```

### Task 7: 创建应用层入口

**Files:**

- Create: `applications/index.md`
- Create: `applications/analysis-toolkit/index.md`
- Create: `applications/personal-use/index.md`
- Create: `applications/ai-context/index.md`

- [ ] **Step 1: 创建 `applications/index.md`**

```markdown
# 应用层

应用层把 wiki 中的稳定知识转化为可使用的工具、模板和 Agent 上下文。

## 入口

- [商业分析工具箱](analysis-toolkit/index.md)
- [个人使用](personal-use/index.md)
- [AI 上下文](ai-context/index.md)
```

- [ ] **Step 2: 创建商业分析工具箱入口**

```markdown
# 商业分析工具箱

## 目标

把课程中的概念、框架和案例整理成可复用的商业分析方法。

## 第一批工具

- 第一性原理分析
- 复盘方法
- 业务全链路分析
- 战略设计

## 使用方式

每个工具页应包含适用场景、输入问题、分析步骤、输出模板和案例。
```

- [ ] **Step 3: 创建个人使用入口**

```markdown
# 个人使用

## 目标

把课程知识转化为个人成长、职业判断、表达、复盘和行动规划的材料。

## 第一批方向

- 职业规划
- 复盘
- 时间管理
- 人脉经营
- 个人品牌
```

- [ ] **Step 4: 创建 AI 上下文入口**

```markdown
# AI 上下文

## 目标

为 Agent、RAG 或长上下文问答提供稳定、可追溯的知识入口。

## 初始索引

- 来源索引：`../../sources/index.md`
- 课程索引：`../../courses/index.md`
- Wiki 索引：`../../wiki/index.md`

## 使用规则

- Agent 回答必须优先引用 wiki 稳定页。
- 当 wiki 页面不足时，再回到讲次页面和来源卡片。
- 当来源证据不足时，必须标记为待验证。
```

- [ ] **Step 5: 验证**

```powershell
Get-ChildItem -Recurse .\applications
```

Expected: 三个应用入口存在。

- [ ] **Step 6: Commit**

```powershell
git add applications
git commit -m "docs: add application layer entry points"
```

### Task 8: 建立维护检查脚本

**Files:**

- Create: `scripts/lint_wiki.py`

- [ ] **Step 1: 创建 `scripts/lint_wiki.py`**

```python
from __future__ import annotations

from pathlib import Path


ROOT = Path(".")
MARKDOWN_DIRS = ["sources", "courses", "wiki", "applications", "schema"]


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for dirname in MARKDOWN_DIRS:
        root = ROOT / dirname
        if root.exists():
            files.extend(sorted(root.rglob("*.md")))
    if (ROOT / "README.md").exists():
        files.append(ROOT / "README.md")
    if (ROOT / "AGENTS.md").exists():
        files.append(ROOT / "AGENTS.md")
    if (ROOT / "log.md").exists():
        files.append(ROOT / "log.md")
    return files


def contains_emoji(text: str) -> bool:
    for char in text:
        codepoint = ord(char)
        if 0x1F300 <= codepoint <= 0x1FAFF:
            return True
    return False


def main() -> None:
    errors: list[str] = []
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        if contains_emoji(text):
            errors.append(f"{path}: contains emoji")
        if path.as_posix().startswith("sources/cards/") and "source_path:" not in text:
            errors.append(f"{path}: source card missing source_path")
        if path.as_posix().startswith("wiki/") and path.name != "index.md":
            if "source_scope:" not in text and "## 来源和证据" not in text:
                errors.append(f"{path}: wiki page missing source evidence")

    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)

    print("lint passed")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 运行检查**

```powershell
uv run python .\scripts\lint_wiki.py
```

Expected: `lint passed`

- [ ] **Step 3: Commit**

```powershell
git add scripts/lint_wiki.py
git commit -m "feat: add wiki maintenance lint"
```

### Task 9: 决定展示层

**Files:**

- Create: `docs/decisions/2026-05-14-display-layer.md`

- [ ] **Step 1: 创建决策记录**

```markdown
# 展示层选择

## 决策

第一阶段优先保持 Markdown 和 Obsidian 兼容，不绑定特定展示软件。

## 原因

- Obsidian 适合本地阅读、双链、图谱和个人使用。
- Markdown 兼容性可以保留未来迁移空间。
- 后续可以追加 Quartz、MkDocs、Docusaurus 或 RAG 索引。
- 第一阶段主要风险不是展示，而是来源追溯、结构分层和维护流程。

## 当前使用方式

- 可以直接用编辑器打开项目目录。
- 如果使用 Obsidian，可将 `D:\Project\Lecture\gao-course-wiki` 作为 vault 打开。
- HomeSpace 中可以创建入口页，链接到本项目关键页面。

## 待复核

- 是否需要安装 Obsidian 插件。
- 是否需要将 `maps/` 中的关系图做成 Obsidian Canvas。
- 是否需要生成静态网站供移动端浏览。
```

- [ ] **Step 2: Commit**

```powershell
git add docs/decisions/2026-05-14-display-layer.md
git commit -m "docs: record display layer decision"
```

### Task 10: 第一轮人工复核和扩展决策

**Files:**

- Modify: `log.md`
- Modify: `docs/plans/2026-05-14-gao-course-llm-wiki-build-plan.md`

- [ ] **Step 1: 人工检查第一轮产物**

检查以下问题：

- 来源路径是否准确。
- 课程层和 wiki 层是否分得清。
- 样本讲次是否足以代表商业逻辑课。
- 页面命名是否适合长期维护。
- Agent 是否能从 `applications/ai-context/index.md` 找到使用入口。

- [ ] **Step 2: 更新 `log.md`**

```markdown
## 2026-05-14 | first-loop-review | 第一轮闭环复核

- 完成来源层、课程层、wiki 层、应用层和维护层最小骨架。
- 完成商业逻辑课样本讲次登记。
- 完成第一批跨课程 wiki 页面骨架。
- 完成展示层初始决策。

人工复核结论：

- 待填写。

下一步：

- 根据复核结果决定批量摄入范围。
```

- [ ] **Step 3: 决定第二阶段范围**

第二阶段三种选择：

1. 扩大样本：继续处理 10 到 20 篇商业逻辑讲次。
2. 横向验证：加入 AI 课或产品课的少量材料，验证跨课程模型。
3. 工具优先：先把商业分析工具箱打磨成可使用模板。

- [ ] **Step 4: Commit**

```powershell
git add log.md docs/plans/2026-05-14-gao-course-llm-wiki-build-plan.md
git commit -m "docs: record first loop review and next scope"
```

## 5. 推荐执行顺序

第一轮推荐只执行 Task 1 到 Task 3，然后停下来复核来源盘点结果。原因是来源盘点会暴露真实文件数量、缺失编号、命名异常和资料边界。

第二轮执行 Task 4 到 Task 6，验证课程层到 wiki 层的转换质量。

第三轮执行 Task 7 到 Task 9，建立应用层和展示层。

Task 10 是第一阶段结束前的人工关口，不建议跳过。

## 6. 需要先讨论的注意事项

### 6.1 是否把 HomeSpace 当作原始资料库

推荐：第一阶段保留 HomeSpace 作为原始资料库，wiki 只记录路径和处理状态。

风险：如果未来移动电脑或调整盘符，路径会失效。缓解方式是在 `sources/raw-paths.md` 中记录根路径变量，并在脚本中集中配置。

### 6.2 是否使用 Obsidian

推荐：第一阶段兼容 Obsidian，但不依赖 Obsidian 插件。

原因：Obsidian 适合浏览和双链，但 LLM Wiki 的核心资产应该是通用 Markdown、schema、日志和来源追溯。

### 6.3 是否直接批量处理全部文字稿

推荐：不要第一步处理全部。先选 5 到 10 篇样本跑通闭环。

原因：如果 schema 或目录分层有问题，小样本更容易返工。等第一轮人工复核通过后，再批量扩展。

### 6.4 是否把个人观点写进同一个 wiki

推荐：可以写，但要区分来源类型。

建议来源类型：

- `course-transcript`：课程文字稿。
- `course-slide`：课件或 PDF。
- `course-video`：视频。
- `personal-note`：个人笔记。
- `external-reference`：外部资料。
- `agent-synthesis`：Agent 综合产物。

### 6.5 是否需要独立素材仓库

当前不需要。等视频、PDF 和课件规模明显变大后，再考虑：

```text
D:\Project\Lecture\gao-course-materials
```

或继续使用：

```text
D:\Space\notes\HomeSpace\Finance\Gao
```

关键是 wiki 中不要硬编码太多散乱路径，而要通过来源卡片统一登记。

## 7. 验收标准

第一阶段完成时，应满足：

- `AGENTS.md` 明确 Agent 工作规则。
- `sources/` 能追溯到原始资料。
- `courses/` 至少有 5 个讲次页面。
- `wiki/` 至少有 5 个跨讲次知识页。
- `applications/` 至少有学习、商业分析、AI 上下文三个入口。
- `scripts/lint_wiki.py` 能检查基础规则。
- `log.md` 记录初始化、样本选择和第一轮复核。
- 没有大视频、PDF、音频被误提交到 git。

## 8. 执行建议

Plan complete and saved to `docs/plans/2026-05-14-gao-course-llm-wiki-build-plan.md`.

Two execution options:

1. Subagent-Driven，推荐用于后续正式实施。每个任务由独立 Agent 执行，主会话负责复核和整合。
2. Inline Execution，适合先完成 Task 1 到 Task 3 的小闭环。

在正式执行前，建议先确认三个问题：

- 第一展示软件是否以 Obsidian 为主。
- 第一批样本是否采用计划中的 5 篇。
- 大文件是否继续留在 HomeSpace。
