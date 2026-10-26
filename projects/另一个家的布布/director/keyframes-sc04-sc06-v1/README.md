# SC04—SC06关键状态帧任务及完整中文提示词 V1

日期：2026-10-25。8张用户角色原图已取得并目视核对；机位/路线和连续蹲姿已批准。本包完成制作准备，11张均未生成，不是11个最终镜头。

原先最少8状态增加了23:15蹲稳、蹲姿抱稳→站稳接口及B接回稳定末态，防止把承重动作和批准的连续姿态省略。

## 实际已有参考及用途

- `PLAN`：[文件](../../assets/space/PLAN-001_彩平图_20261025_阳台家具删除版.png)；实际家具、墙体和开放阳台垭口，不复制俯视角。
- `ZONE`：[文件](../../assets/space/PLAN-002_AB世界交汇区标注_V2.2.png)；G/E/X行动关系，不沿用旧底图家具。
- `V01`：[文件](../../assets/views/VIEW-01_朝阳台.png)；阳台/电视/沙发关系、外窗关闭。
- `V03`：[文件](../../assets/views/VIEW-03_朝沙发.png)；新版v02沙发、贵妃位、薄毯、茶几和阳台垭口。
- `V02`：[文件](../../assets/views/VIEW-02_朝厨房.jpg)；餐厨外围。
- `W`：[文件](../../assets/characters/wife-identity.png)；A/B共同面部身份；忽略蓝背景、白吊带和静态笑容。
- `A`：[文件](../../assets/characters/wife-A-fullbody.png)；A浅银灰滚边长袖长裤睡衣、赤脚与身材比例。
- `B`：[文件](../../assets/characters/wife-B-fullbody.png)；B黑色细吊带长裙、赤脚与身材比例。
- `B3`：[文件](../../assets/characters/wife-B-three-views.png)；侧背面轮廓、盘发；黑裙仅供B，不抄文字版式。
- `CAT`：[文件](../../assets/characters/bubu-multiview.png)；同一只浅奶油短卷毛蓝眼大耳猫的侧/正/斜前坐姿，不复制多只猫。
- `MAP4`：[文件](../../director/previs-sc04-sc06-v1/SC04_camera-route_v1.png)；已批SC04机位与路线，不复制箭头色块。
- `MAP5`：[文件](../../director/previs-sc04-sc06-v1/SC05_camera-route_v1.png)；已批SC05机位与路线，不复制箭头色块。
- `MAP6`：[文件](../../director/previs-sc04-sc06-v1/SC06_camera-route_v1.png)；已批SC06机位与路线，不复制箭头色块。

## 执行前置与分批顺序

先做一张K04-E0，兼作C42视角与第八夜夜景曝光候选；通过后派生E1。无需强制额外制作一整套空景。只对实际进入画面的G外猫用品提供造型候选，不为画外物件预先增加生图任务。其余机位继承通过的同夜曝光与物件，不一轮生成11张。
现有六视图是白天参考，不是假定夜景已通过。后续任务需要前一通过帧作编辑目标；这些帧目前不存在，不伪造上传编号。下列提示词只列真实已有输入，实际执行时再加入已通过帧，绑定真实上传编号。

## 状态任务清单

| ID | 场次/剧情时点 | 机位 | 用途 | 前置任务 | 当前状态 |
|---|---|---|---|---|---|
| [K04-E0](prompts/K04-E0.txt) | SC04/23:13 | C42 | 猫在E外，未回应 | K04-E0兼核夜景/机位 | 提示词已备，未生成 |
| [K04-E1](prompts/K04-E1.txt) | SC04/23:14 | C42 | 四脚全入G | K04-E0 | 提示词已备，未生成 |
| [K04-R1](prompts/K04-R1.txt) | SC04/23:15 | C41 | 妻子回应后蹲稳 | K04-E1 | 提示词已备，未生成 |
| [K05-T0](prompts/K05-T0.txt) | SC05/23:21—23:22 | C52 | 同一蹲姿闻手 | K04-R1 | 提示词已备，未生成 |
| [K05-H0](prompts/K05-H0.txt) | SC05/23:23托起阶段 | C52 | 蹲姿已托猫抱稳 | K05-T0 | 提示词已备，未生成 |
| [K05-H1](prompts/K05-H1.txt) | SC05/23:23站稳阶段 | C52 | 抱稳后站稳 | K05-H0 | 提示词已备，未生成 |
| [K06-O0](prompts/K06-O0.txt) | SC06/23:24—23:25 | C61 | 客观双妻子关系 | K05-H1 | 提示词已备，未生成 |
| [K06-P0](prompts/K06-P0.txt) | SC06/23:26 | C62 | B真实眼位空镜 | K06-O0 | 提示词已备，未生成 |
| [K06-X0](prompts/K06-X0.txt) | SC06/23:29放手后 | C63 | 猫仍G内，手已放开 | K06-P0, K05-H1 | 提示词已备，未生成 |
| [K06-X1](prompts/K06-X1.txt) | SC06/23:29完整越界后 | C63 | 猫四脚全出X | K06-X0 | 提示词已备，未生成 |
| [K06-B0](prompts/K06-B0.txt) | SC06/23:30关闭前 | C63 | B在G外已抱回 | K06-X1 | 提示词已备，未生成 |

## 可直接复制的逐项提示词

### K04-E0｜猫在E外，未回应

```text
任务K04-E0：猫在E外，未回应。
单张写实电影关键状态候选，横向16:9，不是最终灯光定稿。严格按PLAN实际家具和开放阳台垭口，G/E/X及机位按已批预演；不抄图纸俯视角、文字、箭头或色块。外窗关闭，地面裸瓷砖，无地毯，阳台无座椅。B世界猫爬架在阳台G外，窝和食水在电视柜与房门之间G外；具体用品造型尚无获批图，执行前需设计候选/空景审核。
出现妻子时以用户已采用C41校准照锁定当前A/B五官，保留棕色低盘发。A只穿wife-A-fullbody浅银灰滚边长袖长裤睡衣、赤脚；B只穿wife-B-fullbody黑色吊带长裙、赤脚。忽略证件图背景与静态微笑，不借用《年复一年》银发老人。出现布布时按bubu-multiview的单只浅奶油短卷毛蓝眼大耳猫，不复制成多猫，不添项圈，不变长毛或无毛猫。猫与人体尺度由候选图交用户审核，不编体重/身高。
候选光线按剧情第八夜夜景：沿现有室内灯具暖光，外窗微弱冷夜与雨痕，脸、猫与接触地面清楚；不沿用白天阳光。具体曝光尚待审核，成对帧沿用前帧获批光线，不擅自加闪电亮帧。禁止文字、水印、多栏拼图、额外人物及漂浮融合肢体。

本帧构图与动作：
固定低位斜看阳台开放垭口与E，保留沙发窗端、茶几边和地砖接缝。布布已下猫架、四脚全部在G外阳台地面，身体朝室内自然前行，不看向A。只出现一只猫，A不入画，A在剧情中仍站在G内。

已有输入文件及职责：
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-001_彩平图_20261025_阳台家具删除版.png：实际家具、墙体和开放阳台垭口，不复制俯视角
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-002_AB世界交汇区标注_V2.2.png：G/E/X行动关系，不沿用旧底图家具
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-01_朝阳台.png：阳台/电视/沙发关系、外窗关闭
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-03_朝沙发.png：新版v02沙发、贵妃位、薄毯、茶几和阳台垭口
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\bubu-multiview.png：同一只浅奶油短卷毛蓝眼大耳猫的侧/正/斜前坐姿，不复制多只猫
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\director\previs-sc04-sc06-v1\SC04_camera-route_v1.png：已批SC04机位与路线，不复制箭头色块

验收：猫四脚均在E外；无回应，尚未上沙发；阳台外窗关闭，通路经开放垭口。
```

计划保存：`projects/另一个家的布布/scene-keyframes/SC04/K04-E0_v01.png`（目前不存在）。

返修：固定人物身份/服装/机位，仅修改失败的边界、姿态、手部承托或遮挡项；不移动家具、不改G/E/X、不为改善技术成功率改剧情。

### K04-E1｜四脚全入G

```text
任务K04-E1：四脚全入G。
单张写实电影关键状态候选，横向16:9，不是最终灯光定稿。严格按PLAN实际家具和开放阳台垭口，G/E/X及机位按已批预演；不抄图纸俯视角、文字、箭头或色块。外窗关闭，地面裸瓷砖，无地毯，阳台无座椅。B世界猫爬架在阳台G外，窝和食水在电视柜与房门之间G外；具体用品造型尚无获批图，执行前需设计候选/空景审核。
出现妻子时以用户已采用C41校准照锁定当前A/B五官，保留棕色低盘发。A只穿wife-A-fullbody浅银灰滚边长袖长裤睡衣、赤脚；B只穿wife-B-fullbody黑色吊带长裙、赤脚。忽略证件图背景与静态微笑，不借用《年复一年》银发老人。出现布布时按bubu-multiview的单只浅奶油短卷毛蓝眼大耳猫，不复制成多猫，不添项圈，不变长毛或无毛猫。猫与人体尺度由候选图交用户审核，不编体重/身高。
候选光线按剧情第八夜夜景：沿现有室内灯具暖光，外窗微弱冷夜与雨痕，脸、猫与接触地面清楚；不沿用白天阳光。具体曝光尚待审核，成对帧沿用前帧获批光线，不擅自加闪电亮帧。禁止文字、水印、多栏拼图、额外人物及漂浮融合肢体。

本帧构图与动作：
从E0通过帧派生，摄影机焦距、家具、灯光不变。布布沿已批路线完整进入G，四脚与尾部均在E室内侧，后脚与边界有可见距离，四脚着地。未上沙发，尚未回应呼唤，A不入画且剧情中仍站在G内。

已有输入文件及职责：
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-001_彩平图_20261025_阳台家具删除版.png：实际家具、墙体和开放阳台垭口，不复制俯视角
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-002_AB世界交汇区标注_V2.2.png：G/E/X行动关系，不沿用旧底图家具
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-01_朝阳台.png：阳台/电视/沙发关系、外窗关闭
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-03_朝沙发.png：新版v02沙发、贵妃位、薄毯、茶几和阳台垭口
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\bubu-multiview.png：同一只浅奶油短卷毛蓝眼大耳猫的侧/正/斜前坐姿，不复制多只猫
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\director\previs-sc04-sc06-v1\SC04_camera-route_v1.png：已批SC04机位与路线，不复制箭头色块

验收：与E0同机位；完整入G，未回应；无穿窗或穿家具。
```

计划保存：`projects/另一个家的布布/scene-keyframes/SC04/K04-E1_v01.png`（目前不存在）。

返修：固定人物身份/服装/机位，仅修改失败的边界、姿态、手部承托或遮挡项；不移动家具、不改G/E/X、不为改善技术成功率改剧情。

### K04-R1｜妻子回应后蹲稳

```text
任务K04-R1：妻子回应后蹲稳。
单张写实电影关键状态候选，横向16:9，不是最终灯光定稿。严格按PLAN实际家具和开放阳台垭口，G/E/X及机位按已批预演；不抄图纸俯视角、文字、箭头或色块。外窗关闭，地面裸瓷砖，无地毯，阳台无座椅。B世界猫爬架在阳台G外，窝和食水在电视柜与房门之间G外；具体用品造型尚无获批图，执行前需设计候选/空景审核。
出现妻子时以用户已采用C41校准照锁定当前A/B五官，保留棕色低盘发。A只穿wife-A-fullbody浅银灰滚边长袖长裤睡衣、赤脚；B只穿wife-B-fullbody黑色吊带长裙、赤脚。忽略证件图背景与静态微笑，不借用《年复一年》银发老人。出现布布时按bubu-multiview的单只浅奶油短卷毛蓝眼大耳猫，不复制成多猫，不添项圈，不变长毛或无毛猫。猫与人体尺度由候选图交用户审核，不编体重/身高。
候选光线按剧情第八夜夜景：沿现有室内灯具暖光，外窗微弱冷夜与雨痕，脸、猫与接触地面清楚；不沿用白天阳光。具体曝光尚待审核，成对帧沿用前帧获批光线，不擅自加闪电亮帧。禁止文字、水印、多栏拼图、额外人物及漂浮融合肢体。

本帧构图与动作：
C41固定中全景朝A，保留沙发端头和地面。A已完成本段唯一一次下蹲，双脚稳定着地，重心落稳，整个落脚范围在G内。双手未抱猫，目光看向G内已经停住并回头的布布。妻子眼眶微湿，不大哭、不夸张张嘴。此低姿持续保持至SC05接触猫。

已有输入文件及职责：
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-001_彩平图_20261025_阳台家具删除版.png：实际家具、墙体和开放阳台垭口，不复制俯视角
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-002_AB世界交汇区标注_V2.2.png：G/E/X行动关系，不沿用旧底图家具
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-03_朝沙发.png：新版v02沙发、贵妃位、薄毯、茶几和阳台垭口
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-identity.png：A/B共同面部身份；忽略蓝背景、白吊带和静态笑容
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-A-fullbody.png：A浅银灰滚边长袖长裤睡衣、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\bubu-multiview.png：同一只浅奶油短卷毛蓝眼大耳猫的侧/正/斜前坐姿，不复制多只猫
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\director\previs-sc04-sc06-v1\SC04_camera-route_v1.png：已批SC04机位与路线，不复制箭头色块

验收：蹲稳而非悬空半蹲；人猫都在G内；回应之后才低身。
```

计划保存：`projects/另一个家的布布/scene-keyframes/SC04/K04-R1_v01.png`（目前不存在）。

返修：固定人物身份/服装/机位，仅修改失败的边界、姿态、手部承托或遮挡项；不移动家具、不改G/E/X、不为改善技术成功率改剧情。

### K05-T0｜同一蹲姿闻手

```text
任务K05-T0：同一蹲姿闻手。
单张写实电影关键状态候选，横向16:9，不是最终灯光定稿。严格按PLAN实际家具和开放阳台垭口，G/E/X及机位按已批预演；不抄图纸俯视角、文字、箭头或色块。外窗关闭，地面裸瓷砖，无地毯，阳台无座椅。B世界猫爬架在阳台G外，窝和食水在电视柜与房门之间G外；具体用品造型尚无获批图，执行前需设计候选/空景审核。
出现妻子时以用户已采用C41校准照锁定当前A/B五官，保留棕色低盘发。A只穿wife-A-fullbody浅银灰滚边长袖长裤睡衣、赤脚；B只穿wife-B-fullbody黑色吊带长裙、赤脚。忽略证件图背景与静态微笑，不借用《年复一年》银发老人。出现布布时按bubu-multiview的单只浅奶油短卷毛蓝眼大耳猫，不复制成多猫，不添项圈，不变长毛或无毛猫。猫与人体尺度由候选图交用户审核，不编体重/身高。
候选光线按剧情第八夜夜景：沿现有室内灯具暖光，外窗微弱冷夜与雨痕，脸、猫与接触地面清楚；不沿用白天阳光。具体曝光尚待审核，成对帧沿用前帧获批光线，不擅自加闪电亮帧。禁止文字、水印、多栏拼图、额外人物及漂浮融合肢体。

本帧构图与动作：
C52固定中全景同时容纳妻子蹲姿、脚和猫，构图预留后续站起头顶空间。A保持R1原位置的同一蹲姿，一手自然松开伸到猫鼻前，另一手不抓猫。猫四脚着地，主动闻手指并轻触，未被提起；桌面不挡鼻尖与手指接近关系。

已有输入文件及职责：
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-001_彩平图_20261025_阳台家具删除版.png：实际家具、墙体和开放阳台垭口，不复制俯视角
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-002_AB世界交汇区标注_V2.2.png：G/E/X行动关系，不沿用旧底图家具
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-03_朝沙发.png：新版v02沙发、贵妃位、薄毯、茶几和阳台垭口
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-identity.png：A/B共同面部身份；忽略蓝背景、白吊带和静态笑容
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-A-fullbody.png：A浅银灰滚边长袖长裤睡衣、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\bubu-multiview.png：同一只浅奶油短卷毛蓝眼大耳猫的侧/正/斜前坐姿，不复制多只猫
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\director\previs-sc04-sc06-v1\SC05_camera-route_v1.png：已批SC05机位与路线，不复制箭头色块

验收：同一蹲姿、原落脚；猫四脚着地主动靠近；手指接触清楚、无抓脖子。
```

计划保存：`projects/另一个家的布布/scene-keyframes/SC05/K05-T0_v01.png`（目前不存在）。

返修：固定人物身份/服装/机位，仅修改失败的边界、姿态、手部承托或遮挡项；不移动家具、不改G/E/X、不为改善技术成功率改剧情。

### K05-H0｜蹲姿已托猫抱稳

```text
任务K05-H0：蹲姿已托猫抱稳。
单张写实电影关键状态候选，横向16:9，不是最终灯光定稿。严格按PLAN实际家具和开放阳台垭口，G/E/X及机位按已批预演；不抄图纸俯视角、文字、箭头或色块。外窗关闭，地面裸瓷砖，无地毯，阳台无座椅。B世界猫爬架在阳台G外，窝和食水在电视柜与房门之间G外；具体用品造型尚无获批图，执行前需设计候选/空景审核。
出现妻子时以用户已采用C41校准照锁定当前A/B五官，保留棕色低盘发。A只穿wife-A-fullbody浅银灰滚边长袖长裤睡衣、赤脚；B只穿wife-B-fullbody黑色吊带长裙、赤脚。忽略证件图背景与静态微笑，不借用《年复一年》银发老人。出现布布时按bubu-multiview的单只浅奶油短卷毛蓝眼大耳猫，不复制成多猫，不添项圈，不变长毛或无毛猫。猫与人体尺度由候选图交用户审核，不编体重/身高。
候选光线按剧情第八夜夜景：沿现有室内灯具暖光，外窗微弱冷夜与雨痕，脸、猫与接触地面清楚；不沿用白天阳光。具体曝光尚待审核，成对帧沿用前帧获批光线，不擅自加闪电亮帧。禁止文字、水印、多栏拼图、额外人物及漂浮融合肢体。

本帧构图与动作：
从T0通过帧派生，机位和A落脚不变。A仍蹲着，一手实际托住猫胸腹、另一手托后躯，猫贴近胸前，身体重量有双点承托，肢体自然收放。猫已离地且抱稳，A尚未起身。不抓项圈、不仅拎前腿，手指与猫腿不融合。

已有输入文件及职责：
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-001_彩平图_20261025_阳台家具删除版.png：实际家具、墙体和开放阳台垭口，不复制俯视角
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-002_AB世界交汇区标注_V2.2.png：G/E/X行动关系，不沿用旧底图家具
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-03_朝沙发.png：新版v02沙发、贵妃位、薄毯、茶几和阳台垭口
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-identity.png：A/B共同面部身份；忽略蓝背景、白吊带和静态笑容
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-A-fullbody.png：A浅银灰滚边长袖长裤睡衣、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\bubu-multiview.png：同一只浅奶油短卷毛蓝眼大耳猫的侧/正/斜前坐姿，不复制多只猫
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\director\previs-sc04-sc06-v1\SC05_camera-route_v1.png：已批SC05机位与路线，不复制箭头色块

验收：先抱稳、尚未起身；胸腹和后躯有支撑；猫尺度交用户审核。
```

计划保存：`projects/另一个家的布布/scene-keyframes/SC05/K05-H0_v01.png`（目前不存在）。

返修：固定人物身份/服装/机位，仅修改失败的边界、姿态、手部承托或遮挡项；不移动家具、不改G/E/X、不为改善技术成功率改剧情。

### K05-H1｜抱稳后站稳

```text
任务K05-H1：抱稳后站稳。
单张写实电影关键状态候选，横向16:9，不是最终灯光定稿。严格按PLAN实际家具和开放阳台垭口，G/E/X及机位按已批预演；不抄图纸俯视角、文字、箭头或色块。外窗关闭，地面裸瓷砖，无地毯，阳台无座椅。B世界猫爬架在阳台G外，窝和食水在电视柜与房门之间G外；具体用品造型尚无获批图，执行前需设计候选/空景审核。
出现妻子时以用户已采用C41校准照锁定当前A/B五官，保留棕色低盘发。A只穿wife-A-fullbody浅银灰滚边长袖长裤睡衣、赤脚；B只穿wife-B-fullbody黑色吊带长裙、赤脚。忽略证件图背景与静态微笑，不借用《年复一年》银发老人。出现布布时按bubu-multiview的单只浅奶油短卷毛蓝眼大耳猫，不复制成多猫，不添项圈，不变长毛或无毛猫。猫与人体尺度由候选图交用户审核，不编体重/身高。
候选光线按剧情第八夜夜景：沿现有室内灯具暖光，外窗微弱冷夜与雨痕，脸、猫与接触地面清楚；不沿用白天阳光。具体曝光尚待审核，成对帧沿用前帧获批光线，不擅自加闪电亮帧。禁止文字、水印、多栏拼图、额外人物及漂浮融合肢体。

本帧构图与动作：
从H0通过帧编辑派生，摄影机固定，不随人物升高、不推近。A由原蹲姿抱猫起身，仍在G内原位站稳，头到脚均在画面中，双脚着地，双手沿用H0实际承托手位，猫与身体贴合及朝向连续。没有额外步行，猫未跳回地面。

已有输入文件及职责：
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-001_彩平图_20261025_阳台家具删除版.png：实际家具、墙体和开放阳台垭口，不复制俯视角
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-002_AB世界交汇区标注_V2.2.png：G/E/X行动关系，不沿用旧底图家具
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-03_朝沙发.png：新版v02沙发、贵妃位、薄毯、茶几和阳台垭口
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-identity.png：A/B共同面部身份；忽略蓝背景、白吊带和静态笑容
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-A-fullbody.png：A浅银灰滚边长袖长裤睡衣、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\bubu-multiview.png：同一只浅奶油短卷毛蓝眼大耳猫的侧/正/斜前坐姿，不复制多只猫
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\director\previs-sc04-sc06-v1\SC05_camera-route_v1.png：已批SC05机位与路线，不复制箭头色块

验收：同机位无裁头；猫手位与朝向接H0；A站稳在G内，接SC06。
```

计划保存：`projects/另一个家的布布/scene-keyframes/SC05/K05-H1_v01.png`（目前不存在）。

返修：固定人物身份/服装/机位，仅修改失败的边界、姿态、手部承托或遮挡项；不移动家具、不改G/E/X、不为改善技术成功率改剧情。

### K06-O0｜客观双妻子关系

```text
任务K06-O0：客观双妻子关系。
单张写实电影关键状态候选，横向16:9，不是最终灯光定稿。严格按PLAN实际家具和开放阳台垭口，G/E/X及机位按已批预演；不抄图纸俯视角、文字、箭头或色块。外窗关闭，地面裸瓷砖，无地毯，阳台无座椅。B世界猫爬架在阳台G外，窝和食水在电视柜与房门之间G外；具体用品造型尚无获批图，执行前需设计候选/空景审核。
出现妻子时以用户已采用C41校准照锁定当前A/B五官，保留棕色低盘发。A只穿wife-A-fullbody浅银灰滚边长袖长裤睡衣、赤脚；B只穿wife-B-fullbody黑色吊带长裙、赤脚。忽略证件图背景与静态微笑，不借用《年复一年》银发老人。出现布布时按bubu-multiview的单只浅奶油短卷毛蓝眼大耳猫，不复制成多猫，不添项圈，不变长毛或无毛猫。猫与人体尺度由候选图交用户审核，不编体重/身高。
候选光线按剧情第八夜夜景：沿现有室内灯具暖光，外窗微弱冷夜与雨痕，脸、猫与接触地面清楚；不沿用白天阳光。具体曝光尚待审核，成对帧沿用前帧获批光线，不擅自加闪电亮帧。禁止文字、水印、多栏拼图、额外人物及漂浮融合肢体。

本帧构图与动作：
C61固定中全景斜看餐厨。前景G内A按H1站姿抱同一只布布，后景G外B从厨房走出、在餐厨通道停稳向沙发家具区寻找。两位妻子同一面部身份和发型，但A浅银睡衣、B黑裙。B不看A眼睛，不回应A。恰好两位女性与一只猫，没有丈夫。茶几花瓶不遮关键面部及抱猫承托。

已有输入文件及职责：
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-001_彩平图_20261025_阳台家具删除版.png：实际家具、墙体和开放阳台垭口，不复制俯视角
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-002_AB世界交汇区标注_V2.2.png：G/E/X行动关系，不沿用旧底图家具
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-03_朝沙发.png：新版v02沙发、贵妃位、薄毯、茶几和阳台垭口
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-02_朝厨房.jpg：餐厨外围
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-identity.png：A/B共同面部身份；忽略蓝背景、白吊带和静态笑容
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-A-fullbody.png：A浅银灰滚边长袖长裤睡衣、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-B-fullbody.png：B黑色细吊带长裙、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-B-three-views.png：侧背面轮廓、盘发；黑裙仅供B，不抄文字版式
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\bubu-multiview.png：同一只浅奶油短卷毛蓝眼大耳猫的侧/正/斜前坐姿，不复制多只猫
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\director\previs-sc04-sc06-v1\SC06_camera-route_v1.png：已批SC06机位与路线，不复制箭头色块

验收：同脸不同衣，恰好两女一猫；A猫在G内，B在G外；无互相对视互动。
```

计划保存：`projects/另一个家的布布/scene-keyframes/SC06/K06-O0_v01.png`（目前不存在）。

返修：固定人物身份/服装/机位，仅修改失败的边界、姿态、手部承托或遮挡项；不移动家具、不改G/E/X、不为改善技术成功率改剧情。

### K06-P0｜B真实眼位空镜

```text
任务K06-P0：B真实眼位空镜。
单张写实电影关键状态候选，横向16:9，不是最终灯光定稿。严格按PLAN实际家具和开放阳台垭口，G/E/X及机位按已批预演；不抄图纸俯视角、文字、箭头或色块。外窗关闭，地面裸瓷砖，无地毯，阳台无座椅。B世界猫爬架在阳台G外，窝和食水在电视柜与房门之间G外；具体用品造型尚无获批图，执行前需设计候选/空景审核。
出现妻子时以用户已采用C41校准照锁定当前A/B五官，保留棕色低盘发。A只穿wife-A-fullbody浅银灰滚边长袖长裤睡衣、赤脚；B只穿wife-B-fullbody黑色吊带长裙、赤脚。忽略证件图背景与静态微笑，不借用《年复一年》银发老人。出现布布时按bubu-multiview的单只浅奶油短卷毛蓝眼大耳猫，不复制成多猫，不添项圈，不变长毛或无毛猫。猫与人体尺度由候选图交用户审核，不编体重/身高。
候选光线按剧情第八夜夜景：沿现有室内灯具暖光，外窗微弱冷夜与雨痕，脸、猫与接触地面清楚；不沿用白天阳光。具体曝光尚待审核，成对帧沿用前帧获批光线，不擅自加闪电亮帧。禁止文字、水印、多栏拼图、额外人物及漂浮融合肢体。

本帧构图与动作：
摄影机必须在O0中B实际站立眼位C62，向A刚才站立的沙发区域拍摄。家具、地砖、薄毯、茶几均与同一时刻一致，G内不见A妻子与布布，B自己也不入画。不使用C61原位直接删人，不使人物不可见时家具也消失，无半透明鬼影。

已有输入文件及职责：
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-001_彩平图_20261025_阳台家具删除版.png：实际家具、墙体和开放阳台垭口，不复制俯视角
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-002_AB世界交汇区标注_V2.2.png：G/E/X行动关系，不沿用旧底图家具
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-03_朝沙发.png：新版v02沙发、贵妃位、薄毯、茶几和阳台垭口
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-01_朝阳台.png：阳台/电视/沙发关系、外窗关闭
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\director\previs-sc04-sc06-v1\SC06_camera-route_v1.png：已批SC06机位与路线，不复制箭头色块

验收：镜头来自B眼位，非C61删人；人猫不可见但家具保持；不画穿界特效。
```

计划保存：`projects/另一个家的布布/scene-keyframes/SC06/K06-P0_v01.png`（目前不存在）。

返修：固定人物身份/服装/机位，仅修改失败的边界、姿态、手部承托或遮挡项；不移动家具、不改G/E/X、不为改善技术成功率改剧情。

### K06-X0｜猫仍G内，手已放开

```text
任务K06-X0：猫仍G内，手已放开。
单张写实电影关键状态候选，横向16:9，不是最终灯光定稿。严格按PLAN实际家具和开放阳台垭口，G/E/X及机位按已批预演；不抄图纸俯视角、文字、箭头或色块。外窗关闭，地面裸瓷砖，无地毯，阳台无座椅。B世界猫爬架在阳台G外，窝和食水在电视柜与房门之间G外；具体用品造型尚无获批图，执行前需设计候选/空景审核。
出现妻子时以用户已采用C41校准照锁定当前A/B五官，保留棕色低盘发。A只穿wife-A-fullbody浅银灰滚边长袖长裤睡衣、赤脚；B只穿wife-B-fullbody黑色吊带长裙、赤脚。忽略证件图背景与静态微笑，不借用《年复一年》银发老人。出现布布时按bubu-multiview的单只浅奶油短卷毛蓝眼大耳猫，不复制成多猫，不添项圈，不变长毛或无毛猫。猫与人体尺度由候选图交用户审核，不编体重/身高。
候选光线按剧情第八夜夜景：沿现有室内灯具暖光，外窗微弱冷夜与雨痕，脸、猫与接触地面清楚；不沿用白天阳光。具体曝光尚待审核，成对帧沿用前帧获批光线，不擅自加闪电亮帧。禁止文字、水印、多栏拼图、额外人物及漂浮融合肢体。

本帧构图与动作：
C63固定较宽低位，保留X两侧地面、A落脚与B所在G外方向。A在G内原位再次蹲下，已将猫放稳裸砖，双手收回不再碰猫。猫四脚着地且完整仍在G内，朝餐厨侧X。B在G外寻找，尚未看见或碰到猫。

已有输入文件及职责：
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-001_彩平图_20261025_阳台家具删除版.png：实际家具、墙体和开放阳台垭口，不复制俯视角
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-002_AB世界交汇区标注_V2.2.png：G/E/X行动关系，不沿用旧底图家具
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-03_朝沙发.png：新版v02沙发、贵妃位、薄毯、茶几和阳台垭口
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-identity.png：A/B共同面部身份；忽略蓝背景、白吊带和静态笑容
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-A-fullbody.png：A浅银灰滚边长袖长裤睡衣、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-B-fullbody.png：B黑色细吊带长裙、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\bubu-multiview.png：同一只浅奶油短卷毛蓝眼大耳猫的侧/正/斜前坐姿，不复制多只猫
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\director\previs-sc04-sc06-v1\SC06_camera-route_v1.png：已批SC06机位与路线，不复制箭头色块

验收：这是放猫的独立第二次下蹲；猫已落地，双手已松；猫未出X，B未触猫。
```

计划保存：`projects/另一个家的布布/scene-keyframes/SC06/K06-X0_v01.png`（目前不存在）。

返修：固定人物身份/服装/机位，仅修改失败的边界、姿态、手部承托或遮挡项；不移动家具、不改G/E/X、不为改善技术成功率改剧情。

### K06-X1｜猫四脚全出X

```text
任务K06-X1：猫四脚全出X。
单张写实电影关键状态候选，横向16:9，不是最终灯光定稿。严格按PLAN实际家具和开放阳台垭口，G/E/X及机位按已批预演；不抄图纸俯视角、文字、箭头或色块。外窗关闭，地面裸瓷砖，无地毯，阳台无座椅。B世界猫爬架在阳台G外，窝和食水在电视柜与房门之间G外；具体用品造型尚无获批图，执行前需设计候选/空景审核。
出现妻子时以用户已采用C41校准照锁定当前A/B五官，保留棕色低盘发。A只穿wife-A-fullbody浅银灰滚边长袖长裤睡衣、赤脚；B只穿wife-B-fullbody黑色吊带长裙、赤脚。忽略证件图背景与静态微笑，不借用《年复一年》银发老人。出现布布时按bubu-multiview的单只浅奶油短卷毛蓝眼大耳猫，不复制成多猫，不添项圈，不变长毛或无毛猫。猫与人体尺度由候选图交用户审核，不编体重/身高。
候选光线按剧情第八夜夜景：沿现有室内灯具暖光，外窗微弱冷夜与雨痕，脸、猫与接触地面清楚；不沿用白天阳光。具体曝光尚待审核，成对帧沿用前帧获批光线，不擅自加闪电亮帧。禁止文字、水印、多栏拼图、额外人物及漂浮融合肢体。

本帧构图与动作：
从X0通过帧派生，同机位、焦距、家具、光线。猫沿茶几餐厨侧地面走出X，四脚、尾部和完整身体全部在G外，不只是前脚越线。A留在G内原位低姿、双手空，不追。B在G外开始转头自然注意到猫，尚未抱起。不让猫闪现或从家具中长出。

已有输入文件及职责：
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-001_彩平图_20261025_阳台家具删除版.png：实际家具、墙体和开放阳台垭口，不复制俯视角
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-002_AB世界交汇区标注_V2.2.png：G/E/X行动关系，不沿用旧底图家具
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-03_朝沙发.png：新版v02沙发、贵妃位、薄毯、茶几和阳台垭口
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-identity.png：A/B共同面部身份；忽略蓝背景、白吊带和静态笑容
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-A-fullbody.png：A浅银灰滚边长袖长裤睡衣、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-B-fullbody.png：B黑色细吊带长裙、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\bubu-multiview.png：同一只浅奶油短卷毛蓝眼大耳猫的侧/正/斜前坐姿，不复制多只猫
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\director\previs-sc04-sc06-v1\SC06_camera-route_v1.png：已批SC06机位与路线，不复制箭头色块

验收：猫完整在G外；A未出G；B在猫出来后才注意到。
```

计划保存：`projects/另一个家的布布/scene-keyframes/SC06/K06-X1_v01.png`（目前不存在）。

返修：固定人物身份/服装/机位，仅修改失败的边界、姿态、手部承托或遮挡项；不移动家具、不改G/E/X、不为改善技术成功率改剧情。

### K06-B0｜B在G外已抱回

```text
任务K06-B0：B在G外已抱回。
单张写实电影关键状态候选，横向16:9，不是最终灯光定稿。严格按PLAN实际家具和开放阳台垭口，G/E/X及机位按已批预演；不抄图纸俯视角、文字、箭头或色块。外窗关闭，地面裸瓷砖，无地毯，阳台无座椅。B世界猫爬架在阳台G外，窝和食水在电视柜与房门之间G外；具体用品造型尚无获批图，执行前需设计候选/空景审核。
出现妻子时以用户已采用C41校准照锁定当前A/B五官，保留棕色低盘发。A只穿wife-A-fullbody浅银灰滚边长袖长裤睡衣、赤脚；B只穿wife-B-fullbody黑色吊带长裙、赤脚。忽略证件图背景与静态微笑，不借用《年复一年》银发老人。出现布布时按bubu-multiview的单只浅奶油短卷毛蓝眼大耳猫，不复制成多猫，不添项圈，不变长毛或无毛猫。猫与人体尺度由候选图交用户审核，不编体重/身高。
候选光线按剧情第八夜夜景：沿现有室内灯具暖光，外窗微弱冷夜与雨痕，脸、猫与接触地面清楚；不沿用白天阳光。具体曝光尚待审核，成对帧沿用前帧获批光线，不擅自加闪电亮帧。禁止文字、水印、多栏拼图、额外人物及漂浮融合肢体。

本帧构图与动作：
从X1通过帧派生，固定同一空间。B在G外接回点自然蹲下，一手托猫胸腹、另一手托后躯，抱稳同一只猫贴近自己，表情只是找到猫后的放松；不看A、不表现知晓交汇。A仍G内低姿且双手空，没有追出。B和猫的承托位置完全在G外。B世界外围仍存在，交汇尚未关闭。

已有输入文件及职责：
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-001_彩平图_20261025_阳台家具删除版.png：实际家具、墙体和开放阳台垭口，不复制俯视角
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\space\PLAN-002_AB世界交汇区标注_V2.2.png：G/E/X行动关系，不沿用旧底图家具
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\views\VIEW-03_朝沙发.png：新版v02沙发、贵妃位、薄毯、茶几和阳台垭口
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-identity.png：A/B共同面部身份；忽略蓝背景、白吊带和静态笑容
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-A-fullbody.png：A浅银灰滚边长袖长裤睡衣、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-B-fullbody.png：B黑色细吊带长裙、赤脚与身材比例
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\wife-B-three-views.png：侧背面轮廓、盘发；黑裙仅供B，不抄文字版式
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\assets\characters\bubu-multiview.png：同一只浅奶油短卷毛蓝眼大耳猫的侧/正/斜前坐姿，不复制多只猫
D:\Codex\2026-10-20\codex-agent-memory\work\github-agent-memory-20261020\projects\另一个家的布布\director\previs-sc04-sc06-v1\SC06_camera-route_v1.png：已批SC06机位与路线，不复制箭头色块

验收：B猫在G外并承托稳定；A仍G内空手；B不知情，抱回先于关闭。
```

计划保存：`projects/另一个家的布布/scene-keyframes/SC06/K06-B0_v01.png`（目前不存在）。

返修：固定人物身份/服装/机位，仅修改失败的边界、姿态、手部承托或遮挡项；不移动家具、不改G/E/X、不为改善技术成功率改剧情。

## A/B任务及交接边界

- A类真实素材：人物、衣装和布布8张已找到，无需用户重复提供。猫未有背面/站姿，A未有单独三视图，均不先强制补；若具体帧失败，再提出所需角度。猫真实大小未知，首次托猫帧交用户确认比例。
- B类导演设计：夜景空景、G外猫用品造型、11个状态帧的构图、姿态、视线和承托由Codex设计；用户如按提示词操作生成，不承担补导演方案的责任。
- 丈夫3张已登记，但不因此把他放进本轮双妻子画面；SC06交汇结束后的丈夫进入镜头另列。
- 旧相框合照原件尚未发现，不阻断本轮，SC01/02/07再核对；不得AI虚构真实旧合照。
- 执行路径：E外首张兼核夜景/可见用品→E内→妻子蹲稳→闻手/蹲姿托稳/抱稳站立→客观双妻子/B主观空镜→X内松手/X外全身/B接回。通过一项才解锁依赖，失败另存版本；没有生成图片或视频，不因任务文件存在标为已制作。

## K04-E0首轮实际候选（2026-10-25）

[候选与实图审查](../../scene-keyframes/SC04/K04-E0/README.md)已完成单张v01生成与门槛定向修正v02，待用户审核。上文“11张均未生成”为任务准备时快照；当前仅K04-E0已有候选，余10状态未生成，K04-E1仍等E0批准。

## 最新约束：女主穿实际参考拖鞋

用户将提供实际拖鞋，不由Codex另选。原图和历史提示词中赤脚描述只供追溯；执行以[鞋款规则](../../assets/characters/footwear-decision_20261025.json)为准。R1已生成赤脚v01/v02，均需局部补鞋，不合格；人物任务等待实际鞋参考。E0/E1无人帧不受影响。

## 实际鞋款接收与派生更新

用户已提供A粉色打孔厚底拖、B黑色夹脚拖，[原图及成果](../../assets/characters/footwear/README.md)已登记。B全身/B三视/R1 v03已补鞋待审；A全身编辑调用被服务拒绝，尚无合成图。无需等待用户重做人像，后续以原A衣装图+真实A鞋图双参考。旧“待提供实际鞋图”不再是当前阻断项。

## 与远端新剧情的边界

本轮已保留合并远端[PLAN-002/PLAN-003差异核对](../../space/PLAN-002与PLAN-003动线差异核对_V1_20261026.md)。SC06新增23:27抱猫出G/23:28返G不由本次补鞋修改，本11状态尚未覆盖这两个新接口，不能直接当作最新SC06完整执行表；后续制作SC06前须同步新剧本和增补任务。SC04的R1补鞋不改变原已批路线。

## 当前面部参考已更新

用户已采用[C41校准照五官](../../assets/characters/identity-calibration-C41/README.md)。执行应读取 `prompts/` 最新单任务文件，其中已移除原特写作为混合输入的旧行；本页早期提示词快照如有旧身份主图描述，以[当前执行映射](../../assets/characters/current-face-reference.json)和单任务新稿为准。R1 v06仍为回填候选，未自动通过。
