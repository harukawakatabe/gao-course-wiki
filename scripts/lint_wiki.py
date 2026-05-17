from __future__ import annotations

from pathlib import Path


ROOT = Path(".")
MARKDOWN_DIRS = ["sources", "courses", "wiki", "applications", "schema"]


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for dirname in MARKDOWN_DIRS:
        root = ROOT / dirname
        if root.exists():
            files.extend(sorted(root.rglob("*.md")))
    if (ROOT / "README.md").exists():
        files.append(ROOT / "README.md")
    if (ROOT / "AGENTS.md").exists():
        files.append(ROOT / "AGENTS.md")
    if (ROOT / "log.md").exists():
        files.append(ROOT / "log.md")
    return files


def contains_emoji(text: str) -> bool:
    for char in text:
        codepoint = ord(char)
        if 0x1F300 <= codepoint <= 0x1FAFF:
            return True
    return False


def main() -> None:
    errors: list[str] = []
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        if contains_emoji(text):
            errors.append(f"{path}: contains emoji")
        # 来源卡片必须有 source_path
        posix = path.as_posix()
        if "sources/cards/" in posix and "source_path:" not in text:
            errors.append(f"{path}: source card missing source_path")
        # wiki 非索引页必须有来源证据
        if "wiki/" in posix and path.name != "index.md":
            if "source_scope:" not in text and "## 来源和证据" not in text:
                errors.append(f"{path}: wiki page missing source evidence")

    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)

    print("lint passed")


if __name__ == "__main__":
    main()
