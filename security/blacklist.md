# 禁止内容与禁用词扫描说明 / Prohibited Content & Blacklist Scan

**语言 / Language：[中文](#中文) | [English](#english)**

---

## 中文

### 一、禁止明文上传违规内容

社区的**任何仓库、任何分支**，都**禁止以明文形式上传任何政治、色情、暴力等违法违规内容**。

包括但不限于：安全策略说明、大模型安全提示词、禁用词列表等——任何形式的明文都在禁止之列。

### 二、禁止上传涉密信息

社区的**任何仓库、任何分支**，都**禁止上传所有公司的内部信息**、秘钥信息等涉密信息。

包括但不限于：任何密钥、公司的内部域名/内部信息/保密信息等等未公开信息等。

### 三、禁用词扫描失败怎么办

如果流水线的"禁用词扫描"任务失败：请联系对应**仓库的 CIE 或接口人**，到流水线中找到对应的"黑名单扫描"任务，**查看报错日志进行定位**。

> 返回顶部 / Back to top：[语言切换](#禁止内容与禁用词扫描说明--prohibited-content--blacklist-scan)

---

## English

### 1. No plaintext prohibited content

In **any repository and any branch** of the community, uploading any illegal or non-compliant content — political, pornographic, violent, etc. — **in plaintext is strictly prohibited**.

This includes but is not limited to: security policy descriptions, LLM safety prompts, and blacklist word lists — plaintext of any such form is forbidden.

### 2. No confidential information

In **any repository and any branch** of the community, uploading information that the company forbids from being shared externally, internal information of other companies, or any other confidential information is **prohibited**.

This includes but is not limited to: keys/secrets, internal domain names of other companies, information covered by NDAs signed with other companies, and non-public information obtained during collaboration with other companies.

### 3. What to do when the blacklist scan fails

If the "blacklist scan" stage in the pipeline fails: contact the **CIE or point of contact of the corresponding repository**, find the "blacklist scan" task in the pipeline, and **check the error log to locate** the offending content.

> 返回顶部 / Back to top：[Language switch](#禁止内容与禁用词扫描说明--prohibited-content--blacklist-scan)
