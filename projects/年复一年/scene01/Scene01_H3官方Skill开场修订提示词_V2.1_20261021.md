# 《年复一年》Scene01｜H3官方Skill开场修订提示词 V2.1

**日期：2026-10-21**  
**状态更新（2026-10-21）：C01、C02已分别生成样片；C02已按本文件审查，未通过镜头验收。C01/C02的生成样片与动态审核记录见各自审查文件。本文件仍为执行提示词依据，不代表成片已批准。**  
**版本关系：本文件仅覆盖[V2原稿](Scene01_H3官方Skill规范执行提示词_V2_20261021.md)中的C01、C02的首尾帧与英文执行文字；V2的C03、C04、C05继续保留。原文件不覆盖、不删除。**  
**图片核对见**[01—04A机位/动作/遮挡核验与H3绑定表](Scene01_01-04A_机位动作遮挡核验及H3绑定修订_20261021.md)。

## 命名：局部编号，不是影片镜号

- C01/C02/C03/C04/C05仍为本段临时摄影镜号；[Shot 1]指**每段生成视频内部的第一镜**，不代表整部电影第一个镜头。
- 01是目前确认的柜前关门态，不等于断言整部短片以此开场。
- **02A与03A是完全相同的源图（SHA-256相同），只作为C01中途开门站姿参考，不另外生视频，也不作不同首尾帧。**
- 用户已确认镜头变化应发生在**完整蹲稳后**，C01是一条完整远景摄影镜头；C02是独立的较近机位摄影镜头。
- 03、04A都为完全蹲姿、柜前同侧较近机位；03在前，04A在后，物品显露变化要由真实手部整理产生。
- 本版遵守MiniMax官方 `h3-prompt-writing`、`base-en.txt` 的 FL2VA格式：首尾帧与时间标记在最前，随后英文三个字段 `integrated_multimodal_description`、`overall_soundscape`、`non_diegetic_music`。

## 一、绑定与时长

|摄影镜头|工作流|真正的first_frame|真正的last_frame|中间核验|建议生成时长|状态|
|---|---|---|---|---|---|---|
|C01 宽景开柜—完整蹲下|FL2VA|**01** 关门站姿|**02B** 开门完全蹲稳|02A=03A开门站姿|**10秒**（试验值）|建议待实测|
|C02 近景整理—局部露盒|FL2VA|**03** 近景蹲姿|**04A** 近景蹲姿局部露盒|02B作切点状态；上游完全隐藏态另核|**5秒**（试验值）|建议待实测|
|C03 柜内旧盒|I2VA|05A|无|—|按V2|未修改|
|C04 妻子反应|I2VA|05B|无|—|按V2|未修改|
|C05 一镜到底取盒|FL2VA|06|07B v02|06B、07A|按V2|未修改|

**执行硬约束**：同一视频中首次出现开门动作必须从01门关状态开始；C01到尾帧02B完成整个下蹲，再切镜进入C02，不能在动作中途切；C02不得只用04A做首帧去略过03与04A之间的遮挡变化。

## 二、C01｜FL2VA严格首尾帧｜01→02B｜10秒

- **直接接线**：first_frame＝`SC01-KF-001`，last_frame＝`SC01-KF-002B`。
- **仅审核的中间图**：02A和03A是同一图片，不是第三个实际输入口。
- **导演动作**：0—3秒开门；3—4秒观察下层；4—9秒完整下蹲；结束完全蹲稳，旧盒仍被遮挡。
- **核心风险**：模型可能直接跳到开门状态、略去下蹲或扭曲柜门；若发生则判生成失败，不能为了凑时长删掉动作。
- **后接C02**：必须等到02B对应的深蹲姿态稳定后，才切同轴线较近机位。

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 10.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action domestic family drama, one uninterrupted static medium-wide shot in a modest Chinese home living room at night. At 0.00 seconds, the elderly East Asian woman stands beside the CLOSED white lower cabinet in the composition and body position of Picture 1. Preserve her exact grey-white low bun, calm aged face, cream knitted cardigan, muted grey-green patterned long dress and light-colored low heels. Preserve the sofa on the left, the wooden coffee table, the window with cool-blue night foliage, the soft warm interior lamps, the cabinet hinges, both doors and the separate niche on the far right. The camera is locked off at its original wide-room angle, with no cut, zoom, pan, push-in or framing change.
From 0.00 to about 3.00 seconds, she brings her hand to the cabinet handle and gently swings the cabinet door outward on its actual existing hinge, then opens the lower cabinet access sufficiently to reach the stored items. She remains standing. By the end of this initial movement she passes through the intermediate open-door standing state represented by the already confirmed still 02A, which is exactly the same image as the stored 03A keyframe; this intermediate asset is NOT an additional cut.
From about 3.00 to 4.00 seconds, she looks down at the lower compartment without exposing the old box. The original wicker baskets and folded fabrics remain in front of the unseen object. Her hands withdraw from the upper shelf area and she prepares to squat.
From about 4.00 to 9.20 seconds, she slowly bends her knees and hips, keeps her feet planted, and lowers her torso with believable gravitational weight and natural joint movement. Her hands coordinate for balance and then return toward the ordinary storage materials in the lower compartment. The cabinet doors stay at their opened positions. No basket is removed, and the old brown box remains concealed by the front items.
From about 9.20 to 10.00 seconds, she has fully settled into a deep balanced squat; the shot progressively converges on Picture 2's wide-room framing and fully squatting posture. Keep the old box invisible from this vantage point. Finish with a short stable pause. Her outfit, face, living-room topology, cabinet contents and warm/cool lighting remain unchanged. No teleportation between standing and squatting, no door morphing, no camera cut or sudden shift to a closer view.

overall_soundscape: Quiet domestic nighttime ambience, a soft cabinet-handle contact and gentle hinged-door creak, followed by subtle clothing rustles as the woman carefully lowers her body. Faint contact sounds from the stored fabrics and wicker remain subdued. No speech or singing.

non_diegetic_music: N/A
```

## 三、C02｜FL2VA严格首尾帧｜03→04A｜5秒

- **直接接线**：first_frame＝原始`03.png`（正式存档`03-source/assets/03_original.png`），last_frame＝`04A`正式PNG。
- **动作**：从原已蹲姿位置微调整理叠布和前景篮子；遮挡状态因真实移动而变化，结束达到04A中旧盒部分可见状态。
- **注意**：从02B远景切到03近景时，检查妻子两手是否因明显重定位而跳变。避免错误地把03误当成03A。
- **核心风险**：03和04A只有细微前景物变化，若模型凭空显露旧盒或道具移动不符合几何关系，优先补动作而非宣称尾帧等于动态连贯。
- **后接C03**：04A的视线自然指向后部旧盒时，切05A物件近景；05A不是整个场景首次有旧盒露出的时刻。

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 5.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action domestic family drama, one uninterrupted static closer medium shot from the cabinet-side angle of Picture 1. The same elderly East Asian woman is ALREADY fully squatting when this shot starts; this is a NEW, closer camera shot introduced only after the preceding wide shot has shown her finishing the entire squat. Preserve her grey-white low bun, cream knitted cardigan, muted grey-green patterned long dress, natural lined skin, stable foot positions, and the existing white cabinet's door openings, hinge geometry, upper wicker basket and decorative objects. The warm-neutral room lamps and cool night foliage through the window remain continuous. No camera movement, zoom or internal cut.
At 0.00 seconds, the lower compartment shows the original front wicker basket and layers of folded beige and dark fabrics largely obscuring the deeper space, consistent with Picture 1. From about 0.50 to 2.70 seconds, she lightly adjusts the front folded fabric and the near edge of the wicker basket with very small, physically credible hand movements, without removing the large basket from the cabinet or disturbing the upper shelf. She does not reach toward or touch the old keepsake box.
From about 2.70 to 4.30 seconds, this modest movement of the front fabric slightly changes the line of sight into the rear of the lower compartment, allowing only part of the worn brown rectangular closed keepsake box to become visible. The box has been in the same place throughout; it does not pop into existence, move by itself, change size, glow or become fully exposed. The foreground objects remain recognizably the same and move only as a direct result of her actual fingertips.
From about 4.30 to 5.00 seconds, she slows her sorting gesture and lets her gaze settle briefly toward the newly noticed object, reaching the pose, hand position, partial reveal and exact closer composition of Picture 2. The shot ends with the box still inside the cabinet and only partly visible. No dramatic surprise, crying, nostalgia, exaggerated camera movement or impossible hand-object intersections.

overall_soundscape: Quiet nighttime room tone with gentle fabric and wicker friction as the woman adjusts the front storage items. The small handling sounds fade into a brief natural pause. No dialogue or singing.

non_diegetic_music: N/A
```

## 四、操作提醒

1. 两个FL2VA任务都必须在ComfyUI中使用真正的首帧和尾帧输入口，不要把两张图简单送进Ref2VA普通参考图集合。
2. 02B在用户Library中已找到并实际读取，SHA-256为`5013f907081de5afbe4c0af7da6739ca4ace419669a4993b8521a81417231d98`，**GitHub尚未作为独立已验证正式PNG保存**。执行用用户已确认的原图，避免误用其它02B候选。
3. 03原图与03A不同，SHA-256为`64996729333a2e7e0d95415eeb0aa29b78baad93b7a34bd426eeb9e976b25468`，切勿混用。
4. 由于01到02B两端背景、家具透视可能存在极小生成差异，技术上应先验证8GB显存下10秒FL2VA的稳定性；建议的10秒不锁定最终剪辑时长，如需分段续接也不代表增加导演切镜。
5. 原先`h3-prompt-writing`官方时长建议4—15秒，10秒与5秒均在范围内；不同工作流合法帧数要求单独核对，实际时长发生变化时必须同步调整英文首尾帧时间标记。
6. 任何图像静帧“保留”“已上传”，都不能被解释为相应视频已生成或动态连贯已批准。用户拥有最终导演审批权。


## 2026-10-21｜C02首轮视频审查状态

用户已按V2.1生成并上传C02样片。审查结论见[C02 H3视频审查](Scene01_C02_H3视频审查_20261021.md)：人物蹲姿、空间与机位稳定性基本保持，但画面仍为全客厅宽景，没有实现03→04A要求的近景变化；前景布品动作没有清楚建立旧盒由遮挡到局部显露的因果。暂不通过，先核对ComfyUI FL2VA是否实际使用03.png→04A正式PNG，再决定强化提示词或重生成。原样片保留，不覆盖。
