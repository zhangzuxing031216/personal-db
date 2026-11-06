# 个人数据库 · Markdown 知识库骨架

> 一个**可搜索、可链接、可备份、可交给 AI 维护**的个人知识库。
> 不绑定某个 App：核心是 Markdown 文件；Obsidian 只是最省事的查看器。
> 适合：读书笔记、项目记录、决策日志、踩坑手册、论文素材、日常收件箱。
>
> - 不会用 AI？看这份 `README.md`。
> - 想让 AI 帮你建库/整理？把 `AI-INSTALL.md` 丢给 AI。
> - 规则以 `vault-template/AGENTS.md` 为准；本仓库是**通用骨架**，不是你的私人笔记。

---

## 目录

- [1. 它是什么](#1-它是什么)
- [2. 五条设计原则](#2-五条设计原则)
- [3. 目录结构](#3-目录结构)
- [4. 快速开始](#4-快速开始)
- [5. 一条笔记怎么写](#5-一条笔记怎么写)
- [6. 日常流程](#6-日常流程)
- [7. 让 AI 维护](#7-让-ai-维护)
- [8. 搜索与回顾](#8-搜索与回顾)
- [9. 备份](#9-备份)
- [10. 隐私](#10-隐私)
- [11. 常见问题](#11-常见问题)
- [附录 A：文件清单](#附录-a文件清单)
- [附录 B：最小示例](#附录-b最小示例)

---

## 1. 它是什么

个人数据库不是“装一个软件”，而是：

```text
一堆 Markdown 文件
  + 稳定的目录/命名
  + 双向链接
  + 标签/属性
  + 定期回顾
  + 备份
  + 可选的 AI 检索/写作
```

它解决的问题：

| 问题 | 做法 |
|---|---|
| 东西找不到 | 固定入口 + 搜索 + 链接 |
| 记了不看 | 收件箱 + 每周回顾 |
| 同一件事记三遍 | 先搜再写，合并到一条 |
| AI 乱改笔记 | 规则 + 先读后写 + 追加优先 |
| 换软件就丢 | 纯 Markdown，随时迁移 |
| 电脑坏了就没了 | Git + 异地备份 |

> 不要一上来设计 20 个文件夹。先能用，再长结构。

---

## 2. 五条设计原则

### 2.1 一条笔记一个主题

标题写“结论/问题”，不写“杂项”。

```text
好：如何用 Caddy 自动签 HTTPS
差：笔记1
```

### 2.2 先搜再写

新建前先搜标题/标签/关键词。已有就追加，不重复造。

### 2.3 链接优先于文件夹

文件夹只分大类；真正的关系用 `[[wikilink]]`。

```markdown
参见 [[caddy-https]] 和 [[backup-3-2-1]]。
```

### 2.4 事实与推断分开

```markdown
【事实】Caddy 首次启动会自动申请证书。
【推断】如果 80 端口不通，ACME 会失败。（置信度：高）
【未验证】Cloudflare 代理下的行为。
```

### 2.5 定期回顾

没有回顾的笔记库 = 垃圾场。
每周清收件箱，每月合并重复，每季度归档。

---

## 3. 目录结构

```text
vault/
├─ 00-index.md              ★ 入口：从这里进
├─ 01-inbox/                收件箱：先记，后整理
├─ 02-projects/             有截止日/有产出的事
├─ 03-areas/                长期责任（健康/财务/团队）
├─ 04-resources/            主题资料（技术/读书/论文）
├─ 05-archive/              完成/失效，保留可搜
├─ _templates/              模板
│  ├─ note.md
│  ├─ project.md
│  └─ meeting.md
├─ _attachments/            图片/PDF（可选）
└─ AGENTS.md                给 AI 的规则
```

规则：

- 目录名用英文 kebab-case，内容可以用中文。
- 项目结束后移到 `05-archive/`，不要删。
- 收件箱允许乱，但每周必须清。
- 附件放 `_attachments/`，不要散落。

> 这是骨架，不是法律。你可以改目录名，但**入口、收件箱、归档**这三件事别省。

---

## 4. 快速开始

### 4.1 复制骨架

```bash
cp -r vault-template ~/my-vault
cd ~/my-vault
```

Windows：

```powershell
Copy-Item .\vault-template "$env:USERPROFILE\my-vault" -Recurse
```

### 4.2 用 Obsidian 打开

1. 安装 Obsidian。
2. “Open folder as vault” 选 `my-vault`。
3. 打开 `00-index.md`。
4. 设置 → 文件与链接 → 使用 `[[Wikilinks]]`。

> 不用 Obsidian 也行：VS Code + Markdown 预览、Typora、Logseq 都能读。

### 4.3 写第一条

在 `01-inbox/` 新建：

```markdown
---
title: 今天学到的一个命令
type: note
status: inbox
created: 2026-11-06
tags: [cli, linux]
---

# 今天学到的一个命令

`ss -lntp` 可以看本机监听端口。

【事实】`-l` 只显示 listening，`-n` 不解析服务名，`-p` 显示进程。
【待办】把它加到 [[linux-cheatsheet]]。
```

### 4.4 链接

在 `00-index.md` 加：

```markdown
- [[今天学到的一个命令]]
```

### 4.5 每周整理

把收件箱里的笔记：

- 合并到已有主题；
- 移到 `02-projects/` / `03-areas/` / `04-resources/`；
- 补标签/来源；
- 加链接；
- 归档过期的。

---

## 5. 一条笔记怎么写

### 5.1 最小 frontmatter

```yaml
---
title: 标题
type: note        # note / project / meeting / source / decision
status: inbox     # inbox / active / done / archived
created: 2026-11-06
updated: 2026-11-06
tags: [tag1, tag2]
source:           # 链接/书名/DOI，可选
---
```

> 属性不是越多越好。至少 `title`、`type`、`status`、`created`、`tags`。

### 5.2 正文结构

```markdown
# 标题

## 一句话结论

## 事实

## 我的判断

## 行动

## 相关
- [[...]]
```

### 5.3 好的笔记 vs 差的笔记

| 好 | 差 |
|---|---|
| 标题是结论 | “随手记” |
| 有来源 | 不知道哪来的 |
| 有日期 | 不知道新旧 |
| 有链接 | 孤岛 |
| 有下一步 | 写完就忘 |
| 事实/推断分开 | 混在一起 |

### 5.4 标签

- 少而稳定：`#project`、`#area`、`#source`、`#decision`。
- 不要给每篇都建新标签。
- 标签用英文/拼音，避免空格。

---

## 6. 日常流程

### 6.1 每天

```text
看到/想到 → 丢 01-inbox（30 秒内）
不追求格式，先记下来
```

### 6.2 每周（20 分钟）

```text
[ ] 清空 01-inbox
[ ] 合并重复
[ ] 给新笔记加链接
[ ] 更新 00-index
[ ] 归档完成的
```

### 6.3 每月（30 分钟）

```text
[ ] 搜重复标题
[ ] 检查孤岛笔记（没有入链/出链）
[ ] 更新项目状态
[ ] 备份验证
```

### 6.4 每季度

```text
[ ] 归档失效内容
[ ] 合并同一主题
[ ] 检查隐私/密钥
[ ] 导出/异地备份
```

---

## 7. 让 AI 维护

### 7.1 把规则给 AI

把 `vault-template/AGENTS.md` 放在库根目录。AI 进入库时先读它。

规则核心：

1. **先搜再写**。
2. **追加优先**，不覆盖。
3. **不改用户原文**，要改先说明。
4. **事实标来源**，推断标置信度，未验证标出来。
5. **不写密钥/证件号/隐私**。
6. **写完给路径/行号**。

### 7.2 常见指令

```text
把这段丢进收件箱，按模板整理。
搜一下“Caddy 证书”，把新踩坑追加到已有笔记。
把这周的会议记录合并成一条决策日志。
找出没有链接的孤岛笔记。
把这篇论文整理成 source 笔记，标出可引用原句。
```

### 7.3 AI 不该做什么

- 不要让它一次重写整个库。
- 不要让它自动删笔记。
- 不要让它把推断写成事实。
- 不要让它把私人内容发到外部服务。
- 不要让它把 key/密码写进笔记。

### 7.4 可选：Basic Memory / 检索工具

- Obsidian 自带搜索够用。
- 需要 AI 语义检索时，可接 Basic Memory、 embeddings、ripgrep。
- 无论用什么，**Markdown 是源**，工具只是索引。

---

## 8. 搜索与回顾

### 8.1 搜索

- Obsidian：`Ctrl+Shift+F` 全库搜索。
- VS Code：`Ctrl+Shift+F`。
- 命令行：`rg "关键词"`。

### 8.2 找孤岛

```bash
python scripts/check-links.py vault
```

会报告：

- 断链（`[[不存在]]`）；
- 没有被链接的笔记；
- 没有出链的笔记。

### 8.3 回顾

- 每周看 `01-inbox/`。
- 每月看 `02-projects/` 状态。
- 每季度看 `05-archive/` 是否可删（一般别删）。

---

## 9. 备份

### 9.1 3-2-1

```text
3 份数据：本机 + 移动盘 + 云
2 种介质：SSD + 云/机械盘
1 份异地：不同城市/不同账号
```

### 9.2 Git

```bash
cd ~/my-vault
git init
git add .
git commit -m "init vault"
```

> 私人笔记仓库默认 **private**。不要把个人日记/客户资料推到 public。

### 9.3 自动备份

- Windows：任务计划 + `robocopy` 到移动盘。
- macOS/Linux：`rsync` + `cron`。
- 云：OneDrive/iCloud/Dropbox（注意冲突）。
- 加密：敏感库用 Cryptomator/VeraCrypt。

### 9.4 恢复演练

每季度：

1. 从备份复制到临时目录；
2. 用 Obsidian 打开；
3. 搜 3 篇笔记；
4. 确认附件/链接正常。

> 没演练过的备份，不算备份。

---

## 10. 隐私

- 公开仓库只放**模板**，不放真实笔记。
- 私人库默认 private。
- 不写：密码、token、cookie、证件号、银行卡、客户隐私。
- 截图前打码。
- 用 AI 前确认 provider 的数据政策。
- 备份加密。

---

## 11. 常见问题

**Q：必须用 Obsidian 吗？**
A：不。Markdown 是核心；Obsidian 只是查看器/链接器。

**Q：文件夹怎么分？**
A：先 `inbox / projects / areas / resources / archive`，够用一年。

**Q：标签还是文件夹？**
A：文件夹分大类，标签做横切；链接做关系。

**Q：笔记太多怎么办？**
A：合并同主题、归档过期、加索引；不要靠更多文件夹。

**Q：AI 会改坏吗？**
A：规则 + 备份 + 先读后写 + 追加优先；重要库用 Git，改前 commit。

**Q：能用中文文件名吗？**
A：能，但跨平台/工具链容易出问题；建议英文 kebab-case，标题用中文。

**Q：需要数据库吗？**
A：个人规模 Markdown 足够；需要全文/语义检索再加索引工具。

---

## 附录 A：文件清单

| 文件 | 作用 |
|---|---|
| `vault-template/00-index.md` | 库入口 |
| `vault-template/01-inbox/` | 收件箱 |
| `vault-template/02-projects/` | 项目 |
| `vault-template/03-areas/` | 长期领域 |
| `vault-template/04-resources/` | 资料 |
| `vault-template/05-archive/` | 归档 |
| `vault-template/_templates/` | 模板 |
| `vault-template/AGENTS.md` | 给 AI 的规则 |
| `scripts/check-links.py` | 断链/孤岛检查 |
| `AI-INSTALL.md` | 给 AI 的建库协议 |
| `docs/` | 规则、流程、备份、排错 |

## 附录 B：最小示例

```text
my-vault/
├─ 00-index.md
├─ 01-inbox/
│  └─ ss-command.md
├─ 04-resources/
│  └─ linux-cheatsheet.md
└─ AGENTS.md
```

`ss-command.md`：

```markdown
---
title: ss 命令看监听端口
type: note
status: inbox
created: 2026-11-06
tags: [linux, cli]
---

# ss 命令看监听端口

`ss -lntp` = listening + numeric + tcp + process。

【事实】需要 root 才能看到所有进程。
【相关】[[linux-cheatsheet]]
```

> 先写，再整理。不要因为“格式不完美”而不记。