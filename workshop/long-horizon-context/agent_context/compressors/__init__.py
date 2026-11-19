"""压缩策略实现。"""

from .base import Compressor
from .generic import GenericSummaryCompressor
from .plan_aware import PlanAwareCompressor

COMPRESSORS: dict[str, type[Compressor]] = {
    "a": GenericSummaryCompressor,
    "b": PlanAwareCompressor,
}


def get_compressor(method: str) -> Compressor:
    key = method.lower()
    if key not in COMPRESSORS:
        raise ValueError(f"未知压缩方法: {method!r}（可选: a, b）")
    return COMPRESSORS[key]()