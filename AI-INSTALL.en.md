# AI-INSTALL.md · A Vault-Building Protocol for AI

> **Language / 语言**: [中文](AI-INSTALL.md) | English

> Goal: create a usable Markdown personal knowledge base on the user's machine, or merge this template into an existing vault.
> Principles: **look before you act, never overwrite, never delete, never guess at private data, always reversible.**
>
> If the user already has their own rules (`AGENTS.md` / team conventions), **the user's rules take precedence**; this file is only a default skeleton.

---

## 0. Your role

You are the vault-building executor. You must:

1. **Gather evidence first**: the target path, whether a vault already exists, Git status, whether Obsidian is installed.
2. **One step at a time**: run → paste the output → judge → next step.
3. **Never overwrite**: if `00-index.md`, `AGENTS.md`, or notes already exist, back them up or merge them first.
4. **Never delete**: any deletion/move/rename requires user confirmation.
5. **Never write private data**: keys, passwords, ID numbers, client material — none of it, ever.
6. **Always reversible**: back up before changing anything, and hand over the recovery procedure at delivery.
7. **Never fabricate**: do not call an unverified link or command "fine".

---

## 1. Settle 4 things before you start

If you can find it out from the system, do not ask.

1. Where will the vault live? Default `~/my-vault` (Windows `%USERPROFILE%\my-vault`).
2. Is this a **new vault** or a **merge into an existing vault**?
3. Obsidian, or VS Code/Typora/plain files?
4. Do you want Git? private or public?

> If the user says "whatever", default to: new vault, Obsidian, private Git, path `~/my-vault`.

---

## 2. Phase 0 · Gather evidence

### 2.1 Path

```bash
# Linux/macOS
ls -la ~/my-vault 2>/dev/null || echo "NOT_EXISTS"
```

```powershell
# Windows
Test-Path "$env:USERPROFILE\my-vault"
```

### 2.2 Existing vault

```bash
# These files suggest an existing vault
test -f ~/my-vault/00-index.md && echo HAS_INDEX
test -f ~/my-vault/AGENTS.md && echo HAS_AGENTS
test -d ~/my-vault/.git && echo HAS_GIT
```

### 2.3 Tools

```bash
obsidian --version 2>/dev/null || echo "NO_OBSIDIAN_CLI"
git --version
python --version
```

> Obsidian having no CLI is normal; to check whether it is installed, just look at the application list.

### 2.4 Decision

| Result | Branch |
|---|---|
| Path does not exist | Create new |
| Empty directory | Create new |
| `00-index.md` already exists | Merge, do not overwrite |
| `.git` already exists | Run `git status` first; do not overwrite uncommitted changes |
| User has custom rules | Use the user's; the template only fills gaps |

---

## 3. Phase 1 · Backup (mandatory for an existing vault)

```bash
STAMP=$(date +%F-%H%M%S)
cp -r ~/my-vault ~/my-vault.bak.$STAMP
```

Windows:

```powershell
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
Copy-Item "$env:USERPROFILE\my-vault" "$env:USERPROFILE\my-vault.bak.$stamp" -Recurse
```

If the vault is large:

```bash
cd ~/my-vault
git status
git add -A
git commit -m "backup before template merge"
```

> Never use `rm -rf` to wipe an existing vault.

---

## 4. Phase 2 · Copy the skeleton

### 4.1 New vault

```bash
cp -r vault-template ~/my-vault
cd ~/my-vault
```

Windows:

```powershell
Copy-Item .\vault-template "$env:USERPROFILE\my-vault" -Recurse
```

### 4.2 Merge into an existing vault

Copy only the files that **do not already exist**:

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

Template files:

```bash
cp -n /path/to/repo/vault-template/_templates/*.md _templates/ 2>/dev/null || true
```

> `cp -n` does not overwrite existing files. On Windows, run `Test-Path` before using `Copy-Item -ErrorAction SilentlyContinue`.

### 4.3 Do not copy

- Real notes
- `.obsidian/workspace.json` (window layout; differs from machine to machine)
- Attachments (unless the user asks for them)
- `.git` (do not overwrite it in an existing vault)

---

## 5. Phase 3 · Initialize

### 5.1 Check the entry point

Open `00-index.md` and confirm it contains:

- the purpose of the vault;
- a description of the directories;
- a link to the inbox;
- entry points for projects/areas/resources.

Add whatever is missing.

### 5.2 Obsidian (optional)

1. Open folder as vault.
2. Settings → Files and links → use `[[Wikilinks]]`.
3. Settings → Files and links → default location for new notes `01-inbox`.
4. Template folder `_templates`.

### 5.3 Git (optional)

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

> Personal vaults are **private** by default. Do not `git remote add` to a public repository unless the user explicitly wants a public template.

---

## 6. Phase 4 · Write the rules

`AGENTS.md` holds the constraints for the AI. It must contain at least:

```markdown
# Personal vault AI rules

1. Search before writing, to avoid duplicates.
2. Prefer appending; never overwrite existing text.
3. Explain before changing the user's original text.
4. Mark the source of facts; mark the confidence of inferences; flag anything unverified.
5. Never write passwords, tokens, ID numbers, or client-confidential data.
6. Do not delete/move/rename unless the user explicitly asks.
7. After writing, give the path + line number.
8. Follow this vault's directory and frontmatter conventions.
```

> If the user already has rules, do not overwrite them; add the missing entries and say what you added.

---

## 7. Phase 5 · Verify

### 7.1 Files

```bash
test -f ~/my-vault/00-index.md && echo INDEX_OK
test -f ~/my-vault/AGENTS.md && echo AGENTS_OK
for d in 01-inbox 02-projects 03-areas 04-resources 05-archive _templates; do
  test -d ~/my-vault/$d && echo "DIR_OK $d"
done
```

### 7.2 Links

```bash
python scripts/check-links.py ~/my-vault
```

Expected:

- 0 broken links;
- "orphan" hints are acceptable (normal for a new vault).

### 7.3 Write test

Have the AI create a test note in `01-inbox/`:

```markdown
---
title: Test note
type: note
status: inbox
created: 2026-11-06
tags: [test]
---

# Test note

This is an installation test. Related: [[00-index]].
```

Verify:

- the file exists;
- the frontmatter parses;
- the link raises no error;
- the user can open it.

After the test, **ask the user** whether to delete it; do not delete it automatically.

### 7.4 Delivery report

```text
[Conclusion] Success / Partial success / Failure

[Environment]
- OS:
- Vault path:
- Obsidian: yes/no
- Git: yes/no

[Created/Merged]
- Directories:
- Entry point:
- Rules:
- Templates:

[Verification]
- File check:
- Broken-link check:
- Test note:

[Not done / To be confirmed]
- ...

[Backup/Rollback]
- Backup path:
- Rollback command:
```

---

## 8. Rollback

### 8.1 New vault

```bash
rm -rf ~/my-vault   # only after user confirmation
```

### 8.2 Merged vault

```bash
# overwrite with the backup
rm -rf ~/my-vault
mv ~/my-vault.bak.YYYY-MM-DD-HHMMSS ~/my-vault
```

Or with Git:

```bash
cd ~/my-vault
git reset --hard HEAD
```

> You must get user confirmation before deleting/overwriting.

---

## 9. Merge rules (important)

If the user already has a vault:

1. **Do not** overwrite the user's entry point with the template's `00-index.md`.
2. **Do not** rename the user's directories.
3. **Do not** batch-edit frontmatter.
4. Only add the missing directories/templates/rules.
5. If the user's rules conflict with the template → use the user's.
6. If the user has no `AGENTS.md` → you may create one.
7. If the user has an `AGENTS.md` → only suggest appending; do not overwrite.

---

## 10. Privacy and security

- Do not copy real notes into a public repository.
- Do not write keys/passwords into notes.
- Do not push a private vault to a public remote.
- Do not send the user's notes to an external model unless the user explicitly agrees.
- Encrypt backups (for sensitive vaults).
- Redact screenshots/logs.

---

## 11. Prohibitions

1. Do not overwrite existing notes/entry points/rules.
2. Do not delete/move/rename unless the user explicitly asks.
3. Do not state inferences as facts.
4. Do not write keys/ID numbers/private data.
5. Do not fake "checks passed".
6. Do not push a private vault to public GitHub.
7. Do not rewrite the entire vault in one go.

---

## 12. Quick command card

```bash
# New vault
cp -r vault-template ~/my-vault
python scripts/check-links.py ~/my-vault

# Merge
mkdir -p ~/my-vault/{01-inbox,02-projects,03-areas,04-resources,05-archive,_templates}
cp -n vault-template/_templates/*.md ~/my-vault/_templates/

# Git
cd ~/my-vault && git init && git add . && git commit -m "init vault"

# Verify
test -f ~/my-vault/00-index.md && echo OK
```