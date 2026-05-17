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
- 第一批样本：5 篇（001、018、032、040、042），足够验证流程。
- 来源文件名：部分文件名含顿号（如"032、战略设计…"），已确认路径无误。
- 提炼工作流约定写入 `CLAUDE.md`，触发口令：`提炼讲次 <id>` / `批量提炼 <id1> <id2> ...`。

## 2026-05-14 | lecture-001-summarized | 提炼讲次 001

- 读取来源卡片 `sources/cards/source-business-logic-001.md`，确认文字稿路径为 `D:\Space\notes\HomeSpace\Finance\Gao\Business Logic\LectureText\001、从DAO看组织的底层逻辑与核心要素.txt`。
- 填充讲次页面 `courses/business-logic/lectures/001-dao-organization-logic.md`，覆盖本讲定位、核心问题、主要观点、概念框架、案例和可复用启发。
- 更新来源卡片状态为 `summarized`，补充事实摘录和推断/待验证项。
- 更新 wiki 页面 `wiki/concepts/organization-logic.md`，沉淀组织底层逻辑、DAO 组织思想、贝壳 ACN 案例和待验证边界。

## 2026-05-14 | lecture-032-summarized | 提炼讲次 032


## 2026-05-14 | lecture-018-summarized | 提炼讲次 018

- 填充讲次页面 `courses/business-logic/lectures/018-review-method.md`，覆盖本讲定位、核心问题、主要观点、概念框架、案例和可复用启发。
- 更新 wiki 页面 `wiki/frameworks/review-method.md`，沉淀复盘定义、适用条件、五步法、七个不放过、直播软件稳定度案例和易错点。

- 在 `AGENTS.md` 和 `CLAUDE.md` 增加约束：`courses/business-logic/lectures/` 的讲次编号必须与 `HomeSpace\Finance\Gao\Business Logic\LectureText` 中原始文字稿编号严格对应。
