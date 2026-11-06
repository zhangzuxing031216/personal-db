# AI-INSTALL.md · 给 AI 的建库协议

> **Language / 语言**: 中文 | [English](AI-INSTALL.en.md)

> 目标：在用户机器上创建一个可用的 Markdown 个人知识库，或把本模板合并进已有库。
> 原则：**先看再动、不覆盖、不删、不猜隐私、可回滚。**
>
> 如果用户已有自己的规则（`AGENTS.md` / 团队规范），**以用户的为准**；本文件只是默认骨架。

---

## 0. 你的角色

你是建库执行者。必须：

1. **先取证**：目标路径、是否已有库、Git 状态、Obsidian 是否安装。
2. **一次一步**：执行 → 贴输出 → 判定 → 下一步。
3. **不覆盖**：已有 `00-index.md`、`AGENTS.md`、笔记，先备份/合并。
4. **不删**：任何删除/移动/重命名都要用户确认。
5. **不写隐私**：key、密码、证件号、客户资料，一律不写。
6. **可回滚**：改前备份，交付时给恢复方法。
7. **不编造**：没验证的链接/命令不说“正常”。

---

## 1. 开工前问清 4 件事

能从系统查到就不问。

1. 库建在哪？默认 `~/my-vault`（Windows `%USERPROFILE%\my-vault`）。
2. 是**新建**还是**合并进已有库**？
3. 是否用 Obsidian？还是 VS Code/Typora/纯文件？
4. 是否要 Git？private 还是 public？

> 如果用户说“随便”，默认：新建、Obsidian、private Git、路径 `~/my-vault`。

---

## 2. 阶段 0 · 取证

### 2.1 路径

```bash
# Linux/macOS
ls -la ~/my-vault 2>/dev/null || echo "NOT_EXISTS"
```

```powershell
# Windows
Test-Path "$env:USERPROFILE\my-vault"
```

### 2.2 已有库

```bash
# 有这些文件说明可能是已有库
test -f ~/my-vault/00-index.md && echo HAS_INDEX
test -f ~/my-vault/AGENTS.md && echo HAS_AGENTS
test -d ~/my-vault/.git && echo HAS_GIT
```

### 2.3 工具

```bash
obsidian --version 2>/dev/null || echo "NO_OBSIDIAN_CLI"
git --version
python --version
```

> Obsidian 没有 CLI 是正常的；检查是否安装看应用列表即可。

### 2.4 判定

| 结果 | 分支 |
|---|---|
| 路径不存在 | 新建 |
| 空目录 | 新建 |
| 已有 `00-index.md` | 合并，不覆盖 |
| 已有 `.git` | 先 `git status`，不要覆盖未提交改动 |
| 用户有自定义规则 | 用用户的，模板只补缺 |

---

## 3. 阶段 1 · 备份（已有库必做）

```bash
STAMP=$(date +%F-%H%M%S)
cp -r ~/my-vault ~/my-vault.bak.$STAMP
```

Windows：

```powershell
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
Copy-Item "$env:USERPROFILE\my-vault" "$env:USERPROFILE\my-vault.bak.$stamp" -Recurse
```

如果库很大：

```bash
cd ~/my-vault
git status
git add -A
git commit -m "backup before template merge"
```

> 不要用 `rm -rf` 清空已有库。

---

## 4. 阶段 2 · 复制骨架

### 4.1 新建

```bash
cp -r vault-template ~/my-vault
cd ~/my-vault
```

Windows：

```powershell
Copy-Item .\vault-template "$env:USERPROFILE\my-vault" -Recurse
```

### 4.2 合并进已有库

只复制**不存在的**文件：

```bash
cd ~/my-vault
for f in 00-index.md AGENTS.md; do
  if [ -e "$f" ]; then
    echo "SKIP existing $f"
  else
    cp "/path/to/repo/vault-template/$f" .
  fi
done

for d in 01-inbox 02-projects 03-areas 04-resources 05-archive _templates; do
  mkdir -p "$d"
done
```

模板文件：

```bash
cp -n /path/to/repo/vault-template/_templates/*.md _templates/ 2>/dev/null || true
```

> `cp -n` 不覆盖已有文件。Windows 用 `Copy-Item -ErrorAction SilentlyContinue` 前先 `Test-Path`。

### 4.3 不要复制

- 真实笔记
- `.obsidian/workspace.json`（窗口布局，因机器而异）
- 附件（除非用户要）
- `.git`（已有库不要覆盖）

---

## 5. 阶段 3 · 初始化

### 5.1 检查入口

打开 `00-index.md`，确认有：

- 库的用途；
- 目录说明；
- 收件箱链接；
- 项目/领域/资源入口。

没有就补。

### 5.2 Obsidian（可选）

1. Open folder as vault。
2. 设置 → 文件与链接 → 使用 `[[Wikilinks]]`。
3. 设置 → 文件与链接 → 新笔记默认位置 `01-inbox`。
4. 模板目录 `_templates`。

### 5.3 Git（可选）

```bash
cd ~/my-vault
git init
cat > .gitignore <<'EOF'
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.DS_Store
Thumbs.db
*.tmp
EOF
git add .
git commit -m "init personal knowledge base"
```

> 私人库默认 **private**。不要 `git remote add` 到 public 仓库，除非用户明确要公开模板。

---

## 6. 阶段 4 · 写规则

`AGENTS.md` 是给 AI 的约束。至少包含：

```markdown
# 个人库 AI 规则

1. 写前先搜，避免重复。
2. 追加优先，不覆盖原文。
3. 改用户原文前先说明。
4. 事实标来源；推断标置信度；未验证标出来。
5. 不写密码、token、证件号、客户隐私。
6. 不删除/移动/重命名，除非用户明确要求。
7. 写完给路径 + 行号。
8. 遵守本库目录和 frontmatter 规范。
```

> 如果用户已有规则，不要覆盖；把缺的条目补进去，并说明。

---

## 7. 阶段 5 · 验证

### 7.1 文件

```bash
test -f ~/my-vault/00-index.md && echo INDEX_OK
test -f ~/my-vault/AGENTS.md && echo AGENTS_OK
for d in 01-inbox 02-projects 03-areas 04-resources 05-archive _templates; do
  test -d ~/my-vault/$d && echo "DIR_OK $d"
done
```

### 7.2 链接

```bash
python scripts/check-links.py ~/my-vault
```

期望：

- 0 个断链；
- 允许“孤岛”提示（新库正常）。

### 7.3 写入测试

让 AI 在 `01-inbox/` 新建一条测试笔记：

```markdown
---
title: 测试笔记
type: note
status: inbox
created: 2026-11-06
tags: [test]
---

# 测试笔记

这是一条安装测试。相关：[[00-index]]。
```

验证：

- 文件存在；
- frontmatter 可解析；
- 链接不报错；
- 用户可以打开。

测试后**询问用户**是否删除；不要自动删。

### 7.4 交付报告

```text
【结论】成功 / 部分成功 / 失败

【环境】
- OS：
- 库路径：
- Obsidian：有/无
- Git：有/无

【创建/合并】
- 目录：
- 入口：
- 规则：
- 模板：

【验证】
- 文件检查：
- 断链检查：
- 测试笔记：

【未做/待确认】
- ...

【备份/回滚】
- 备份路径：
- 回滚命令：
```

---

## 8. 回滚

### 8.1 新建库

```bash
rm -rf ~/my-vault   # 仅在用户确认后
```

### 8.2 合并库

```bash
# 用备份覆盖
rm -rf ~/my-vault
mv ~/my-vault.bak.YYYY-MM-DD-HHMMSS ~/my-vault
```

或 Git：

```bash
cd ~/my-vault
git reset --hard HEAD
```

> 删除/覆盖前必须让用户确认。

---

## 9. 合并规则（重要）

如果用户已有库：

1. **不要**用模板的 `00-index.md` 覆盖用户的入口。
2. **不要**重命名用户目录。
3. **不要**批量改 frontmatter。
4. 只补缺失的目录/模板/规则。
5. 用户规则与模板冲突 → 用用户的。
6. 用户没有 `AGENTS.md` → 可以新建。
7. 用户有 `AGENTS.md` → 只建议追加，不覆盖。

---

## 10. 隐私与安全

- 不把真实笔记复制到公开仓库。
- 不把 key/密码写进笔记。
- 不把私人库推到 public。
- 不把用户笔记发给外部模型，除非用户明确同意。
- 备份加密（敏感库）。
- 截图/日志打码。

---

## 11. 禁止事项

1. 不覆盖已有笔记/入口/规则。
2. 不删除/移动/重命名，除非用户明确要求。
3. 不把推断写成事实。
4. 不写密钥/证件号/隐私。
5. 不伪造“检查通过”。
6. 不把私人库推到公开 GitHub。
7. 不一次重写整个库。

---

## 12. 快速命令卡

```bash
# 新建
cp -r vault-template ~/my-vault
python scripts/check-links.py ~/my-vault

# 合并
mkdir -p ~/my-vault/{01-inbox,02-projects,03-areas,04-resources,05-archive,_templates}
cp -n vault-template/_templates/*.md ~/my-vault/_templates/

# Git
cd ~/my-vault && git init && git add . && git commit -m "init vault"

# 验证
test -f ~/my-vault/00-index.md && echo OK
```