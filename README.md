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

## 开始之前

### 了解 openJiuwen

openJiuwen 为原生支持多智能体协同和智能体自演进而设计，系统架构主要由 **openJiuwen Core**、**openJiuwen Studio** 和 **openJiuwen Ops**（即将开放）三大部分组成，为开发者提供从 Agent 开发、调优到部署的一站式平台。

![架构图](https://openjiuwen-ci.obs.cn-north-4.myhuaweicloud.com/testmyai/ScreenShot_2025-12-05_144831_247.png)

**社区热门仓库：**

- **openJiuwen Studio** - Agent 零码、低码可视化开发和工作流编排，模型、知识库、插件等各资源管理
- **openJiuwen Core** - AI Agent 开发、运行、调优与演进相关的全套 SDK 及工具
- **community** - 社区章程、社区规范、CLA 签署等社区运作类相关信息
- **docs** - openJiuwen 文档中心，存放社区所有 SIG 组的技术文档和手册

### 遵守行为准则

openJiuwen 是一个开源社区，它完全依赖于社区提供友好的开发和协作环境。在参与社区贡献之前，请先阅读并遵守 [openJiuwen 社区行为准则](https://gitcode.com/openjiuwen/community/tree/master/openJiuwen社区行为准则.md)。

### 签署开发者贡献协议（CLA）

**重要：** 您必须首先签署完成 openJiuwen 社区"开发者贡献协议"（CLA），才能参与 openJiuwen 社区贡献。

- 点击[这里](https://clasign.osinfra.cn/sign/68ee0908765718ad08bab9ee)签署 CLA
- 详细流程请参考[签署指南](https://gitcode.com/openjiuwen/community/tree/master/cla/cla使用指南.md)

### 找到感兴趣的 SIG

SIG（Special Interest Group，特别兴趣小组）是 openJiuwen 社区的技术组织单元。如何参与 SIG，请参考 [SIG 治理章程](https://gitcode.com/openJiuwen/Sigs)。

---

## 贡献类型

openJiuwen 社区欢迎多种形式的贡献：

### 代码贡献

您可以对现有代码进行评价、更改、反馈问题或贡献原创代码，我们鼓励开发者以各种方式参与代码反馈和贡献。

### 非代码贡献

- **文档贡献**：若需要贡献文档，请参考[文档贡献指南](https://gitcode.com/openjiuwen/docs/tree/master/CONTRINUTING_zh.md)
- **合规类问题**：若发现合规类问题，请参考[开源合规类问题管理](https://gitcode.com/openjiuwen/community/tree/master/contribute/开源合规类问题管理.md)
- **安全类问题**：若发现安全/漏洞问题，请参考：
  - [网络安全事件管理流程](https://gitcode.com/openjiuwen/community/tree/master/contribute/网络安全事件管理.md)
  - [社区漏洞治理&披露](https://gitcode.com/openjiuwen/community/tree/master/contribute/社区安全漏洞治理及披露.md)

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
   git checkout master
   git pull --rebase
   ```

   基于远端 master 分支拉取本地调试分支：

   ```bash
   git branch myfeature origin/master
   git checkout myfeature
   ```

   然后在 myfeature 分支上编辑和修改代码。

---

## 开发规范

### License

openJiuwen 采用 [Apache License 2.0 (Apache-2.0)](https://www.apache.org/licenses/LICENSE-2.0)。

### 版权规范

**重要：** 用户提交的代码必须是原创内容，不得侵犯他人知识产权。

- 贡献代码请遵守[许可证与版权规范](https://gitcode.com/openjiuwen/community/tree/master/contribute/许可证与版权规范.md)
- 若新贡献代码涉及第三方开源软件引入或片段引用，请严格遵守[许可证与特殊许可证评审指导](https://gitcode.com/openjiuwen/community/tree/master/contribute/许可证与特殊许可证评审指导.md)中的要求
- openJiuwen 有权根据相关规范修改/删除开发者贡献的内容，直至符合对应规范要求

### 设计规范

- [openJiuwen 安全设计规范](https://gitcode.com/openjiuwen/community/tree/master/contribute/style_guide/openJiuwen-security-design-guide.md)

### 代码风格

请遵循 openJiuwen 编程规范，进行代码开发、检视，务必保持代码风格统一。

- **Python 语言编程规范**：[PEP 8](https://pep8.org/)
- **JavaScript 语言编程规范**：[openJiuwen JavaScript 编码规范](https://gitcode.com/openjiuwen/community/tree/master/contribute/style_guide/openJiuwen-JavaScript-coding-style-guide.md)

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

**范围（scope）：** 可选，表示影响的范围，如 `models`、`agent`、`studio`、`core` 等。



**示例：**
```bash
feat(core): add user authentication module
fix(studio): resolve button click event issue
docs(guide): update contribution guidelines
style(core): adjust code formatting to match style guide
refactor(studio): simplify component structure
perf(core): optimize data loading performance
test(core): add unit tests for API endpoints
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

Refs: #I12345
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

如果您在使用 openJiuwen 过程中遇到问题，请加入邮件群组参与讨论。这是参与 openJiuwen 社区讨论的正确方式，请参考[订阅邮件列表](https://gitcode.com/openJiuwen/community/blob/master/maillist_zh.md)。

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


