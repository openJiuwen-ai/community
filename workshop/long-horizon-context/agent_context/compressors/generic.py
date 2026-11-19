"""策略 A：通用摘要型压缩。"""

from __future__ import annotations

from ..schema import CompressedBundle, Trajectory
from ..tokenizer import Tokenizer
from .base import Compressor, assemble, step_segment, window_segment

RECENT_RATIO = 0.2
WINDOW_SIZE = 5
SNIPPET_CHARS = 80


class GenericSummaryCompressor(Compressor):
    method = "a"

    def compress(self, trajectory: Trajectory, budget_tokens: int, tokenizer: Tokenizer) -> CompressedBundle:
        steps = trajectory.steps
        recent_start = int(len(steps) * (1 - RECENT_RATIO))
        segments = []

        for step in steps[recent_start:]:
            segments.append(step_segment(step, priority=0, kind="recent_verbatim"))

        for index in range(0, recent_start, WINDOW_SIZE):
            window = steps[index : index + WINDOW_SIZE]
            if window:
                segments.append(
                    window_segment(window, priority=1, kind="window_summary", char_limit=SNIPPET_CHARS)
                )

        return assemble(segments, budget_tokens, tokenizer, self.method, trajectory)