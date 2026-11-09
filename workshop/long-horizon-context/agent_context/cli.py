"""agent-context 命令行入口。"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from .compressors import get_compressor
from .evaluator import baseline_accuracy, evaluate, load_questions
from .generator import build_trajectory, load_dataset, write_dataset
from .metrics import markdown_table, write_report
from .tokenizer import TOKENIZER_NAME, get_tokenizer

DEFAULT_BUDGETS = "2000,4000,8000"
DEFAULT_METHODS = "a,b"


def _parse_int_list(raw: str) -> list[int]:
    return [int(item) for item in raw.split(",") if item.strip()]


def _parse_str_list(raw: str) -> list[str]:
    return [item.strip().lower() for item in raw.split(",") if item.strip()]


def cmd_generate(args: argparse.Namespace) -> int:
    trajectory = build_trajectory(steps=args.steps, seed=args.seed)
    summary = write_dataset(trajectory, Path(args.out))
    summary["tokenizer"] = TOKENIZER_NAME
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def cmd_eval(args: argparse.Namespace) -> int:
    data_dir = Path(args.data)
    trajectory = load_dataset(data_dir / "trajectory.json")
    questions = load_questions(data_dir / "questions.jsonl")
    tokenizer = get_tokenizer()

    budgets = [args.budget] if args.budget is not None else _parse_int_list(args.budgets)
    methods = [args.method.lower()] if args.method else _parse_str_list(args.methods)

    baseline = baseline_accuracy(trajectory, questions, tokenizer)
    results = []
    for method in methods:
        for budget in budgets:
            started = time.perf_counter()
            bundle = get_compressor(method).compress(trajectory, budget, tokenizer)
            elapsed = time.perf_counter() - started
            results.append(evaluate(trajectory, bundle, questions, tokenizer, baseline, elapsed))

    output_dir = Path(args.out)
    output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "tokenizer": TOKENIZER_NAME,
        "full_tokens": results[0].full_tokens if results else 0,
        "baseline_accuracy": baseline,
        "results": [item.to_dict() for item in results],
    }
    (output_dir / "results.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    report_path = write_report(results, output_dir)

    print(markdown_table(results))
    print(f"报告: {report_path}")

    if args.fail_on_threshold:
        required = [item for item in results if item.method in {"a", "b"} and item.method == "b"]
        if any(not item.passed for item in required):
            return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agent-context", description="长程上下文压缩与可验证评测")
    sub = parser.add_subparsers(dest="command", required=True)

    generate = sub.add_parser("generate", help="生成确定性的长程轨迹与问答题")
    generate.add_argument("--out", default="data", help="输出目录")
    generate.add_argument("--steps", type=int, default=280, help="轨迹步数，至少 200")
    generate.add_argument("--seed", type=int, default=2026, help="随机种子")
    generate.set_defaults(func=cmd_generate)

    evaluate = sub.add_parser("eval", help="运行压缩与可验证评测")
    evaluate.add_argument("--data", default="data", help="数据目录")
    evaluate.add_argument("--out", default="reports", help="报告输出目录")
    evaluate.add_argument("--budget", type=int, default=None, help="单个 token 预算")
    evaluate.add_argument("--method", default=None, help="单个压缩方法：a 或 b")
    evaluate.add_argument("--budgets", default=DEFAULT_BUDGETS, help="逗号分隔的多档预算")
    evaluate.add_argument("--methods", default=DEFAULT_METHODS, help="逗号分隔的多个方法")
    evaluate.add_argument("--fail-on-threshold", action="store_true", help="方法 B 未达门槛时非零退出")
    evaluate.set_defaults(func=cmd_eval)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())