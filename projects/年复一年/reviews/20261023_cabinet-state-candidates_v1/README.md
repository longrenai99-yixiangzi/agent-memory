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


## 2026-10-23 更新：B2 重生成，C2 生成中

### B2 — 首次露角候选（新版本，不覆盖 B）
- Runway task ID：`4cc831fd-51cd-489c-a006-e35461af0c88`
- 新预览：[打开 B2 候选图](https://dnznrvs05pmza.cloudfront.net/gemini/gemini-3-pro-image/images/4cc831fd-51cd-489c-a006-e35461af0c88/b401420b-b841-4f52-bc0b-7dc0b2ec5a5c/Create_ONE_standalone_photorealistic_cinematic_still__16_9__.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMzQ1M2JlNjYyYTFhYmFkMSIsInR5cCI6InByb2QiLCJleHAiOjE3OTI4Nzk0NjJ9.Nlw7ixWq8UagwQyEQZeHjX7spMyHbrqCulHJVyu7HWw)
- 生成任务已完成。仅记录为新候选，未完成实际图像二进制归档、SHA-256 或视觉验收。

### C2 — 完整显露候选（新版本，不覆盖 C）
- Runway task ID：`7c4edd89-fa7c-41a3-9ddf-f552b4404526`
- 状态：最后一次查询时 RUNNING，进度 23%；尚无最终输出链接。
- 生成意图：从 B2 继续，移动前景布品/篮子，让同一旧盒完整显露但仍留在柜内，不接触、不抬起。

### 原图保存与审核状态
- 尝试直接下载 B2 原始 PNG 失败，尚未获得本地原始字节；不能计算或声称 SHA-256。
- 旧 A/B/C 与新 B2/C2 均保持候选状态，尚未逐图通过实际视觉验收。
- 不将预览 URL 视为永久资产，不覆盖旧版本，不用于正式视频生成。


## 2026-10-23 更新：C2 已完成生成，等待原图可访问后验收

### C2 — 完整显露候选（新版本，不覆盖 C）
- Runway task ID：`7c4edd89-fa7c-41a3-9ddf-f552b4404526`
- 最新预览：[打开 C2 候选图](https://dnznrvs05pmza.cloudfront.net/gemini/gemini-3-pro-image/images/7c4edd89-fa7c-41a3-9ddf-f552b4404526/2b85c647-a0e1-4f7e-a0fc-65e634b24f69/Edit__stateB2_into_ONE_standalone_photorealistic_cinematic_s.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiYWM0OTU1ZWJkMTk2YTNhMiIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5Mjg2MTY3NX0.JdZWApO4qjTUzzobFb42i-JlsqCdCu8-dwbjkaoC7jY)
- 状态：生成已完成（16:9，2K）。实际视觉验收未完成。
- 下载状态：尝试经当前执行环境下载原始 PNG 失败；尚未取得原始字节，因此无 SHA-256、无永久 PNG 入库。
- B2、C2 均为候选，不可视为正式资产。临时预览链接可能过期；链接可打开不代表视觉合格。

### 下一步边界
1. 必须先取得 B2、C2 的实际像素文件，核验盒角显露程度、同一柜体/机位、盒子唯一性与比例、物件物理落点。
2. 当前环境只能返回临时预览 URL，无法从该 URL 读取图像字节；Web 打开也报告该 URL 不可访问。视觉验收因此仍受阻，不能假称已检查。
3. 在 B2/C2 视觉验收之前，不生成 D1/D2，不做正式视频输入，不覆盖任何历史图。
4. 需要由用户将 B2、C2 原图下载后直接上传当前对话，或提供可读取的本地原文件；收到后再继续哈希、GitHub PNG 入库与后续取盒动作设计。


## 2026-10-23 追加：预览链接返回 Invalid JWT

- 用户实测 B/C2 临时预览链接，浏览器页面显示 `Invalid JWT`；该结果确认临时签名链接不可正常访问，不是用户操作失误。
- 重新调用 Runway 任务查询与最近资产列表，返回的仍是相同签名 URL；无法从当前连接获取 PNG 原始字节或刷新该链接的签名。
- B2/C2 的视觉内容因此仍未完成验收；没有计算 SHA-256，没有上传 PNG 二进制，也不生成 D1/D2。
- 下一步需从 Runway 的生成历史/资产页面导出 B2、C2 原始 PNG 并上传当前对话；随后检查盒角显露、盒体完整性、柜体机位比例和物理落点。旧候选继续保留，不覆盖。


## 2026-10-23 更新：用户上传了一张实际 PNG，已完成视觉与文件核验

### 上传文件信息
- 文件名：`Edit and reframe the provided TV-wall living-room reference.png`
- 文件来源判断：与最初 A 候选的任务标题/输出文件名相符（Runway task `898e495f-ec58-48ad-bc71-bb76d12e1335`）；它不是可据此确认的 B2 或 C2 文件。
- 实际文件：PNG，2048 × 1143，RGBA。
- SHA-256：`35e5944794603ecacee0f2740e0b1e99422b062aeacb8c6e982409eee4beebc7`。
- 当前记录的是文件的实际哈希；图片二进制尚未写入 GitHub 仓库，因此不能称为永久资产已归档。

### 视觉验收结论：不通过
- **A（完全遮挡）：不通过。** 旧盒的顶部与大部分正面清晰可见，违背“初始状态完全看不到盒子”的要求。
- **B2（只露极小盒角）：不通过。** 这张图里盒子露出面积过大，不符合首次只露出极小角的状态。
- **C2（完整显露且仍在柜内）：暂不通过。** 画面里主盒下方另有一块明显的棕色矩形物体，造成“同一盒子的结构还是第二个盒子/底座”的歧义；主盒下缘也被前景物品遮挡，不能作为干净、无歧义的完整显露状态。
- 柜体/机位/比例连续性：目前只有这一张真实文件，不能与 B2/C2 进行并排像素级比对。

### 后续动作
1. 保留该图为失败候选证据，不覆盖、不标记为正式资产。
2. 继续从 Runway 生成列表中下载其余状态图；按实际提示词/任务来源识别，不只看缩略图。
3. 取得 B2、C2 原图后单独验收；在 C 状态通过前不生成 D1/D2，也不生成视频。


### 2026-10-23 补充：用户指出此文件是按生成时间找到的最新结果
- 用户再次上传文件 `Edit and reframe the provided TV-wall living-room reference(1).png`，并说明这是时间最新的生成结果。
- 实测该文件与此前上传的 `Edit and reframe the provided TV-wall living-room reference.png` SHA-256 完全一致：`35e5944794603ecacee0f2740e0b1e99422b062aeacb8c6e982409eee4beebc7`；尺寸仍为 2048×1143，RGBA，PNG，4,269,922 bytes。故本次不是不同像素内容的新修订，而是同一图像的再次上传/重命名。
- 即使它是 Runway 当前最新生成项，视觉验收仍不通过：旧盒主体清晰可见，不符合 A 的完全遮挡，也不符合 B2 的只露极小盒角；若作为 C2，盒下方棕色矩形结构造成物件身份歧义，主盒下缘亦受遮挡，暂不批准。
- 保留其最新生成时间语境，但不重复登记为新资产、不覆盖旧版本、不生成 D1/D2。仍需从其余候选中下载像素内容不同的 B2/C2 图再验收。
