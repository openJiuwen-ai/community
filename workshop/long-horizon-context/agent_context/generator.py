"""确定性地合成一条长程运维轨迹，并注入可检验事实。"""

from __future__ import annotations

import json
import random
from pathlib import Path

from .schema import Fact, Milestone, Step, Trajectory
from .tokenizer import get_tokenizer

MILESTONES = [
    ("M1", "收集订单文件"),
    ("M2", "校验订单格式"),
    ("M3", "执行对账"),
    ("M4", "差异分类"),
    ("M5", "退款修复"),
    ("M6", "库存回滚"),
    ("M7", "生成审计报告"),
    ("M8", "归档与收尾"),
]

TOOLS = ["list_dir", "read_file", "query_db", "run_sql", "call_api", "write_file", "check_metric"]

NOISE_BANK = [
    "继续按计划推进当前里程碑，先确认上一步的工具输出是否完整，再决定下一次调用的参数。",
    "对当前批次中的异常订单逐条检查，记录处理原因、操作人和时间戳，避免后续审计时缺少依据。",
    "读取配置中心的最新参数，确认批处理大小、重试策略与告警阈值没有被其他任务覆盖。",
    "复核工具返回的字段映射，确保订单号、批次号与文件路径在上下游之间保持一致。",
    "将中间结果写入临时目录，并在写入后重新读取一次，校验内容长度与哈希是否匹配。",
    "检查数据库连接池状态，确认没有长期占用的事务，必要时重新建立连接后继续执行。",
    "对失败条目执行有限次重试，超过上限后转入人工队列，避免无限循环消耗执行预算。",
    "汇总当前阶段的统计指标，包括处理条数、成功条数、失败条数、平均耗时与差异率。",
    "核对审计要求：每个危险操作都要有审批记录，每次外部调用都要有 trace id 与耗时。",
    "更新计划看板中的子任务状态，把已完成的里程碑标记为 done，未完成的保持 pending。",
]


def _noise(rng: random.Random, step_id: int, milestone: Milestone) -> str:
    parts = [rng.choice(NOISE_BANK) for _ in range(rng.randint(2, 3))]
    parts.append(
        f"当前步骤编号 {step_id}，所属里程碑 {milestone.milestone_id}（{milestone.title}），"
        f"状态 {milestone.status}，工具队列剩余任务 {rng.randint(1, 9)} 个。"
    )
    parts.append(
        "执行备注：若输入文件缺少表头则先补齐字段，若返回码非零则记录错误码与原始响应，"
        "并在下一步前完成状态同步。"
    )
    return " ".join(parts)


def _build_facts() -> list[Fact]:
    specs: list[tuple[str, str, str | None, str | None]] = []

    for index in range(8):
        number = 100 + index
        order_id = f"ORD-2026-{number:05d}"
        path = f"/data/orders/2026/batch-{index + 1}/order_{number:05d}.csv"
        specs.append(
            (
                "order_file",
                f"{order_id} 的原始文件路径为 {path}",
                f"订单 {order_id} 的原始文件路径是什么？",
                path,
            )
        )

    constraints = [
        ("单笔退款金额上限为 1200 CNY", "单笔退款金额上限是多少？", "1200 CNY"),
        ("对账任务截止时间为 2026-12-31 18:00", "对账任务的截止时间是什么？", "2026-12-31 18:00"),
        ("失败重试次数上限为 3 次", "失败重试次数上限是多少？", "3 次"),
        ("差异率告警阈值为 0.5%", "差异率告警阈值是多少？", "0.5%"),
        ("单批处理订单数量上限为 500 笔", "单批处理订单数量上限是多少？", "500 笔"),
        ("退款审批金额上限为 8000 CNY", "退款审批金额上限是多少？", "8000 CNY"),
        ("库存回滚窗口为 24 小时", "库存回滚窗口是多少小时？", "24 小时"),
        ("审计日志保留期限为 180 天", "审计日志保留期限是多少天？", "180 天"),
    ]
    for value, question, answer in constraints:
        specs.append(("constraint", value, question, answer))

    errors = [
        ("错误码 E4031 表示订单状态不一致", "错误码 E4031 表示什么问题？", "订单状态不一致"),
        ("错误码 E5022 表示库存锁定失败", "错误码 E5022 表示什么问题？", "库存锁定失败"),
        ("错误码 E4001 表示文件校验失败", "错误码 E4001 表示什么问题？", "文件校验失败"),
        ("错误码 E4090 表示重复退款", "错误码 E4090 表示什么问题？", "重复退款"),
        ("错误码 E5012 表示对账超时", "错误码 E5012 表示什么问题？", "对账超时"),
        ("错误码 E4033 表示权限不足", "错误码 E4033 表示什么问题？", "权限不足"),
    ]
    for value, question, answer in errors:
        specs.append(("error_code", value, question, answer))

    endpoints = [
        ("对账接口路径为 /api/v2/orders/reconcile", "对账接口的路径是什么？", "/api/v2/orders/reconcile"),
        ("退款接口路径为 /api/v2/orders/refund", "退款接口的路径是什么？", "/api/v2/orders/refund"),
        ("库存接口路径为 /api/v2/stock/rollback", "库存回滚接口的路径是什么？", "/api/v2/stock/rollback"),
        ("审计接口路径为 /api/v2/audit/report", "审计报告接口的路径是什么？", "/api/v2/audit/report"),
        ("归档接口路径为 /api/v2/archive/batch", "归档接口的路径是什么？", "/api/v2/archive/batch"),
    ]
    for value, question, answer in endpoints:
        specs.append(("endpoint", value, question, answer))

    storages = [
        ("对账明细表名为 ods_order_detail_2026", "对账明细表名是什么？", "ods_order_detail_2026"),
        ("退款流水表名为 dwd_refund_ledger", "退款流水表名是什么？", "dwd_refund_ledger"),
        ("差异汇总表名为 dws_reconcile_diff", "差异汇总表名是什么？", "dws_reconcile_diff"),
        ("订单状态维表名为 dim_order_status", "订单状态维表名是什么？", "dim_order_status"),
        ("批处理参数为 reconcile.batch_size=64", "批处理参数 reconcile.batch_size 的值是多少？", "reconcile.batch_size=64"),
    ]
    for value, question, answer in storages:
        specs.append(("storage", value, question, answer))

    metrics = [
        ("本次对账差异率为 0.37%", "本次对账差异率是多少？", "0.37%"),
        ("退款成功率为 99.62%", "退款成功率是多少？", "99.62%"),
        ("平均对账耗时为 42 秒", "平均对账耗时是多少秒？", "42 秒"),
        ("库存回滚延迟为 3.5 小时", "库存回滚延迟是多少小时？", "3.5 小时"),
        ("审计覆盖率为 100%", "审计覆盖率是多少？", "100%"),
        ("异常订单占比为 1.8%", "异常订单占比是多少？", "1.8%"),
    ]
    for value, question, answer in metrics:
        specs.append(("metric", value, question, answer))

    facts: list[Fact] = []
    for index, (fact_type, value, question, answer) in enumerate(specs):
        facts.append(
            Fact(
                fact_id=f"F{index + 1:03d}",
                fact_type=fact_type,
                value=value,
                step_id=5 + index * 6,
                question=question,
                answer=answer,
            )
        )
    return facts


def build_trajectory(steps: int = 280, seed: int = 2026) -> Trajectory:
    if steps < 200:
        raise ValueError("steps 必须 >= 200，以覆盖长程压力要求")

    facts = _build_facts()
    if facts[-1].step_id >= steps:
        raise ValueError("轨迹步数不足以容纳全部事实")

    per_milestone = steps // len(MILESTONES)
    milestones = [
        Milestone(
            milestone_id=mid,
            title=title,
            status="done" if index < len(MILESTONES) - 2 else "pending",
            start_step=index * per_milestone,
            end_step=(index + 1) * per_milestone - 1,
        )
        for index, (mid, title) in enumerate(MILESTONES)
    ]

    facts_by_step: dict[int, list[Fact]] = {}
    for fact in facts:
        facts_by_step.setdefault(fact.step_id, []).append(fact)

    rng = random.Random(seed)
    trajectory_steps: list[Step] = []
    for step_id in range(steps):
        milestone = milestones[min(step_id // per_milestone, len(milestones) - 1)]
        kind_cycle = step_id % 4
        if kind_cycle == 0:
            role, kind, tool_name = "assistant", "plan", None
        elif kind_cycle == 1:
            role, kind, tool_name = "assistant", "tool_call", TOOLS[step_id % len(TOOLS)]
        elif kind_cycle == 2:
            role, kind, tool_name = "tool", "observation", TOOLS[step_id % len(TOOLS)]
        else:
            role, kind, tool_name = "assistant", "reflection", None

        content = _noise(rng, step_id, milestone)
        tool_result = None
        if kind == "observation":
            tool_result = (
                f"返回 {rng.randint(1, 240)} 行；状态码 200；trace_id=tr-{step_id:04d}-{rng.randint(1000, 9999)}；"
                f"耗时 {rng.randint(20, 900)} ms。"
            )

        for fact in facts_by_step.get(step_id, []):
            content = f"{content} 检查记录：{fact.value}。"

        trajectory_steps.append(
            Step(
                step_id=step_id,
                role=role,
                content=content,
                tool_name=tool_name,
                tool_result=tool_result,
                kind=kind,
                milestone_id=milestone.milestone_id,
                milestone_status=milestone.status,
            )
        )

    return Trajectory(task_id="long-horizon-reconcile-2026", steps=trajectory_steps, facts=facts, milestones=milestones)


def write_dataset(trajectory: Trajectory, output_dir: Path) -> dict[str, int]:
    output_dir.mkdir(parents=True, exist_ok=True)
    trajectory_path = output_dir / "trajectory.json"
    trajectory_path.write_text(
        json.dumps(trajectory.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )

    questions = [fact for fact in trajectory.facts if fact.question]
    questions_path = output_dir / "questions.jsonl"
    with questions_path.open("w", encoding="utf-8") as handle:
        for fact in questions:
            handle.write(
                json.dumps(
                    {
                        "fact_id": fact.fact_id,
                        "fact_type": fact.fact_type,
                        "question": fact.question,
                        "answer": fact.answer,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    tokenizer = get_tokenizer()
    return {
        "steps": len(trajectory.steps),
        "facts": len(trajectory.facts),
        "questions": len(questions),
        "full_tokens": tokenizer.count(trajectory.full_text()),
    }


def load_dataset(path: Path) -> Trajectory:
    return Trajectory.from_dict(json.loads(path.read_text(encoding="utf-8")))