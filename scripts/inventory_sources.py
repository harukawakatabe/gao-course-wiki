from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


RAW_ROOT = Path(r"D:\Space\notes\HomeSpace\Finance\Gao\Business Logic\LectureText")


@dataclass(frozen=True)
class SourceFile:
    course: str
    lecture_id: str
    title: str
    path: Path
    size: int


def parse_file(path: Path) -> SourceFile | None:
    if path.suffix.lower() != ".txt":
        return None
    match = re.match(r"^(\d{3})、(.+)\.txt$", path.name)
    if not match:
        return None
    lecture_id, title = match.groups()
    return SourceFile(
        course="business-logic",
        lecture_id=lecture_id,
        title=title,
        path=path,
        size=path.stat().st_size,
    )


def collect_sources(root: Path) -> list[SourceFile]:
    sources: list[SourceFile] = []
    for path in sorted(root.glob("*.txt")):
        source = parse_file(path)
        if source is not None:
            sources.append(source)
    return sources


def render_index(sources: list[SourceFile]) -> str:
    lines = [
        "# 来源路径盘点",
        "",
        "由 `scripts/inventory_sources.py` 自动生成，勿手动修改。",
        "",
        "## Business Logic",
        "",
        "| 讲次 | 标题 | 字节数 | 路径 |",
        "|---|---|---:|---|",
    ]
    for source in sources:
        lines.append(
            f"| {source.lecture_id} | {source.title} | {source.size} | `{source.path}` |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    sources = collect_sources(RAW_ROOT)
    output = Path("sources/raw-paths.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_index(sources), encoding="utf-8")
    print(f"indexed={len(sources)} output={output}")


if __name__ == "__main__":
    main()
