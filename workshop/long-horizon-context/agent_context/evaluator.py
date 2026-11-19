"""规则基线评测器：只检查压缩结果是否仍包含可检验事实。"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from .schema import CompressedBundle, Trajectory
from .tokenizer import Tokenizer


@dataclass
class QuestionResult:
    fact_id: str
    fact_type: str
    question: str
    expected: str
    hit: bool


@dataclass
class EvalResult:
    method: str
    budget: int
    token_count: int
    full_tokens: int
    reduction: float
    accuracy: float
    baseline_accuracy: float
    accuracy_drop: float
    passed: bool
    retained_spans: int
    dropped_stats: dict
    elapsed_seconds: float
    results: list[QuestionResult]

    def to_dict(self) -> dict:
        data = asdict(self)
        return data


def load_questions(path: Path) -> list[dict]:
    questions = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                questions.append(json.loads(line))
    return questions


def answer_questions(text: str, questions: list[dict]) -> list[QuestionResult]:
    results = []
    for item in questions:
        expected = item["answer"]
        results.append(
            QuestionResult(
                fact_id=item["fact_id"],
                fact_type=item["fact_type"],
                question=item["question"],
                expected=expected,
                hit=bool(expected) and expected in text,
            )
        )
    return results


def baseline_accuracy(trajectory: Trajectory, questions: list[dict], tokenizer: Tokenizer) -> float:
    results = answer_questions(trajectory.full_text(), questions)
    return sum(1 for item in results if item.hit) / max(len(results), 1)


def evaluate(
    trajectory: Trajectory,
    bundle: CompressedBundle,
    questions: list[dict],
    tokenizer: Tokenizer,
    baseline: float,
    elapsed_seconds: float,
) -> EvalResult:
    results = answer_questions(bundle.summary_text, questions)
    accuracy = sum(1 for item in results if item.hit) / max(len(results), 1)
    full_tokens = tokenizer.count(trajectory.full_text())
    reduction = 1 - bundle.token_count / max(full_tokens, 1)
    accuracy_drop = baseline - accuracy
    return EvalResult(
        method=bundle.method,
        budget=bundle.budget_tokens,
        token_count=bundle.token_count,
        full_tokens=full_tokens,
        reduction=reduction,
        accuracy=accuracy,
        baseline_accuracy=baseline,
        accuracy_drop=accuracy_drop,
        passed=(reduction >= 0.4 and accuracy_drop <= 0.08 and bundle.token_count <= bundle.budget_tokens),
        retained_spans=len(bundle.retained_spans),
        dropped_stats=bundle.dropped_stats,
        elapsed_seconds=elapsed_seconds,
        results=results,
    )