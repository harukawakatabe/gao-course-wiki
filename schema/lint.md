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

## 自动化覆盖范围

`scripts/lint_wiki.py` 当前检查：

- emoji 检测（扫描所有 Markdown 文件）。
- 来源卡片是否包含 `source_path`。
- wiki 页面是否包含 `source_scope` 或 `## 来源和证据`。

人工复核无法被自动化替代，仍需定期人工检查建议检查项。
