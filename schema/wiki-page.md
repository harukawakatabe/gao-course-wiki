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

## 字段说明

- `id`：全局唯一标识，格式为 `{type}-{slug}`。
- `type`：`concept`、`framework`、`case`、`industry`、`people-org`。
- `source_scope`：知识来源的课程和讲次列表，至少一条。
- `human_checked`：是否经过人工确认，默认 `false`。
- `status`：`draft`、`reviewed`、`stable`。`stable` 必须 `human_checked: true`。
