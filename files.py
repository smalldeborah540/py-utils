"""Path helpers."""
from pathlib import Path


def ensure_dir(path):
    """Create the directory if missing and return it as a Path."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def move_into(src, dst_dir):
    """Move a file into a directory, creating it if needed."""
    src = Path(src)
    dst_dir = ensure_dir(dst_dir)
    return src.rename(dst_dir / src.name)


def read_lines(path, encoding="utf-8"):
    """Read a file into stripped, non-empty lines."""
    with open(path, encoding=encoding) as fh:
        return [ln.strip() for ln in fh if ln.strip()]
