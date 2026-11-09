"""首次准备时拉取 cl100k_base 编码文件到 data/tokenizer（需要联网）。"""

from __future__ import annotations

import os
from pathlib import Path

CACHE_DIR = Path(__file__).resolve().parent.parent / "data" / "tokenizer"


def main() -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    os.environ["TIKTOKEN_CACHE_DIR"] = str(CACHE_DIR)

    import tiktoken

    encoding = tiktoken.get_encoding("cl100k_base")
    print(f"tokenizer ready: {CACHE_DIR}")
    print(f"sample tokens: {len(encoding.encode('hello world'))}")


if __name__ == "__main__":
    main()