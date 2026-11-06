#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查 Markdown 知识库的断链和孤岛笔记。

用法：
  python scripts/check-links.py ~/my-vault
  python scripts/check-links.py vault-template

检查：
  1. [[wikilink]] 目标是否存在（笔记 stem / 目录名 / 相对路径）
  2. 相对 Markdown 链接 [x](path.md) 是否存在
  3. 没有任何入链/出链的孤岛笔记

退出码：
  0 = 没有断链（孤岛只警告）
  1 = 有断链
  2 = 路径错误
"""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

SKIP_DIRS = {".git", ".obsidian", "node_modules", "__pycache__", "_templates"}
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MDLINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def is_skipped(path: Path, root: Path) -> bool:
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        return True
    return any(p in SKIP_DIRS for p in parts)


def normalize_target(raw: str) -> str:
    return unquote(raw.strip().strip("<>")).split("#", 1)[0].split("?", 1)[0]


def strip_code(text: str) -> str:
    """忽略代码块/行内代码里的示例链接。"""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"~~~.*?~~~", "", text, flags=re.S)
    text = re.sub(r"`[^`]*`", "", text)
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", help="知识库根目录")
    args = ap.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: 不是目录：{root}", file=sys.stderr)
        return 2

    files = [p for p in root.rglob("*.md") if not is_skipped(p, root)]
    if not files:
        print(f"ERROR: 没有找到 Markdown 文件：{root}", file=sys.stderr)
        return 2

    stems = {p.stem for p in files}
    dirs = {p.name for p in root.rglob("*") if p.is_dir() and not is_skipped(p, root)}
    rel_files = {p.relative_to(root).as_posix() for p in files}

    broken = []
    inbound = {p: 0 for p in files}
    outbound = {p: 0 for p in files}
    stem_to_file = {}
    for p in files:
        stem_to_file.setdefault(p.stem, []).append(p)

    for p in files:
        text = strip_code(p.read_text(encoding="utf-8", errors="replace"))
        relp = p.relative_to(root).as_posix()

        for m in WIKILINK.finditer(text):
            target = m.group(1).strip()
            if not target:
                continue
            target = normalize_target(target)
            if not target:
                continue
            if target in stems or target in dirs or target in rel_files or (target + ".md") in rel_files:
                outbound[p] += 1
                if target in stem_to_file:
                    for t in stem_to_file[target]:
                        if t != p:
                            inbound[t] += 1
            else:
                broken.append((relp, f"[[{target}]]", "wikilink target not found"))

        for m in MDLINK.finditer(text):
            raw = m.group(1).strip()
            if not raw or raw.startswith(("http://", "https://", "mailto:", "tel:", "#")):
                continue
            target = normalize_target(raw)
            if not target:
                continue
            if target.startswith("/"):
                candidate = root / target.lstrip("/")
            else:
                candidate = (p.parent / target).resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                broken.append((relp, raw, "link escapes vault"))
                continue
            if not candidate.exists():
                broken.append((relp, raw, "file not found"))
            else:
                outbound[p] += 1

    print(f"扫描：{root}")
    print(f"笔记：{len(files)}")
    print(f"目录：{len(dirs)}")

    if broken:
        print(f"\n断链：{len(broken)}")
        for relp, target, why in broken[:100]:
            print(f"  {relp}: {target}  ({why})")
        if len(broken) > 100:
            print(f"  ... 还有 {len(broken) - 100} 条")
    else:
        print("\n断链：0")

    orphans = []
    for p in files:
        relp = p.relative_to(root).as_posix()
        if relp in ("00-index.md", "AGENTS.md"):
            continue
        if inbound[p] == 0 and outbound[p] == 0:
            orphans.append(relp)

    if orphans:
        print(f"\n孤岛（无入链/出链）：{len(orphans)}")
        for relp in orphans[:50]:
            print(f"  {relp}")
    else:
        print("\n孤岛：0")

    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())