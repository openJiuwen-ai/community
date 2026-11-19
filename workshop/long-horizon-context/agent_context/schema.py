"""轨迹、事实与压缩结果的数据契约。"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class Step:
    step_id: int
    role: str
    content: str
    tool_name: str | None = None
    tool_result: str | None = None
    kind: str = "observation"
    milestone_id: str | None = None
    milestone_status: str | None = None

    def text(self) -> str:
        parts = [f"[step {self.step_id}] {self.role}"]
        if self.tool_name:
            parts.append(f"tool={self.tool_name}")
        if self.kind:
            parts.append(f"kind={self.kind}")
        if self.milestone_id:
            parts.append(f"milestone={self.milestone_id}:{self.milestone_status}")
        parts.append(self.content)
        if self.tool_result:
            parts.append(f"result: {self.tool_result}")
        return "\n".join(parts)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Step":
        return cls(**data)


@dataclass
class Fact:
    fact_id: str
    fact_type: str
    value: str
    step_id: int
    question: str | None = None
    answer: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Fact":
        return cls(**data)


@dataclass
class Milestone:
    milestone_id: str
    title: str
    status: str
    start_step: int
    end_step: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Milestone":
        return cls(**data)


@dataclass
class RetainedSpan:
    span_id: str
    start_step: int
    end_step: int
    sha256: str
    tokens: int
    kind: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class CompressedBundle:
    summary_text: str
    retained_spans: list[RetainedSpan]
    dropped_stats: dict[str, Any] = field(default_factory=dict)
    token_count: int = 0
    budget_tokens: int = 0
    method: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "summary_text": self.summary_text,
            "retained_spans": [s.to_dict() for s in self.retained_spans],
            "dropped_stats": self.dropped_stats,
            "token_count": self.token_count,
            "budget_tokens": self.budget_tokens,
            "method": self.method,
        }


@dataclass
class Trajectory:
    task_id: str
    steps: list[Step]
    facts: list[Fact]
    milestones: list[Milestone]

    def full_text(self) -> str:
        return "\n".join(step.text() for step in self.steps)

    def step_by_id(self, step_id: int) -> Step | None:
        for step in self.steps:
            if step.step_id == step_id:
                return step
        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "steps": [s.to_dict() for s in self.steps],
            "facts": [f.to_dict() for f in self.facts],
            "milestones": [m.to_dict() for m in self.milestones],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Trajectory":
        return cls(
            task_id=data["task_id"],
            steps=[Step.from_dict(s) for s in data["steps"]],
            facts=[Fact.from_dict(f) for f in data["facts"]],
            milestones=[Milestone.from_dict(m) for m in data["milestones"]],
        )