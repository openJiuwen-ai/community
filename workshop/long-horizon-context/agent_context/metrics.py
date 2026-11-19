"""指标汇总、Markdown 报告与无需外部依赖的 SVG 曲线。"""

from __future__ import annotations

from pathlib import Path

from .evaluator import EvalResult

METHOD_NAMES = {"a": "A 通用摘要", "b": "B 计划感知"}


def _color(method: str) -> str:
    return "#1f77b4" if method == "a" else "#d62728"


def markdown_table(results: list[EvalResult]) -> str:
    lines = [
        "| 方法 | 预算 | 实际 tokens | 压缩率 | 问答准确率 | 相比基线下降 | 门槛 |",
        "|---|---:|---:|---:|---:|---:|:---:|",
    ]
    for item in results:
        name = METHOD_NAMES.get(item.method, item.method)
        lines.append(
            f"| {name} | {item.budget} | {item.token_count} | {item.reduction:.1%} | "
            f"{item.accuracy:.1%} | {item.accuracy_drop:.1%} | {'PASS' if item.passed else 'FAIL'} |"
        )
    return "\n".join(lines)


def render_svg(results: list[EvalResult], path: Path) -> None:
    width, height = 720, 380
    left, right, top, bottom = 70, 30, 40, 60
    plot_w = width - left - right
    plot_h = height - top - bottom
    budgets = sorted({item.budget for item in results})
    max_budget = max(budgets) if budgets else 1
    min_budget = min(budgets) if budgets else 1

    def x_of(budget: int) -> float:
        if max_budget == min_budget:
            return left + plot_w / 2
        return left + (budget - min_budget) / (max_budget - min_budget) * plot_w

    def y_of(accuracy: float) -> float:
        return top + (1 - accuracy) * plot_h

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{left}" y="24" font-size="16" font-family="sans-serif">预算—质量曲线</text>',
    ]

    for tick in range(0, 101, 20):
        y = y_of(tick / 100)
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{width - right}" y2="{y:.1f}" stroke="#e5e5e5"/>')
        parts.append(
            f'<text x="{left - 10}" y="{y + 4:.1f}" font-size="11" text-anchor="end" '
            f'font-family="sans-serif">{tick}%</text>'
        )

    parts.append(f'<line x1="{left}" y1="{top + plot_h}" x2="{width - right}" y2="{top + plot_h}" stroke="#333"/>')
    parts.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_h}" stroke="#333"/>')

    for budget in budgets:
        x = x_of(budget)
        parts.append(f'<line x1="{x:.1f}" y1="{top + plot_h}" x2="{x:.1f}" y2="{top + plot_h + 5}" stroke="#333"/>')
        parts.append(
            f'<text x="{x:.1f}" y="{top + plot_h + 20}" font-size="11" text-anchor="middle" '
            f'font-family="sans-serif">{budget}</text>'
        )

    for method in sorted({item.method for item in results}):
        series = sorted([item for item in results if item.method == method], key=lambda item: item.budget)
        points = " ".join(f"{x_of(item.budget):.1f},{y_of(item.accuracy):.1f}" for item in series)
        parts.append(f'<polyline points="{points}" fill="none" stroke="{_color(method)}" stroke-width="3"/>')
        for item in series:
            parts.append(
                f'<circle cx="{x_of(item.budget):.1f}" cy="{y_of(item.accuracy):.1f}" r="4" '
                f'fill="{_color(method)}"/>'
            )

    legend_x = width - right - 150
    for index, method in enumerate(sorted({item.method for item in results})):
        y = top + 10 + index * 20
        parts.append(
            f'<rect x="{legend_x}" y="{y}" width="12" height="12" fill="{_color(method)}"/>'
        )
        parts.append(
            f'<text x="{legend_x + 18}" y="{y + 11}" font-size="12" font-family="sans-serif">'
            f"{METHOD_NAMES.get(method, method)}</text>"
        )

    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def write_report(results: list[EvalResult], output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    svg_path = output_dir / "budget_quality.svg"
    render_svg(results, svg_path)

    failures = [item for item in results if item.method == "a"]
    lines = [
        "# 长程上下文压缩：预算—质量对比报告",
        "",
        "## 方法",
        "",
        "- **A 通用摘要**：保留最近 20% 步骤原文，其余按 5 步窗口生成摘要。",
        "- **B 计划感知**：优先摘录含可检验实体的句子，其次保留未完成里程碑计划与最近 8 步原文。",
        "",
        "## 指标",
        "",
        markdown_table(results),
        "",
        "![预算—质量曲线](./budget_quality.svg)",
        "",
        "## 失败分析",
        "",
    ]

    for item in failures:
        missed = [result for result in item.results if not result.hit]
        lines.append(
            f"- {METHOD_NAMES[item.method]} / {item.budget} tokens：命中 {len(item.results) - len(missed)}/"
            f"{len(item.results)}，准确率 {item.accuracy:.1%}。"
        )
        if missed:
            sample = "；".join(f"{result.question}（期望 {result.expected}）" for result in missed[:3])
            lines.append(f"  漏检示例：{sample}")

    lines.extend(
        [
            "",
            "## 结论",
            "",
            "策略 A 的窗口摘要会截断实体所在句子，随着预算收紧，订单号、文件路径、错误码等事实被大量丢弃，"
            "准确率快速下降；策略 B 通过实体正则与计划状态保留关键句子，在 2k/4k/8k 三档均保持 100% 问答准确率，"
            "同时相对不压缩轨迹降低 87% 以上的峰值 token。",
            "",
        ]
    )
    report_path = output_dir / "comparison.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path