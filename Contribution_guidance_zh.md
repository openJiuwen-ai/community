# 什么是openJiuwen

openJiuwen作为开源Agent平台，致力于提供灵活、强大且易用的AI Agent开发与运行能力。基于该平台，开发者可快速构建处理各类简单或复杂任务的AI Agent，实现多Agent协同交互，高效开发生产级可靠AI Agent；并助力企业与个人快速搭建AI Agent系统或平台，推动商用级Agentic AI技术广泛应用与落地。

# 系统架构

openJiuwen 采用分层架构设计，覆盖 AI Agent 从开发、运行到部署和运维的完整生命周期，整体由 **DeepAgents**、**Agent Studio** 、**Agent Framwork**、**Agent Distributed Runtime**、**Agent System Service** 组成。
- **DeepAgents**：提供面向不同场景的复杂智能体，如 JiuwenSwarm、JiuwenSymbiosis、DeepSearch 等，支持开箱即用。 
- **Agent Studio**：一站式 AI Agent 开发平台，提供低代码 / 零代码可视化开发能力，支持 Agent 开发、工作流编排、Prompt 调优、在线调试和资源管理，帮助开发者快速打造和调试智能体及工作流。
- **Agent Framework**: openJiuwen 核心框架与执行引擎，为开发者提供多场景、易用的 Agent 开发、编排与调用接口。覆盖复杂任务规划、循环执行、工具与技能调用、上下文管理、记忆子系统、多智能体协同、Agent 自演进、算力亲和调度等关键特性，全面支撑单体 Agent 到多 Agent 协同的工程化落地。
- **Agent Distributed Runtime**: 提供分布式 Agent 运行时底座，支持低码、高码两种智能体部署模式，实现 Agent 一键发布部署与全生命周期统一管控。原生内置多租户资源隔离、服务弹性扩缩容、统一注册发现、跨集群高速互通等核心能力，全面支撑大规模多 Agent 集群稳定运行、业务规模化落地。
- **Agent System Service**：AgentOS 底层基础系统服务，内置系统级安全隔离沙箱、全局统一记忆持久化存储、原生 CLI 系统工具、标准化 Agent 文件系统、跨Agent通信总线等底层核心能力，支撑全平台智能体安全运行、资源统一调度与多Agent高效协同。

<img src="https://gitcode.com/openJiuwen/community/blob/main/images/openJiuwen能力架构图.png" alt="openJiuwen能力架构图" style="display: block; width: 100%; max-width: 1000px; height: auto; margin: 16px auto;" />

## 实现概览

openJiuwen 采用模块化仓库设计，逐层构建 AI Agent 开发生态。各仓库可独立演进，也可组合使用，覆盖从智能体应用、技能分发、可视化编排、框架开发到服务化运行的完整链路。

<img src="https://gitcode.com/openJiuwen/community/blob/main/images/openJiuwen实现架构图.jpg" alt="openJiuwen实现架构图" style="display: block; width: 100%; max-width: 1000px; height: auto; margin: 16px auto;" />

### 代码仓总览

<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <colgroup>
    <col style="width: 18%;" />
    <col style="width: 26%;" />
    <col style="width: 56%;" />
  </colgroup>
  <thead>
    <tr>
      <th style="border: 1px solid; padding: 10px 12px; text-align: left; font-weight: 700;">模块</th>
      <th style="border: 1px solid; padding: 10px 12px; text-align: left; font-weight: 700;">仓库</th>
      <th style="border: 1px solid; padding: 10px 12px; text-align: left; font-weight: 700;">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3" style="border: 1px solid; padding: 10px 12px; font-weight: 700; vertical-align: middle;">Deep Agents</td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;"><a href="https://gitcode.com/openJiuwen/jiuwenswarm">jiuwenswarm</a></td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">多智能体协同框架与官方旗舰应用，支持复杂任务协作与 Skill 自演进。</td>
    </tr>
    <tr>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;"><a href="https://gitcode.com/openJiuwen/jiuwensymbiosis">jiuwensymbiosis</a></td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">面向具身智能的 Agent 框架，支持构型无关的能力复用与安全控制。</td>
    </tr>
    <tr>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;"><a href="https://gitcode.com/openJiuwen/deepsearch">deepsearch</a></td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">知识增强型深度检索与研究 Agent，面向搜索、推理和报告生成场景。</td>
    </tr>
    <tr>
      <td style="border: 1px solid; padding: 10px 12px; font-weight: 700; vertical-align: middle;">SkillHub</td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;"><a href="https://gitcode.com/openJiuwen/skillhub">skillhub</a></td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">Skill 托管与分发平台，支持 Skill 发布、版本管理、检索下载、共享复用及私有化部署。</td>
    </tr>
    <tr>
      <td style="border: 1px solid; padding: 10px 12px; font-weight: 700; vertical-align: middle;">Agent Studio</td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;"><a href="https://gitcode.com/openJiuwen/agent-studio">agent-studio</a></td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">一站式可视化 Agent 开发平台，支持 Agent 编辑、工作流编排、资源配置、Prompt 调优与在线调试。</td>
    </tr>
    <tr>
      <td rowspan="4" style="border: 1px solid; padding: 10px 12px; font-weight: 700; vertical-align: middle;">Agent Framework</td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">agent-gateway</td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">统一接入网关，提供 Channel 管理、消息处理、定时任务与心跳等能力，当前 Opening Soon。</td>
    </tr>
    <tr>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;"><a href="https://gitcode.com/openJiuwen/agent-core">agent-core</a></td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">Python Agent SDK，提供 Agent 编排、运行时、模型、工具、检索与评测等核心能力。</td>
    </tr>
    <tr>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;"><a href="https://gitcode.com/openJiuwen/agent-core-java">agent-core-java</a></td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">Java Agent SDK，为 Java 生态提供与 Python SDK 一致的 Agent 开发能力。</td>
    </tr>
    <tr>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;"><a href="https://gitcode.com/openJiuwen/agent-memory">agent-memory</a></td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">智能体长期记忆系统，支持记忆抽取、压缩、混合检索、沉淀构建与自主演化。</td>
    </tr>
    <tr>
      <td rowspan="3" style="border: 1px solid; padding: 10px 12px; font-weight: 700; vertical-align: middle;">Agent Distributed Runtime</td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;"><a href="https://gitcode.com/openJiuwen/agent-runtime">agent-runtime</a></td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">Python Agent Runtime，负责 Agent 服务化运行、会话管理与生命周期管理。</td>
    </tr>
    <tr>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;"><a href="https://gitcode.com/openJiuwen/agent-runtime-java">agent-runtime-java</a></td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">Java Agent Runtime，基于 Spring Boot 提供 Agent 服务化运行与部署能力。</td>
    </tr>
    <tr>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;"><a href="https://gitcode.com/openJiuwen/agent-protocol">agent-protocol</a></td>
      <td style="border: 1px solid; padding: 10px 12px; vertical-align: top;">Agent 互操作协议 SDK，提供 MCP SDK、A2A SDK 与 A2X Registry。</td>
    </tr>
  </tbody>
</table>
</div>

# 如何参与贡献

加入方式参见：https://www.openjiuwen.com/contribute

# 社区沟通与交流

如果您在使用openJiuwen过程中遇到问题，可以通过如下渠道联系我们。

网站： https://www.openjiuwen.com

邮箱： contact@openjiuwen.com

<!-- 左右并排 -->
<div style="display:flex; align-items: flex-start; gap: 50px;">
	<div style="text-align: center;">
		<img src="./images/公众号.jpg" width="200" alt="openJiuwen公众号">
		<p>openJiuwen公众号</p>
	</div>
	<div style="text-align: center;">
		<img src="./images/视频号.jpg" width="200" alt="openJiuwen视频号">
		<p>openJiuwen视频号</p>
	</div>
</div>