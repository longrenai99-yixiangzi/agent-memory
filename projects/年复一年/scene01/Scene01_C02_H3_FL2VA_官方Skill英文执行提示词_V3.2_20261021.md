# 《年复一年》Scene01｜C02 H3 FL2VA 官方Skill英文执行提示词 V3.2

日期：2026-10-21。状态：**最新版首尾静帧可进入首轮FL2VA测试；V3.2视频尚未生成、未经动态审核。**

## 参考图实际绑定（不得误用旧03、04A宽景）

- **Picture 1 / first_frame**：用户已确认的C02新版近景隐藏态 `C02首帧(2).png`，1672×941，SHA-256 `36bcb9aa4fff1c221f0148b2e06349d6aa8e0bb1885ca441dfb9155ad5b44eac`。
- **Picture 2 / last_frame**：刚通过当前静帧可执行性审核的最新尾帧 `warm_cinematic_cozy_indoor_scene_of_a_middle_age.png`，1672×941，SHA-256 `8ad18651a483c8eac02ee755af7618f1230f7d997302a4aded7f32bd7d430bec`。
- 上述是当前对话容器里已验证的原始文件，不代表已上传GitHub原始二进制PNG。两张必须接真正的FL2VA首帧与尾帧端口；`03.png`、`04A.png`旧宽景不再用于当前C02测试。
- 近景图两端机位、人物、柜体比例基本兼容；存在非动作区域的轻微重绘差异，动态测试需继续核对而不是预先宣布完美。

## 设计任务与自然物理路径

1. 妻子始终深蹲；上方手原本接触布叠上缘，下方手从大篮前缘转去托住**浅灰米色完整折叠布叠的前下缘**。
2. 双手承托同一完整布叠，**只做一次有目的的搬移**：略微抬起→向妻子身体和画面左侧移动约一掌宽→放稳于原大编织篮左前部。双手在尾帧依然轻扶布叠，**不能写成双手完全松开**。
3. 后方PR01旧纸盒一直静止在下层**右后方柜板**上，随布叠移位才从遮挡下露出少量盖沿、水平套盖接缝和边角；不能滑动或新增锁扣。两只编织篮原位不动，大篮移出动作留给后面的C05。
4. 妻子接近尾帧时仅以余光注意盒角，不大幅转头，不在C02提前完成后续C04的面部疑惑反应。

## 生成参数

- 模式：H3 FL2VA（真正first_frame/last_frame），单一固定中近景。
- 建议目标时长：5秒；首尾对齐文本为0.00s及5.00s；若工作流实际更改时长需一起修正。
- 16:9，24fps；沿用用户现有可运行的0.4MP与采样配置，本次仅替换提示词，不同时改多参数。
- 视频输出可能比5秒多一小段尾帧缓冲，以实际节点帧数为准。

## MiniMax H3官方FL2VA英文提示词

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 5.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] One continuous, completely locked-off medium-close live-action cinematic shot of an elderly East Asian woman in a deep, stable squat beside the open white cabinet in her living room at night. Picture 1 establishes the exact starting camera angle, person, clothing, cabinet, baskets, folded fabrics, and lighting. Picture 2 establishes the final arrangement. The camera position, framing and perspective remain unchanged from beginning to end. Her grey-white low bun, cream cardigan, muted grey-green patterned skirt, natural aged skin, the cabinet doors and hinges, upper wicker basket, and warm indoor light against a cool blue nighttime window all remain consistent.

The old mottled brown rectangular keepsake box is ALREADY resting, completely still, on the shelf at the back-right of the lower cabinet throughout this shot. It has a plain overlapping lid seam and no lock or metal clasp. At first it is hidden behind the folded light-grey beige knitted fabrics on the large wicker basket at the front-left of the same shelf. The box itself never changes position.

0.00–0.80 seconds: The woman looks down at the folded knitted stack. One hand is already near its upper edge; the other is lightly resting by the front rim of the large wicker basket.

0.80–1.60 seconds: She establishes a secure two-handed grip on ONE intact folded stack: one hand steadies its top and outer edge, while the other comes under and supports the near lower edge. The stack does not separate into loose individual garments.

1.60–3.50 seconds: In ONE clear, purposeful movement, she lifts the folded stack only enough to clear its resting contact, brings the whole stack slightly toward herself and toward screen-left by about a hand's width, then lowers it onto the LEFT-FRONT portion of the SAME large wicker basket. The basket stays inside the cabinet and does not shift. The small right-side basket and all upper shelf items stay still. Because the folded stack moves away from the camera's line of sight, a small part of the stationary box's brown mottled lid edge, horizontal lid seam and adjacent corner becomes visible at the back-right. The box is revealed by the moving fabric, never by the box moving.

3.50–4.50 seconds: She gently settles the stack into its stable new position, with both hands still lightly resting against the folded cloth, just as in Picture 2. The stack is supported by the basket, not suspended in the air. The box remains mostly concealed in the rear compartment.

4.50–5.00 seconds: Her hand movement comes to a natural stop. Without changing her deep squat or turning her head dramatically, her eyes begin to notice the exposed old box corner. End in the exact composition and hand positions of Picture 2, with quiet, restrained curiosity rather than a dramatic emotional reaction.

This is a single practical housekeeping action, performed once: support the stack, move it left-forward, set it down, and pause. No repeated touching or aimless searching. The old box and both wicker baskets remain physically fixed, with no self-moving box, box sliding out and back, duplicate objects, changing cabinet geometry, camera move or cut.

overall_soundscape: Quiet nighttime living-room ambience, the gentle rustling of folded knit fabric, and a soft touch against the wicker basket as the stack is set down. No box sliding or impact sound. No dialogue or singing.

non_diegetic_music: N/A
```

## 审片验收

- 镜头固定，不突然推近，不跳变景别；头发、脸、裙、柜门与上层篮位置稳定。
- 0.8—1.6s建立两手承托，1.6—3.5s布叠**一次性整体向左前方挪动**，而不是反复抚摸。
- 布叠最后有大篮承托、尾帧仍被双手轻扶；大篮没提前搬出柜子。
- 旧盒始终固定右后位置；因前景布品让位而局部可见，没有自己滑进滑出、长出锁扣或体积跳变。
- 到尾帧与Picture 2的手位、布叠位置、盒盖露出面积一致，且自然过渡；最终是否通过由用户审片决定。

如再次出现盒子自行移动或目的不明，应暂停盲目重复运行，回到首尾帧的遮挡几何和局部运动实现性，保留历史V3/V3.1失败样片，不以自由拼接冒充正确动作。
