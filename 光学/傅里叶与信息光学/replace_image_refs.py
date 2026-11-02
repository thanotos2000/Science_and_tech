"""将 Markdown 标准图片引用转换为 Obsidian wiki 链接格式。

示例:
  ![](images/abc.jpg)  ->  ![[abc.jpg]]
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

# 匹配 ![](images/filename.ext) 或 ![alt](images/filename.ext)
IMAGE_REF_RE = re.compile(
    r"!\[.*?\]\(\s*images/([^)\s]+)\s*\)",
    re.IGNORECASE,
)


def convert_content(text: str) -> tuple[str, int]:
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return f"![[{match.group(1)}]]"

    return IMAGE_REF_RE.sub(repl, text), count


def convert_file(path: Path, dry_run: bool = False) -> int:
    original = path.read_text(encoding="utf-8")
    updated, count = convert_content(original)
    if count and not dry_run:
        path.write_text(updated, encoding="utf-8")
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="替换 Markdown 图片引用为 Obsidian 格式")
    parser.add_argument(
        "files",
        nargs="+",
        type=Path,
        help="要处理的 Markdown 文件路径",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只统计匹配数量，不写回文件",
    )
    args = parser.parse_args()

    total = 0
    for file_path in args.files:
        if not file_path.is_file():
            raise SystemExit(f"文件不存在: {file_path}")
        count = convert_file(file_path, dry_run=args.dry_run)
        total += count
        action = "将替换" if args.dry_run else "已替换"
        print(f"{file_path}: {action} {count} 处")
    print(f"合计: {total} 处")


if __name__ == "__main__":
    main()
