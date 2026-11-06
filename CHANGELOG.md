# 更新记录

## 2026-11-06 · 中英双语

- 新增 `README.en.md`：完整英文说明，不是摘要；`README.md` 顶部可切换。
- 新增 `AI-INSTALL.en.md`：英文 AI 建库协议；`AI-INSTALL.md` 顶部可切换。
- 项目名改为中英双语：README 标题与首屏名称行同时出现“个人数据库 / Personal Knowledge Base”。
- 英文版保留目录结构、命令、模板和隐私/备份警告。

## 2026-11-06 · 预览图

- 新增 `docs/images/vault-overview.svg`：Obsidian 布局示意。
- 新增 `docs/images/obsidian-real.png`：Obsidian 1.15.0 真实界面截图。
- 新增 `docs/images/README.md`。
- `README.md` 增加“效果预览”和首屏徽章/简介/新手 3 步。

## 2026-11-06 · v0.1

- 初版通用骨架（规则仍在更新中；以你本地最新 `AGENTS.md` 为准）。
- 文档：
  - `README.md`：给人看，设计原则/目录/快速开始/日常流程/备份/隐私。
  - `AI-INSTALL.md`：给 AI 看，取证/备份/新建/合并/验证/回滚。
  - `docs/rules.md`：命名、frontmatter、类型、状态、链接、标签。
  - `docs/workflow.md`：捕获/每周/每月/项目/会议/论文/决策/复盘。
  - `docs/backup.md`：3-2-1、Git、Windows/Linux、加密、恢复演练。
  - `docs/troubleshooting.md`：断链、孤岛、同步冲突、乱码、AI 改坏、Git 冲突。
- 骨架：
  - `vault-template/00-index.md`
  - `vault-template/AGENTS.md`
  - `01-inbox` / `02-projects` / `03-areas` / `04-resources` / `05-archive`
  - `_templates/note.md` / `project.md` / `meeting.md`
  - 示例笔记/项目
- 脚本：
  - `scripts/check-links.py`：断链/孤岛检查。

## 待办

- [ ] 等用户最新规则更新后，替换 `vault-template/AGENTS.md` 与 `docs/rules.md` 的对应章节。
- [ ] 补真实截图（Obsidian 入口、模板、断链检查）。
- [ ] 补 `new-note.py` 交互式新建。
- [ ] 补 Dataview 查询示例。
- [ ] 补多语言/英文版。
- [ ] 补附件管理规范。