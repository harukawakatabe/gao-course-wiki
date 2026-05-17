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

## 字段说明

- `id`：全局唯一标识，格式为 `source-{course}-{lecture_id}`。
- `type`：固定为 `source-card`。
- `course`：课程 slug，如 `business-logic`。
- `lecture_id`：三位讲次编号，字符串类型。
- `source_format`：`transcript`（文字稿）、`slide`、`video`、`audio`、`pdf`、`image`。
- `source_type`：内容来源性质，必填。
  - `course-transcript`：课程文字稿
  - `course-slide`：课件或 PDF
  - `course-video`：视频
  - `personal-note`：个人观点、笔记、感悟
  - `external-reference`：外部资料、书籍、文章
  - `agent-synthesis`：Agent 综合产物（必须追溯来源）
- `status`：`inventoried`、`summarized`、`linked`、`reviewed`。
- `rights`：`private-reference`（私有参考）、`public`（可公开）。
