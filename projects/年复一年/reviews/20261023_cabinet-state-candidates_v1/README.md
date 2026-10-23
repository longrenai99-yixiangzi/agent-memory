# Scene01 白色下柜 A/B/C 状态图生成记录 V1

日期：2026-10-23  
项目：电影短片《年复一年》/ Scene01  
记录状态：候选生成任务已完成；**尚未通过实际视觉验收；未归档 PNG 二进制；未批准为正式资产**。  
审批规则：用户为最终导演与创作审批者。生成完成、提示词完整或有预览链接均不代表用户批准。

## 1. 目标

基于新客厅/电视墙空间，建立同一只 PR01 棕色合盖旧照片盒在同一白色低柜下层格中的连续状态：

- A：柜门打开，盒仍在后方，前景篮与布品完全遮住盒子的任何可识别部分。
- B：仅有少量前景布品移动，旧盒仍固定在原位，首次露出极小盒角。
- C：前景收纳物移开，唯一旧盒完整显露但仍留在柜内，未被取出。

硬约束：同一柜格、同一机位/透视、同一只盒、盒子尺寸与盖身比例不变；物件只能因明确动作改变位置；无拼图、无文字、无第二只同型盒。上层篮/罐/碟按既有用户确认保留。旧 SC01-PROP-001 原始失败图不得被新候选静默覆盖。

## 2. 生成结果登记

### A — 初始完全遮挡候选

- Runway task ID：898e495f-ec58-48ad-bc71-bb76d12e1335
- 预览：[打开 A 候选图](https://dnznrvs05pmza.cloudfront.net/gemini/gemini-3-pro-image/images/898e495f-ec58-48ad-bc71-bb76d12e1335/8e1ee687-8888-4cc4-8447-80a4c951cc39/Edit_and_reframe_the_provided_TV_wall_living_room_reference_.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiYWQxOGM2MjFmZTg2MjhjOSIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsImV4cCI6MTc5Mjg5MTU1M30.65O8TBpl8RQhBlI27MBcdeITjlC_orhKb5AZS-5VKeg)
- 任务意图：以电视墙/客厅参考生成单幅 16:9 柜内近景；前景编织篮、浅灰/米色叠布完全遮挡后方唯一旧盒。
- 预览链接预计于 2026-10-25 01:25:53 UTC 过期；并非永久仓库文件。

### B — 首次显露候选

- Runway task ID：dd99dade-f4b7-498a-bf25-51d37c48cf0b
- 预览：[打开 B 候选图](https://dnznrvs05pmza.cloudfront.net/gemini/gemini-3-pro-image/images/dd99dade-f4b7-498a-bf25-51d37c48cf0b/da3c6db3-0f51-4c77-9fc7-bd3795ad8337/Edit__stateA_into_ONE_standalone_photorealistic_cinematic_st.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMGU2OTQ4NWQxOWJkMTU0ZSIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsImV4cCI6MTc5MjgzMzYyOX0.LwU4jfyKxJojqxqTRp6lJfD3wWoTe-aqlTyr4oi0q6Q)
- 任务意图：基于 A 只小幅移动前景布品，旧盒固定在原位，仅露出一个很小的角与短薄盖沿。
- 预览链接预计于 2026-10-24 09:20:29 UTC 过期；并非永久仓库文件。

### C — 完整显露候选

- Runway task ID：983d4f30-3543-4c41-bab5-6628029157e1
- 预览：[打开 C 候选图](https://dnznrvs05pmza.cloudfront.net/gemini/gemini-3-pro-image/images/983d4f30-3543-4c41-bab5-6628029157e1/c3b87d3b-308c-4ccb-bc75-54a8fbd83803/Edit__stateB_into_ONE_standalone_photorealistic_cinematic_st.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNzYyZjU2ZTE1NzIzODBkNSIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsImV4cCI6MTc5MjkwNjcyMX0.oKCNPe0krHB2A3E3Ib1tT-4xNQwSqs3-eD83GItMzQE)
- 任务意图：基于 B，仅移动前景篮/布品以完整露出同一旧盒；盒仍在原柜格、未被拿出。
- 预览链接预计于 2026-10-25 05:38:41 UTC 过期；并非永久仓库文件。

## 3. 验收状态

| 检查项 | 状态 |
|---|---|
| A/B/C 三个生成任务完成 | 已完成 |
| 预览链接可见性 | 已提供，属于临时外链 |
| 实际像素级视觉复核 | 待完成 |
| A 是否真正完全遮挡 | 待确认 |
| B 是否仅露出极小盒角 | 待确认 |
| C 是否同盒、同尺度、仍在柜内 | 待确认 |
| 三图柜体/机位/灯光一致性 | 待确认 |
| PNG 原始二进制写入 GitHub | 未完成 |
| 用户正式批准 | 未完成 |
| 视频生成许可 | 未批准 |

## 4. 归档限制与下一步

当前运行环境只收到 Runway 返回的临时预览 URL，未取得三张 PNG 的本地原始字节；因此不能计算 SHA-256、不能将它们当作仓库中的永久图像资产，也不能冒称已完成真实视觉审核。

下一步：先将 A/B/C 原图保存到本地或重新上传到当前对话；逐图核验遮挡、盒子唯一性、柜体/机位/比例和物理落点。只有通过审核的图片，才以新版本独立上传到现有 reviews/<版本>/assets/ 结构，并补充哈希与审核记录。失败图保留为候选/失败证据，不覆盖历史原图，不直接用于 Seedance 视频生成。
