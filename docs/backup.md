# 备份

## 1. 原则：3-2-1

```text
3 份数据：本机 + 移动盘 + 云
2 种介质：SSD + 云/机械盘
1 份异地：不同城市/不同账号
```

## 2. Git

适合：文本笔记、想留历史、想多机同步。

```bash
cd ~/my-vault
git init
git add .
git commit -m "init vault"
```

`.gitignore`：

```gitignore
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.DS_Store
Thumbs.db
*.tmp
```

远程：

```bash
git remote add origin git@github.com:YOUR_NAME/my-vault.git
git push -u origin main
```

> 私人库用 **private**。公开仓库只放模板。

## 3. Windows 备份

### 3.1 移动盘

```powershell
robocopy "$env:USERPROFILE\my-vault" "E:\backup\my-vault" /MIR /R:2 /W:5 /LOG+:backup.log
```

> `/MIR` 会删除目标多余文件。第一次先不用 `/MIR`，确认方向。

### 3.2 任务计划

- 每周一次。
- 目标：移动盘/另一块盘。
- 保留至少 4 周。

## 4. macOS / Linux

```bash
rsync -av --delete ~/my-vault/ /mnt/backup/my-vault/
```

cron：

```cron
0 3 * * * rsync -a --delete /home/me/my-vault/ /mnt/backup/my-vault/
```

> `--delete` 会删目标多余文件。先 dry-run：`rsync -avn --delete ...`。

## 5. 云

- OneDrive/iCloud/Dropbox：方便，但注意冲突文件。
- 对象存储：R2/OSS/S3，适合打包备份。
- 加密：Cryptomator/VeraCrypt（敏感库）。

不要：

- 只放一个云盘；
- 把 private 库设成公开分享；
- 把密钥放笔记里再同步。

## 6. 加密

敏感库建议：

1. 用 Cryptomator 建加密盘。
2. 库放在加密盘里。
3. 云同步加密盘。
4. 备份也加密。

> 加密后忘记密码 = 数据没了。密码放密码管理器，不写笔记。

## 7. 恢复演练

每季度：

```bash
# 1. 复制备份到临时目录
cp -r /mnt/backup/my-vault ~/restore-test

# 2. 用 Obsidian 打开
# 3. 搜 3 篇笔记
# 4. 打开 2 个附件
# 5. 检查链接
python scripts/check-links.py ~/restore-test

# 6. 确认后删除临时目录
rm -rf ~/restore-test
```

## 8. 版本历史

- Git：每次大改前 commit。
- Obsidian Sync：有版本历史（付费）。
- 文件历史：Windows 文件历史/Time Machine。

## 9. 备份检查表

```text
[ ] 本机有库
[ ] 移动盘/第二块盘有副本
[ ] 云/异地在另一账号
[ ] 私人库 private
[ ] 密钥不在库
[ ] 至少每季度恢复演练
[ ] 备份日志正常
```