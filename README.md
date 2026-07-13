# openJiuwen 贡献指南

欢迎参与 openJiuwen 社区贡献！openJiuwen 作为开源 Agent 平台，致力于提供灵活、强大且易用的 AI Agent 开发与运行能力。我们鼓励开发者以各种方式参与社区贡献，包括但不限于代码贡献、文档改进、问题反馈、功能建议等。

## 目录

- [开始之前](#开始之前)
- [贡献类型](#贡献类型)
- [代码贡献流程](#代码贡献流程)
- [开发规范](#开发规范)
- [提交流程](#提交流程)
- [代码审查](#代码审查)
- [社区沟通](#社区沟通)

---

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

**社区热门仓库：**

- **openJiuwen JiuwenSwarm** - 多智能体协作的Agent系统，具备自然语言驱动多Agent协作、Skill自演进和工具调用能力。
- **openJiuwen Core** - AI Agent 开发、运行、调优与演进相关的全套 SDK 及工具。
- **openJiuwen Studio** - Agent 零码、低码可视化开发和工作流编排，模型、知识库、插件等各资源管理。

### 遵守行为准则

openJiuwen 是一个开源社区，它完全依赖于社区提供友好的开发和协作环境。在参与社区贡献之前，请先阅读并遵守 [openJiuwen 社区行为准则](https://gitcode.com/openjiuwen/community/tree/main/openJiuwen社区行为准则.md)。

### 签署开发者贡献协议（CLA）

**重要：** 您必须首先签署完成 openJiuwen 社区"开发者贡献协议"（CLA），才能参与 openJiuwen 社区贡献。

- 点击[这里](https://clasign.osinfra.cn/sign/68ee0908765718ad08bab9ee)签署 CLA
- 详细流程请参考[签署指南](https://gitcode.com/openjiuwen/community/tree/main/cla/cla使用指南.md)

### 找到感兴趣的 SIG

SIG（Special Interest Group，特别兴趣小组）是 openJiuwen 社区的技术组织单元。如何参与 SIG，请参考 [SIG 治理章程](https://gitcode.com/openJiuwen/community/blob/main/coreteam/openJiuwen%E7%A4%BE%E5%8C%BA%E7%AB%A0%E7%A8%8B.md#sig  )。

---

## 贡献类型

openJiuwen 社区欢迎多种形式的贡献：

### 代码贡献

您可以对现有代码进行评价、更改、反馈问题或贡献原创代码，我们鼓励开发者以各种方式参与代码反馈和贡献。

### 非代码贡献

- **文档贡献**：若需要贡献文档，请参考[文档贡献指南](https://gitcode.com/openJiuwen/community/blob/main/CONTRIBUTING_zh.md)
- **合规类问题**：若发现合规类问题，请参考[开源合规类问题管理](https://gitcode.com/openjiuwen/community/tree/main/contribute/开源合规类问题管理.md)
- **安全类问题**：若发现安全/漏洞问题，请参考：
  - [网络安全事件管理流程](https://gitcode.com/openjiuwen/community/tree/main/contribute/网络安全事件管理.md)
  - [社区漏洞治理&披露](https://gitcode.com/openjiuwen/community/tree/main/contribute/社区安全漏洞治理及披露.md)

---

## 代码贡献流程

### 环境准备

1. **安装 Git**
   - 针对 Git 的安装、环境配置及使用方法，请参考 GitCode 帮助中心的 [Git 知识大全](https://docs.gitcode.com/docs/help/home/general-reference/git)

2. **配置 SSH 公钥**
   - 注册 SSH 公钥，请参考 GitCode 帮助中心的 [公钥管理](https://docs.gitcode.com/docs/help/home/user_center/security_management/ssh)

3. **找到感兴趣的仓库**
   - 在 openJiuwen 的代码托管平台上找到您感兴趣的 Repository

### Fork 仓库

1. 找到并打开对应 Repository 的首页
2. 点击右上角的 **Fork** 按钮，按照指引，建立一个属于**个人**的云上 Fork 分支

### 克隆到本地

1. **创建本地工作目录**

   ```bash
   mkdir ${your_working_dir}
   cd ${your_working_dir}
   ```

2. **克隆远程仓库**

   - 在仓库页面复制远程仓库的地址（`$remote_link`）
   - 在本地执行克隆命令：

   ```bash
   git clone $remote_link
   ```

### 创建开发分支

1. **拉分支**

   更新您的本地分支：

   ```bash
   git remote add origin $remote_link
   git fetch origin
   git checkout main
   git pull --rebase
   ```

   基于远端 main 分支拉取本地调试分支：

   ```bash
   git branch myfeature origin/main
   git checkout myfeature
   ```

   然后在 myfeature 分支上编辑和修改代码。

---

## 开发规范

### License

openJiuwen 采用 [Apache License 2.0 (Apache-2.0)](https://www.apache.org/licenses/LICENSE-2.0)。

### 版权规范

**重要：** 用户提交的代码必须是原创内容，不得侵犯他人知识产权。

- 贡献代码请遵守[许可证与版权规范](https://gitcode.com/openjiuwen/community/tree/main/contribute/许可证与版权规范.md)
- 若新贡献代码涉及第三方开源软件引入或片段引用，请严格遵守[许可证与特殊许可证评审指导](https://gitcode.com/openjiuwen/community/tree/main/contribute/许可证与特殊许可证评审指导.md)中的要求
- openJiuwen 有权根据相关规范修改/删除开发者贡献的内容，直至符合对应规范要求

### 设计规范

- [openJiuwen 安全设计规范](https://gitcode.com/openjiuwen/community/tree/main/contribute/style-guide/openJiuwen-security-design-guide.md)

### 代码风格

请遵循 openJiuwen 编程规范，进行代码开发、检视，务必保持代码风格统一。

- **Python 语言编程规范**：[PEP 8](https://pep8.org/)
- **JavaScript 语言编程规范**：[openJiuwen JavaScript 编码规范](https://gitcode.com/openjiuwen/community/tree/main/contribute/style-guide/openJiuwen-JavaScript-coding-style-guide.md)

### 提交信息规范

提交信息遵循 [Conventional Commits（约定式提交规范）](https://www.conventionalcommits.org/zh-hans/v1.0.0/)。采用此规范有助于提升提交历史的可读性，同时便于自动化工具生成变更日志。

**格式：**
```
<type>(<scope>): <subject>
```

注意事项：

- 提交信息采用英文格式。
- 通过`git rebase`将多次零散提交合并为单个原子性提交，确保主干提交历史清晰可追溯。

**类型（type）：**
- `feat:` 新功能
- `fix:` 错误修复
- `docs:` 仅文档更改
- `style:` 不影响代码含义的更改（空格、格式等）
- `refactor:` 既不修复错误也不添加功能的代码更改
- `perf:` 提高性能的代码更改
- `test:` 添加缺失的测试或更正现有测试
- `ci:` CI 配置文件和脚本的更改
- `chore:` 对构建过程或辅助工具和库的更改


**范围（scope）：** 可选，表示影响的范围，如 `model`、`agent`、`workflow` 等。


**示例：**
```bash
feat(model): add user authentication module
fix(front): resolve button click event issue
docs(guide): update contribution guidelines
style(agent): adjust code formatting to match style guide
refactor(workflow): simplify component structure
perf(runtime): optimize runtime performance
test(endpoint): add unit tests for API endpoints
ci: configure GitCode CI pipeline
chore: update dependencies to latest versions
```

**复杂提交格式：**
对于需要详细说明的提交，可以使用多行格式：

```
feat(core): add configuration management feature

Add configuration management module to support dynamic settings loading.
This feature includes:

- Configuration file parser
- Environment variable support
- Settings validation logic

Refs: #12345
```

---

## 提交流程

### 1. 在本地工作目录提交变更

```bash
git add .
git commit -sm "feat: xxx"  # 提交信息包含signoff邮箱
```

您可能会在前次提交的基础上，继续编辑构建并测试更多内容，可以使用 `commit --amend` 继续添加提交。

### 2. 将变更推送到您的远端目录

准备进行审查（或只是建立工作的异地备份）时，将分支推到您的 fork 仓库：

```bash
git push -f origin myfeature
```

### 3. 创建 Pull Request

1. 访问您的 Fork 仓库页面
2. 点击 **创建 Pull Request** 按钮
3. 选择您的功能分支生成 PR
4. 详细操作请参考 GitCode 帮助中心的[开发协作指导](https://docs.gitcode.com/docs/help/home/org_project/pullrequests/pr-create)

**PR 描述建议包含：**

- 变更的目的和背景
- 变更的详细说明
- 测试情况
- 相关 Issue 编号（使用 `#I12345` 格式）

### 4. 关联 Issue 与门禁构建

#### 创建 Issue

1. 找到并打开对应 Repository 的首页
2. 选择左上角的 **Issues** 页签
3. 点击右侧 **新建 Issue** 按钮
4. 按照指引建立一个专属的任务，用于相关联的代码（开发特性/修改 Bug）执行 CI 门禁

#### 关联 Issue 与 PR

创建 PR 或编辑已有的 PR 时，在描述框输入 `#I` + 五位 Issue ID（例如：`#I12345`），即可将 Issue 与 PR 关联。

#### 触发代码门禁

门禁执行完成，会在该 Issue 关联的所有 PR 中自动评论门禁执行结果。

---

## 代码审查

### PR 审查约束

- 需要达到最低评审人数
- 评审问题全部解决才能合入
- **禁止合入自己创建的 Pull Request**
- 合并 PR 前需确保关联的流水线任务成功运行并通过检查

### CI 持续集成

openJiuwen 通过持续集成（CI，Continuous Integration）及时发现代码问题，确保代码质量可靠和功能稳定：

- **代码门禁**：开发者向 openJiuwen 提交代码合入申请后，会触发门禁检查，例如静态检查、代码编译、功能测试等，门禁通过后才能合入代码
- **每日构建**：openJiuwen 的持续集成流水线每日自动执行，以便提前发现代码静态检查、编译、功能等方面的问题，及时修复问题，确保代码质量

---

## 社区沟通

### 邮件列表

如果您在使用 openJiuwen 过程中遇到问题，请加入邮件群组参与讨论。这是参与 openJiuwen 社区讨论的正确方式，请参考[订阅邮件列表](https://gitcode.com/openJiuwen/community/blob/main/maillist_zh.md)。

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


### 获取帮助

- 查看文档：[openJiuwen 文档中心](https://gitcode.com/openjiuwen/docs)
- 提交 Issue：在对应仓库的 Issues 页面创建问题
- 参与讨论：通过邮件列表与社区成员交流

---

## 总结

**感谢您对 openJiuwen 社区的关注和贡献！我们期待您的参与，共同推动 AI Agent 技术的发展**。🎉


