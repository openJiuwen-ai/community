"""压缩器公共片段模型与预算装配逻辑。"""

from __future__ import annotations

import hashlib
from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass, replace

from ..schema import CompressedBundle, RetainedSpan, Step, Trajectory
from ..tokenizer import Tokenizer


@dataclass
class Segment:
    text: str
    start_step: int
    end_step: int
    kind: str
    priority: int
    digest: str
    tokens: int = 0


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]


def step_segment(step: Step, priority: int, kind: str) -> Segment:
    text = step.text()
    return Segment(text, step.step_id, step.step_id, kind, priority, digest(text))


def excerpt_segment(step: Step, excerpt: str, priority: int, kind: str) -> Segment:
    return Segment(excerpt, step.step_id, step.step_id, kind, priority, digest(step.text()))


def window_segment(steps: list[Step], priority: int, kind: str, char_limit: int = 80) -> Segment:
    sid = steps[0].step_id
    eid = steps[-1].step_id
    parts = [f"[steps {sid}-{eid} summary]"]
    for step in steps:
        snippet = (step.content or step.tool_result or "").replace("\n", " ")[:char_limit]
        parts.append(f"{step.step_id}:{step.role}/{step.kind}:{snippet}")
    text = " ".join(parts)
    return Segment(text, sid, eid, kind, priority, digest("\n".join(s.text() for s in steps)))


def assemble(
    segments: list[Segment],
    budget_tokens: int,
    tokenizer: Tokenizer,
    method: str,
    trajectory: Trajectory,
) -> CompressedBundle:
    header = f"[compressed context] method={method} task={trajectory.task_id}"
    header_tokens = tokenizer.count(header)
    if budget_tokens <= header_tokens:
        summary = tokenizer.truncate(header, budget_tokens)
        return CompressedBundle(
            summary_text=summary,
            retained_spans=[],
            dropped_stats={"budget_too_small": True},
            token_count=tokenizer.count(summary),
            budget_tokens=budget_tokens,
            method=method,
        )

    selected: list[Segment] = []
    dropped: list[Segment] = []
    used = header_tokens

    for segment in sorted(segments, key=lambda item: (item.priority, item.start_step)):
        segment.tokens = tokenizer.count(segment.text)
        remaining = budget_tokens - used - 1
        if remaining <= 0:
            dropped.append(segment)
            continue
        if segment.tokens <= remaining:
            selected.append(segment)
            used += segment.tokens + 1
        else:
            truncated = tokenizer.truncate(segment.text, remaining)
            if truncated:
                selected.append(
                    replace(
                        segment,
                        text=truncated,
                        tokens=tokenizer.count(truncated),
                        kind=f"{segment.kind}_truncated",
                    )
                )
                used += tokenizer.count(truncated) + 1
            else:
                dropped.append(segment)

    selected.sort(key=lambda item: item.start_step)
    summary = header + "\n" + "\n".join(segment.text for segment in selected)
    summary = tokenizer.truncate(summary, budget_tokens)

    spans = [
        RetainedSpan(
            span_id=f"S{index:03d}",
            start_step=segment.start_step,
            end_step=segment.end_step,
            sha256=segment.digest,
            tokens=tokenizer.count(segment.text),
            kind=segment.kind,
        )
        for index, segment in enumerate(selected, start=1)
    ]

    dropped_steps: dict[str, int] = defaultdict(int)
    dropped_chars: dict[str, int] = defaultdict(int)
    for segment in dropped:
        dropped_steps[segment.kind] += segment.end_step - segment.start_step + 1
        dropped_chars[segment.kind] += len(segment.text)

    retained_steps = sum(span.end_step - span.start_step + 1 for span in spans)
    dropped_stats = {
        "total_steps": len(trajectory.steps),
        "retained_steps": retained_steps,
        "dropped_steps_by_kind": dict(dropped_steps),
        "dropped_chars_by_kind": dict(dropped_chars),
    }

    return CompressedBundle(
        summary_text=summary,
        retained_spans=spans,
        dropped_stats=dropped_stats,
        token_count=tokenizer.count(summary),
        budget_tokens=budget_tokens,
        method=method,
    )


class Compressor(ABC):
    method: str = ""

    @abstractmethod
    def compress(self, trajectory: Trajectory, budget_tokens: int, tokenizer: Tokenizer) -> CompressedBundle:
        raise NotImplementedError