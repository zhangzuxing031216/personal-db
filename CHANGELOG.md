# 更新记录 / Changelog

版本号遵循 SemVer；当前版本见 `VERSION`，发布和对比流程见 `VERSIONING.md`。

## v0.1.0 · 2026-11-06 · 首次发布

### 新增

- 不绑定 App 的 Markdown 个人知识库骨架：目录、模板、双链、周回顾、备份、AI 维护规则。
- 中英双语人看文档：`README.md` / `README.en.md`，顶部可切换。
- 中英双语 AI 建库协议：`AI-INSTALL.md` / `AI-INSTALL.en.md`。
- 骨架：
  - `vault-template/00-index.md`
  - `vault-template/AGENTS.md`
  - `01-inbox` / `02-projects` / `03-areas` / `04-resources` / `05-archive`
  - `_templates/note.md` / `project.md` / `meeting.md`
  - 示例笔记与示例项目
- 文档：
  - `docs/rules.md`
  - `docs/workflow.md`
  - `docs/backup.md`
  - `docs/troubleshooting.md`
- 脚本：`scripts/check-links.py`，检查断链和孤岛。
- 真实截图：`docs/images/obsidian-real.png`（Obsidian 1.15.0）。

### 说明

- 这是第一个公开版本，作为后续版本对比的基线。
- 与下一版本比较：`git diff v0.1.0..v0.2.0`。
- 当前 `vault-template/AGENTS.md` 是通用骨架，仍待用户最新规则替换。
- 示例笔记不含真实隐私数据。

## 未发布 / Unreleased

- [ ] 等用户最新规则更新后，替换 `vault-template/AGENTS.md` 与 `docs/rules.md` 的对应章节。
- [ ] 补 `new-note.py` 交互式新建。
- [ ] 补 Dataview 查询示例。
- [ ] 补附件管理规范。
- [ ] 补英文版深层专题文档。