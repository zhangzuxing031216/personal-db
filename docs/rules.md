# 规则

## 1. 命名

| 对象 | 规则 | 例 |
|---|---|---|
| 文件 | 英文 kebab-case，`.md` | `caddy-https.md` |
| 标题 | 中文/英文都行，写结论 | `Caddy 自动签 HTTPS` |
| 目录 | 英文 kebab-case | `02-projects/` |
| 标签 | 小写、无空格 | `#linux` `#project` |

> 中文文件名不是错，但跨平台/命令行/URL 容易出问题。标题用中文，文件名用英文最稳。

## 2. frontmatter

```yaml
---
title: 标题
type: note        # note / project / meeting / source / decision / index
status: inbox     # inbox / active / done / archived
created: 2026-11-06
updated: 2026-11-06
tags: [tag1, tag2]
source:           # 可选：URL / 书名 / DOI
---
```

必填：`title`、`type`、`status`、`created`、`tags`。
可选：`updated`、`source`、`deadline`、`attendees`。

## 3. 类型

| type | 用途 | 放哪 |
|---|---|---|
| `note` | 一条知识/结论 | `01-inbox` → `03-areas`/`04-resources` |
| `project` | 有截止日/产出 | `02-projects` |
| `meeting` | 会议/讨论 | `01-inbox` → `02-projects`/`05-archive` |
| `source` | 书/论文/视频 | `04-resources` |
| `decision` | 决策记录 | 项目内或 `03-areas` |
| `index` | 入口/索引 | 根目录 |

## 4. 状态流转

```text
inbox → active → done → archived
```

- `inbox`：还没整理，允许不完整。
- `active`：正在用。
- `done`：完成，但还可能引用。
- `archived`：失效/结束，保留可搜。

> 不要用删除代替归档。

## 5. 链接

```markdown
[[note-stem]]
[[note-stem|显示文字]]
[[note-stem#标题]]
```

- 链接到“概念”，不是“文件位置”。
- 每篇至少 1 个出链（除非是入口）。
- 新建笔记后，回到相关笔记加入链。

## 6. 标签

少而稳定：

- 类型：`#project` `#area` `#source` `#decision`
- 主题：`#linux` `#ai` `#paper`
- 状态：一般不用标签，用 `status`。

不要：

- 每篇一个新标签；
- 用标签代替链接；
- 用中文长句当标签。

## 7. 事实 / 推断 / 未验证

```markdown
【事实】来自官方文档/实测。
【推断】基于事实的判断，标置信度。
【未验证】听说/没跑过。
```

> 这是个人库最重要的规则。AI 最容易把推断写得很像事实。

## 8. 来源

- 网页：URL + 访问日期。
- 书：书名 + 作者 + 页码/章节。
- 论文：标题 + DOI/arXiv。
- 对话：谁说的 + 日期。

没有来源也可以记，但标“个人经验/未核实”。

## 9. 回顾

| 周期 | 做什么 |
|---|---|
| 每天 | 往 inbox 丢 |
| 每周 | 清 inbox、加链接、更新项目 |
| 每月 | 合并重复、找孤岛、检查备份 |
| 每季度 | 归档、恢复演练、隐私检查 |

## 10. AI 规则

见 `vault-template/AGENTS.md`。核心：

1. 先搜再写。
2. 追加优先。
3. 不改原话。
4. 事实/推断分开。
5. 不写隐私。
6. 不删/不移动。
7. 写完给路径/行号。
8. 没验证标出来。

## 11. 反模式

| 反模式 | 后果 | 改法 |
|---|---|---|
| 20 层文件夹 | 找不到 | 5 大类 + 链接 |
| 只收藏不整理 | 垃圾场 | 每周清 inbox |
| 一篇塞所有事 | 无法链接 | 拆成原子笔记 |
| 没有来源 | 无法信任 | 加 source |
| AI 全库重写 | 丢原文 | 追加 + Git |
| 删除代替归档 | 丢历史 | `05-archive` |
| 标签爆炸 | 搜不到 | 少而稳定 |