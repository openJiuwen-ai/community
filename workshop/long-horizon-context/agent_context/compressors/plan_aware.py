"""策略 B：计划/里程碑感知压缩，优先保留可检验实体与未完成子目标。"""

from __future__ import annotations

import re

from ..schema import CompressedBundle, Trajectory
from ..tokenizer import Tokenizer
from .base import Compressor, assemble, excerpt_segment, step_segment, window_segment

ENTITY_PATTERNS = [
    re.compile(r"ORD-\d{4}-\d{5}"),
    re.compile(r"/data/[\w\-./]+"),
    re.compile(r"/api/v\d/[\w/{}\-]+"),
    re.compile(r"\bE\d{4}\b"),
    re.compile(r"\b(?:ods|dwd|dws|dim)_[a-z_0-9]+\b"),
    re.compile(r"\b(?:reconcile|refund|audit|stock)\.[a-z_]+=\S+"),
    re.compile(r"\d+(?:\.\d+)?%"),
    re.compile(r"\b\d+\s*(?:CNY|次|小时|天|笔|秒)\b"),
    re.compile(r"20\d{2}-\d{2}-\d{2}\s+\d{2}:\d{2}"),
]

RECENT_STEPS = 8
WINDOW_SIZE = 6
SNIPPET_CHARS = 60


def contains_entity(text: str) -> bool:
    return any(pattern.search(text) for pattern in ENTITY_PATTERNS)


def entity_excerpt(step, limit: int = 120) -> str:
    text = step.text()
    sentences = re.split(r"(?<=[。；;！？\n])", text)
    for sentence in sentences:
        if contains_entity(sentence):
            return sentence.strip()[:limit]
    return text[:limit]


class PlanAwareCompressor(Compressor):
    method = "b"

    def compress(self, trajectory: Trajectory, budget_tokens: int, tokenizer: Tokenizer) -> CompressedBundle:
        steps = trajectory.steps
        pending = {m.milestone_id for m in trajectory.milestones if m.status == "pending"}
        covered: set[int] = set()
        segments = []

        for step in steps:
            if contains_entity(step.text()):
                segments.append(
                    excerpt_segment(step, entity_excerpt(step), priority=0, kind="entity_excerpt")
                )
                covered.add(step.step_id)

        for step in steps:
            if step.step_id in covered:
                continue
            if step.milestone_id in pending and step.kind == "plan":
                segments.append(step_segment(step, priority=1, kind="pending_plan"))
                covered.add(step.step_id)

        for step in steps[-RECENT_STEPS:]:
            if step.step_id in covered:
                continue
            segments.append(step_segment(step, priority=2, kind="recent_verbatim"))
            covered.add(step.step_id)

        index = 0
        while index < len(steps):
            window = []
            while index < len(steps) and len(window) < WINDOW_SIZE:
                if steps[index].step_id not in covered:
                    window.append(steps[index])
                index += 1
            if window:
                segments.append(
                    window_segment(window, priority=3, kind="window_summary", char_limit=SNIPPET_CHARS)
                )

        return assemble(segments, budget_tokens, tokenizer, self.method, trajectory)