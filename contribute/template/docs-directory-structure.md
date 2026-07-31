# docs 目录结构模板

本模板展示 openJiuwen 各仓 docs 目录的标准结构，配合 [各仓资料体系治理规范](../各仓资料体系治理规范.md) 使用。

> **说明：**
> 以下为完整的目标结构示意。各仓可根据实际内容增减文件，但四类目录（tutorial、how-to、reference、explanation）必须齐全。

## 完整目录结构

```
仓根/
├── README.md                  # 最小闭环：定位 / 特性 / 相关文档 / 环境 / 安装 / QuickStart / License
├── LICENSE                    #
├── CHANGELOG.md               # 可选：变更日志；可通过 GitCode Release 管理，但 README 须有 Release 入口
├── CONTRIBUTING.md            # 贡献指南
├── SECURITY.md                # 可选：安全策略；参考：https://gitcode.com/openJiuwen/skillhub/blob/develop/SECURITY.md
│
├── examples/                  # 可运行示例工程（clone 即跑）
│   ├── README.md              # 示例总览（列出所有示例及用途）
│   └── {example-name}/       # 每个示例一个目录
│       ├── README.md          # 示例说明（运行命令、预期输出）
│       └── ...
│
├── docs/                      # 用户文档（给用户读，Diátaxis 四类）
│   ├── README.md              # 文档介绍与导航入口；参考：https://gitcode.com/openJiuwen/jiuwenswarm/blob/develop/docs/README.md
│   │
│   ├── zh/                    # 中文权威源
│   │   ├── tutorial/          # 教程（"我想学"，数字前缀编号）
│   │   │   ├── 01-quick-start.md          # 快速开始
│   │   │   ├── 02-first-agent.md          # 第一个 Agent
│   │   │   └── 03-workflow-basics.md      # 工作流入门
│   │   │
│   │   ├── how-to/            # 操作指南（"我想做"，语义名不编号）
│   │   │   ├── configure-llm.md           # 配置大模型
│   │   │   ├── configure-mcp.md           # 配置 MCP 服务
│   │   │   ├── deploy-service.md          # 部署服务
│   │   │   └── integrate-a2a.md           # 接入 A2A 协议
│   │   │
│   │   ├── reference/         # 参考文档（"我想查"，语义名不编号）
│   │   │   ├── api.md                     # API 文档入口
│   │   │   ├── config-params.md           # 配置参数表
│   │   │   └── error-codes.md             # 错误码表
│   │   │
│   │   └── explanation/       # 解释文档（"我想理解"，语义名不编号）
│   │       ├── architecture-overview.md   # 架构概述
│   │       ├── design-decisions.md         # 设计决策
│   │       └── key-concepts.md            # 关键概念
│   │
│   └── en/                    # 英文跟随（结构与 zh/ 对称）
│       ├── tutorial/
│       ├── how-to/
│       ├── reference/
│       └── explanation/
│
└── design/                    # 可选：开发设计稿（给开发者；如涉及架构机制等请归档此处，不要放入 docs）
    ├── session-vcs.md          # Session 版本控制设计
    └── ...
```

> **说明：**
> 备注中标注为"可选"的文件或目录，表示在有必要时包含即可，不要求必须存在。

> **说明：**
> docs/README.md 作为文档介绍与导航入口，简要说明文档覆盖范围和阅读建议，并按四类列出文档链接。当某一类别文档数量超过 10 篇时，再在该类别目录下新建 README.md 做栏目级导航。

## SDK 仓与服务仓的差异

SDK 仓和服务仓在 Reference 目录下内容不同：

### SDK 仓（agent-core、agent-core-java、agent-memory）

```
docs/zh/reference/
├── {package-name}/           # 按包组织 API 文档
│   ├── README.md             # 包级导航（可选，文档多时再加）
│   └── {class-name}.md       # 类级 API 文档（方法签名、参数、返回值）
└── config-params.md          # 配置参数表
```

### 服务仓（agent-runtime、agent-runtime-java、agent-studio）

```
docs/zh/reference/
├── rest-api.md               # 精简版 REST API 参考（核心接口加典型请求响应示例）
├── openapi.json              # OpenAPI 规范（自动生成或导出）
└── error-codes.md            # 错误码表
```

> **说明：**
> 服务仓的 Reference 推荐双轨并行：docs 中放精简版 REST API 参考，完整版由服务运行时 OpenAPI 自动生成。docs 中链接到运行时的 `/docs` 端点。

## 迁移映射参考

从当前结构迁移到 Diátaxis 四类结构的映射参考：

| 当前位置 | 目标位置 | 类别 |
| -------- | -------- | -------- |
| 基础功能/接入大模型.md | tutorial/01-connect-llm.md | Tutorial |
| 基础功能/自定义工具.md | how-to/custom-tool.md | How-to |
| 高阶用法/MCP工具.md | how-to/configure-mcp.md | How-to |
| 高阶用法/上下文引擎.md | explanation/context-engine.md | Explanation |
| 高阶用法/记忆引擎.md | explanation/memory-engine.md | Explanation |
| 智能体/构建ReActAgent.md | tutorial/02-build-react-agent.md | Tutorial |
| 工作流/构建工作流.md | tutorial/03-build-workflow.md | Tutorial |
| API文档/ | reference/ | Reference |
| documents/ | docs/ | 目录改名 |

> **说明：**
> 迁移时只移动和改名文件，不重写内容。内容质量的提升在迁移完成后再逐步进行。
