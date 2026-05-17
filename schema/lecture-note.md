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

## 字段说明

- `id`：全局唯一标识，格式为 `lecture-{course}-{lecture_id}`。
- `type`：固定为 `lecture-note`。
- `source_cards`：引用的来源卡片 ID 列表，至少一个。
- `status`：`draft`、`reviewed`、`stable`。
