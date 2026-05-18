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

## 2026-05-14 | schema-confirmed | 指引文件全部确认

- 项目名 `gao-course-wiki` 锁定，不再更改。
- 来源类型字段 `source_type` 写入 schema，含 personal-note / external-reference / agent-synthesis 等类型。
- wiki 正文个人观点用 [个人] 标注，外部资料用 [外部] 标注。
- Obsidian Canvas 和静态网站推迟到内容积累后再评估，零返工风险。
- 所有指引文件（CLAUDE.md / AGENTS.md / schema/ / docs/decisions/）不再有待确认项。

## 2026-05-14 | init-confirmed | 初始化确认项

- 展示软件：Obsidian，插件已安装，vault 指向本项目目录。
- 大文件存放：视频、PDF、音频长期留在 HomeSpace，wiki 只记录路径引用。
- 第一批样本：2 篇（001、018），先确保回数和来源绑定正确，再继续扩展。
- 来源文件名：部分文件名含顿号，已确认路径无误。
- 提炼工作流约定写入 `CLAUDE.md`，触发口令：`提炼讲次 <id>` / `批量提炼 <id1> <id2> ...`。

## 2026-05-14 | lecture-001-summarized | 提炼讲次 001

- 读取来源卡片 `sources/cards/source-business-logic-001.md`，确认文字稿路径为 `D:\Space\notes\HomeSpace\Finance\Gao\Business Logic\LectureText\001、从DAO看组织的底层逻辑与核心要素.txt`。
- 填充讲次页面 `courses/business-logic/lectures/001-dao-organization-logic.md`，覆盖本讲定位、核心问题、主要观点、概念框架、案例和可复用启发。
- 更新来源卡片状态为 `summarized`，补充事实摘录和推断/待验证项。
- 更新 wiki 页面 `wiki/concepts/organization-logic.md`，沉淀组织底层逻辑、DAO 组织思想、贝壳 ACN 案例和待验证边界。

## 2026-05-14 | lecture-018-summarized | 提炼讲次 018

- 填充讲次页面 `courses/business-logic/lectures/018-review-method.md`，覆盖本讲定位、核心问题、主要观点、概念框架、案例和可复用启发。
- 更新 wiki 页面 `wiki/frameworks/review-method.md`，沉淀复盘定义、适用条件、五步法、七个不放过、直播软件稳定度案例和易错点。

- 在 `AGENTS.md` 和 `CLAUDE.md` 增加约束：`courses/business-logic/lectures/` 的讲次编号必须与 `HomeSpace\Finance\Gao\Business Logic\LectureText` 中原始文字稿编号严格对应。

## 2026-05-17 | lecture-018-source-extraction-corrected | 重新提炼讲次 018

- 读取来源卡片 `sources/cards/source-business-logic-018.md`，确认文字稿路径为 `D:\Space\notes\HomeSpace\Finance\Gao\Business Logic\LectureText\018、从 ChatGPT 看 AI 是否会抢走人类饭碗.txt`。
- 核对原始文字稿编号和正文主题：讲次为第十八回“从最近爆火的 ChatGPT 看 AI 是否会抢走人类饭碗”。
- 删除旧讲次页面 `courses/business-logic/lectures/018-review-method.md`，新增讲次页面 `courses/business-logic/lectures/018-ai-chatgpt-human-work.md`，按正文主题覆盖本讲定位、核心问题、主要观点、概念框架、案例和可复用启发。
- 更新来源卡片状态为 `summarized`，补充 ChatGPT、AIGC、搜索与推荐引擎、传统行业 AI 应用和信息甄别相关事实摘录与推断/待验证项。
- 删除缺少 018 正文证据支撑的旧 wiki 页面 `wiki/frameworks/review-method.md`，新增 wiki 页面 `wiki/frameworks/ai-capability-boundary.md`，沉淀 AI 能力边界与产业应用判断框架。
- 更新课程索引和 wiki 索引，指向重新提炼后的 018 讲次页和 AI 框架页。
- 运行 `python scripts\lint_wiki.py`，结果通过。

## 2026-05-18 | lecture-018-resummarized | 覆盖重提炼讲次 018

- 读取来源卡片 `sources/cards/source-business-logic-018.md`，确认文字稿路径为 `D:\Space\notes\HomeSpace\Finance\Gao\Business Logic\LectureText\018、从 ChatGPT 看 AI 是否会抢走人类饭碗.txt`。
- 再次核对原始文字稿：讲次为第十八回“从最近爆火的 ChatGPT 看 AI 是否会抢走人类饭碗”。
- 覆盖讲次页面 `courses/business-logic/lectures/018-ai-chatgpt-human-work.md`，按正文主线重写本讲定位、核心问题、主要观点、概念框架、案例和可复用启发。
- 覆盖来源卡片 `sources/cards/source-business-logic-018.md`，收紧事实摘录与推断/待验证项，使其更贴近原文的三段结构和 AI 判断主线。
- 覆盖 wiki 页面 `wiki/frameworks/ai-capability-boundary.md`，继续沉淀 AI 能力边界、搜索与语言模型边界、传统行业落地前提和信息甄别框架。

## 2026-05-18 | lecture-040-042-removed | 删除错误回数绑定的 040 与 042 派生产物

- 根据 `sources/raw-paths.md` 与当前原始目录 `D:\Project\Lecture\gao-course-raw\LectureText\Transcript` 复核，确认原项目中的 040 与 042 派生产物对应关系已不再成立。
- 删除讲次页面 `courses/business-logic/lectures/040-first-principles-1.md` 与 `courses/business-logic/lectures/042-business-full-chain-thinking.md`。
- 删除来源卡片 `sources/cards/source-business-logic-040.md` 与 `sources/cards/source-business-logic-042.md`。
- 删除 wiki 页面 `wiki/frameworks/first-principles.md` 与 `wiki/frameworks/business-full-chain-thinking.md`。
- 更新课程索引、wiki 索引与 README，保留原始来源盘点，等待前置讲次完成后按正确回数重新提炼。
