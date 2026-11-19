"""固定 tokenizer：cl100k_base，优先使用仓库内置的离线编码文件。"""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

TOKENIZER_NAME = "cl100k_base"
_CACHE_DIR = Path(__file__).resolve().parent.parent / "data" / "tokenizer"


def configure_cache_dir() -> Path:
    if _CACHE_DIR.is_dir():
        os.environ.setdefault("TIKTOKEN_CACHE_DIR", str(_CACHE_DIR))
    return _CACHE_DIR


class Tokenizer:
    def __init__(self) -> None:
        configure_cache_dir()
        import tiktoken

        self._encoding = tiktoken.get_encoding(TOKENIZER_NAME)

    def count(self, text: str) -> int:
        if not text:
            return 0
        return len(self._encoding.encode(text, disallowed_special=()))

    def encode(self, text: str) -> list[int]:
        return self._encoding.encode(text, disallowed_special=())

    def decode(self, tokens: list[int]) -> str:
        return self._encoding.decode(tokens)

    def truncate(self, text: str, max_tokens: int) -> str:
        if max_tokens <= 0:
            return ""
        tokens = self.encode(text)
        if len(tokens) <= max_tokens:
            return text
        return self.decode(tokens[:max_tokens])


@lru_cache(maxsize=1)
def get_tokenizer() -> Tokenizer:
    return Tokenizer()