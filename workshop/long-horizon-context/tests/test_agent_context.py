"""长程上下文压缩的回归测试。"""

from __future__ import annotations

import hashlib

import pytest

from agent_context.cli import main
from agent_context.compressors import get_compressor
from agent_context.generator import build_trajectory
from agent_context.tokenizer import get_tokenizer


def _questions(trajectory):
    return [fact for fact in trajectory.facts if fact.question]


def _accuracy(text: str, questions) -> float:
    hits = sum(1 for fact in questions if fact.answer in text)
    return hits / max(len(questions), 1)


def test_generator_meets_long_horizon_requirements() -> None:
    trajectory = build_trajectory()
    tokenizer = get_tokenizer()

    assert len(trajectory.steps) >= 200
    assert tokenizer.count(trajectory.full_text()) >= 50_000
    assert len(_questions(trajectory)) >= 20


@pytest.mark.parametrize("budget", [2000, 4000, 8000])
def test_plan_aware_respects_budget_and_keeps_answers(budget: int) -> None:
    trajectory = build_trajectory()
    tokenizer = get_tokenizer()
    questions = _questions(trajectory)

    bundle = get_compressor("b").compress(trajectory, budget, tokenizer)

    assert bundle.token_count <= budget
    assert _accuracy(bundle.summary_text, questions) == 1.0
    assert 1 - bundle.token_count / tokenizer.count(trajectory.full_text()) >= 0.4


def test_retained_spans_are_auditable() -> None:
    trajectory = build_trajectory()
    tokenizer = get_tokenizer()
    bundle = get_compressor("b").compress(trajectory, 4000, tokenizer)

    assert bundle.retained_spans
    for span in bundle.retained_spans:
        if span.start_step != span.end_step:
            continue
        step = trajectory.step_by_id(span.start_step)
        assert step is not None
        expected = hashlib.sha256(step.text().encode("utf-8")).hexdigest()[:8]
        assert span.sha256 == expected


def test_generic_summary_loses_more_entities_than_plan_aware() -> None:
    trajectory = build_trajectory()
    tokenizer = get_tokenizer()
    questions = _questions(trajectory)

    generic = get_compressor("a").compress(trajectory, 2000, tokenizer)
    planned = get_compressor("b").compress(trajectory, 2000, tokenizer)

    assert _accuracy(generic.summary_text, questions) < _accuracy(planned.summary_text, questions)


def test_cli_generate_and_eval(tmp_path) -> None:
    data_dir = tmp_path / "data"
    report_dir = tmp_path / "reports"

    assert main(["generate", "--out", str(data_dir)]) == 0
    assert (data_dir / "trajectory.json").is_file()
    assert (data_dir / "questions.jsonl").is_file()

    assert (
        main(
            [
                "eval",
                "--data",
                str(data_dir),
                "--out",
                str(report_dir),
                "--budgets",
                "2000",
                "--methods",
                "b",
                "--fail-on-threshold",
            ]
        )
        == 0
    )
    assert (report_dir / "comparison.md").is_file()
    assert (report_dir / "budget_quality.svg").is_file()
    assert (report_dir / "results.json").is_file()