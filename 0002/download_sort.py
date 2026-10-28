"""sort_downloads.py — moves files in a folder into subfolders by extension."""

import shutil
import sys
from pathlib import Path

CATEGORIES = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "documents": {".pdf", ".docx", ".txt", ".md"},
    "audio": {".mp3", ".wav", ".flac"},
    "video": {".mp4", ".mov", ".mkv"},
    "archives": {".zip", ".tar", ".gz", ".7z"},
}


def category_for(suffix):
    for name, extensions in CATEGORIES.items():
        if suffix.lower() in extensions:
            return name
    return "other"


def organize(folder):
    folder = Path(folder)
    if not folder.is_dir():
        print(f"Not a folder: {folder}")
        return

    moved = 0
    for item in folder.iterdir():
        if not item.is_file():
            continue

        category = category_for(item.suffix)
        dest_dir = folder / category
        dest_dir.mkdir(exist_ok=True)

        dest = dest_dir / item.name
        if dest.exists():
            print(f"skip (already exists): {item.name}")
            continue

        shutil.move(str(item), str(dest))
        print(f"{item.name} -> {category}/")
        moved += 1

    print(f"\nDone. {moved} file(s) moved.")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    organize(target)
