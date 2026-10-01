# SIG

SIG（Special Interest Group，特别兴趣小组）是 openJiuwen 社区的技术组织单元。SIG 在技术委员会（TC）指导下，负责项目群社区特定子领域及创新项目的架构设计、开源开发及社区运营等工作。

本目录集中管理各 SIG 的组织信息：每个 SIG 对应一个子目录，目录内的 `sig-info.yaml` 登记了该 SIG 的名称、描述、成熟度等级、Maintainer、Committer 以及负责的代码仓库等元数据。

> SIG 的成立、成员职责、竞选流程、例会组织等完整治理规则，请参阅[社区章程 - SIG 章节](../coreteam/openJiuwen社区章程.md#sig)。

## SIG 总览

下表汇总了当前社区的全部 SIG，点击 SIG 名称可查看其详细的 `sig-info.yaml`。

| SIG | 描述 | 成熟度 | Maintainer | 负责仓库 |
| --- | --- | --- | --- | --- |
| [sig-agent-core](sig-agent-core/sig-info.yaml) | 负责 agent-core（Python Agent SDK）的开发维护 | startup | [xinyu-jiuwen](https://gitcode.com/xinyu-jiuwen)、[seanzhang_cn](https://gitcode.com/seanzhang_cn) | [openJiuwen/agent-core](https://gitcode.com/openJiuwen/agent-core) |
| [sig-agent-core-java](sig-agent-core-java/sig-info.yaml) | 负责 agent-core-java（Java Agent SDK）的开发维护 | startup | [shenwei21](https://gitcode.com/shenwei21)、[tianmingyong](https://gitcode.com/tianmingyong) | [openJiuwen/agent-core-java](https://gitcode.com/openJiuwen/agent-core-java) |
| [sig-agent-memory](sig-agent-memory/sig-info.yaml) | 负责 agent-memory（智能体长期记忆系统）的开发维护 | startup | [chenglinsong](https://gitcode.com/chenglinsong)、[li_zhonghua](https://gitcode.com/li_zhonghua)、[JingwenZhao](https://gitcode.com/JingwenZhao) | [openJiuwen/agent-memory](https://gitcode.com/openJiuwen/agent-memory) |
| [sig-agent-os](sig-agent-os/sig-info.yaml) | 负责 agent-os（Agent 系统服务）的开发维护 | startup | [liufangchao](https://gitcode.com/liufangchao)、[xinyu-jiuwen](https://gitcode.com/xinyu-jiuwen)、[hekefeng](https://gitcode.com/hekefeng) | [openJiuwen/agent-os](https://gitcode.com/openJiuwen/agent-os) |
| [sig-agent-protocol](sig-agent-protocol/sig-info.yaml) | 负责 agent-protocol（Agent 互操作协议 SDK）的开发维护 | startup | [YiyangShao](https://gitcode.com/YiyangShao)、[xinyu-jiuwen](https://gitcode.com/xinyu-jiuwen) | [openJiuwen/agent-protocol](https://gitcode.com/openJiuwen/agent-protocol) |
| [sig-agent-runtime-java](sig-agent-runtime-java/sig-info.yaml) | 负责 agent-runtime-java（Java Agent Runtime）的开发维护 | startup | [fujilie](https://gitcode.com/fujilie)、[LucioIT](https://gitcode.com/LucioIT) | [openJiuwen/agent-runtime-java](https://gitcode.com/openJiuwen/agent-runtime-java) |
| [sig-agent-solution](sig-agent-solution/sig-info.yaml) | 负责 agent-solution（Agent 解决方案）的开发维护 | startup | [LucioIT](https://gitcode.com/LucioIT)、[xingchao_ml](https://gitcode.com/xingchao_ml) | [openJiuwen/agent-solution](https://gitcode.com/openJiuwen/agent-solution) |
| [sig-agent-studio](sig-agent-studio/sig-info.yaml) | 负责 agent-studio（可视化 Agent 开发平台）的开发维护 | startup | [seanzhang_cn](https://gitcode.com/seanzhang_cn)、[xinyu-jiuwen](https://gitcode.com/xinyu-jiuwen) | [openJiuwen/agent-studio](https://gitcode.com/openJiuwen/agent-studio) |
| [sig-agent-tools](sig-agent-tools/sig-info.yaml) | 负责 agent-tools（Agent 工具能力）的开发维护 | startup | [seanzhang_cn](https://gitcode.com/seanzhang_cn)、[xinyu-jiuwen](https://gitcode.com/xinyu-jiuwen) | [openJiuwen/agent-tools](https://gitcode.com/openJiuwen/agent-tools) |
| [sig-deepsearch](sig-deepsearch/sig-info.yaml) | 负责 deepsearch（知识增强型深度检索与研究 Agent）的开发维护 | startup | [li_zhonghua](https://gitcode.com/li_zhonghua) | [openJiuwen/deepsearch](https://gitcode.com/openJiuwen/deepsearch) |
| [sig-docs](sig-docs/sig-info.yaml) | 负责社区文档体系建设与文档类贡献维护 | startup | — | [openJiuwen/community](https://gitcode.com/openJiuwen/community) |
| [sig-jiuwenswarm](sig-jiuwenswarm/sig-info.yaml) | 负责 jiuwenswarm（多智能体协同框架）的开发维护 | startup | [douran](https://gitcode.com/douran) | [openJiuwen/jiuwenswarm](https://gitcode.com/openJiuwen/jiuwenswarm) |
| [sig-jiuwensymbiosis](sig-jiuwensymbiosis/sig-info.yaml) | 负责 jiuwensymbiosis（具身智能 Agent 框架）的开发维护 | startup | [viviseason930](https://gitcode.com/viviseason930)、[zhangjiahui998](https://gitcode.com/zhangjiahui998) | [openJiuwen/jiuwensymbiosis](https://gitcode.com/openJiuwen/jiuwensymbiosis) |
| [sig-rm](sig-rm/sig-info.yaml) | 负责社区版本管理与需求管理 | startup | [ryanw22](https://gitcode.com/ryanw22)、[z00430070](https://gitcode.com/z00430070) | — |
| [sig-sec](sig-sec/sig-info.yaml) | 负责社区用户安全管理与安全相关规范 | startup | [yyuse](https://gitcode.com/yyuse)、[seanzhang_cn](https://gitcode.com/seanzhang_cn) | — |
| [sig-skillhub](sig-skillhub/sig-info.yaml) | 负责 skillhub（Skill 托管与分发平台）的开发维护 | startup | [caozhenhua0000](https://gitcode.com/caozhenhua0000)、[xiaowenzihwl](https://gitcode.com/xiaowenzihwl) | [openJiuwen/skillhub](https://gitcode.com/openJiuwen/skillhub) |

> 说明：sig-docs 的 `sig-info.yaml` 暂未登记 Maintainer，当前由 Committer（yuzengjie01、zhangmingyang_zz、huguangzheng、renquanjia）共同维护。

## 如何参与 SIG

openJiuwen 社区欢迎任何开发者参与 SIG，步骤如下：

1. **签署 CLA**：参与贡献前，请先[签署开发者贡献协议（CLA）](https://clasign.osinfra.cn/sign/68ee0908765718ad08bab9ee)。
2. **找到感兴趣的 SIG**：浏览上方[SIG 总览](#sig-总览)，或阅读[贡献指南](../README.md)了解各仓库的定位。
3. **联系对应 SIG**：通过该 SIG 的 `sig-info.yaml` 中的 Maintainer / Committer 联系，或加入[邮件列表](../maillist_zh.md)参与社区讨论。
4. **参与例会**：各 SIG 每月召开 1~2 次工作例会，会议公开举行，议题收集、技术讨论与会议纪要均对外开放，具体规则参见[社区章程](../coreteam/openJiuwen社区章程.md#sig)。
5. **认领任务**：在 SIG 负责的仓库中提交 Issue / PR，认领需求或修复问题。PR 提交规范请参考[贡献指南](../README.md)。

## 新建 SIG 流程

如果您与至少 2 位开发者对某一主题有共同兴趣，可以发起一个新的 SIG，流程如下：

1. **准备提案**：确定 SIG 名称与 Maintainer 候选人，并准备提案，内容应包括：
   - 创建 SIG 的背景信息
   - 创建 SIG 的业务范围
   - 创建 SIG 的业务目标
2. **提交评审**：将提案以 Issue 形式提交至 [community 仓库](https://gitcode.com/openJiuwen/community/issues)，供技术委员会（TC）评审。
3. **TC 审批**：TC 对提案进行评审，审核通过后正式批准成立 SIG。
4. **登记信息**：SIG 成立后，在本目录下新增 SIG 子目录（如 `sigs/sig-xxx/`），创建 `sig-info.yaml` 登记 SIG 元数据，并通过 PR 提交至 community 仓库。

> 详细规则请参阅[社区章程 - SIG 章节](../coreteam/openJiuwen社区章程.md#sig)。

## SIG 成熟度等级

每个 SIG 的 `sig-info.yaml` 中 `mature_level` 字段标识其成熟度等级：

| 等级 | 说明 |
| --- | --- |
| startup | 初创阶段：SIG 刚获 TC 批准成立，处于探索与建设期 |
| active | 活跃阶段：SIG 正常运行，定期召开例会并持续产出 |
| retired | 归档阶段：SIG 已撤销或停止运作，相关职责移交其他 SIG |
