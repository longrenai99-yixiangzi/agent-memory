# 《年复一年》｜Seedance 2.5 Skills 安装登记与双模型提示词工作流

- **日期：** 2026-10-22
- **来源：** 用户在 Windows 11 PowerShell 中实际执行下载、复制和检查命令并提供终端截图；ChatGPT 依据截图登记
- **记录状态：** 三个 Skill 的 `SKILL.md` 文件检查均为 `True`（安装文件存在）；Codex 识别/调用、Skill 内容与相互兼容性尚未验证
- **用途：** 供 ChatGPT、Codex 接续《年复一年》视频制作及提示词规范整合
- **审批界限：** 仅记录工具部署与流程方向，不批准任何 Scene01 新机位、镜头时长、提示词版本或视频成片

## 一、实际 Codex 环境

- 操作系统：Windows 11，PowerShell
- 实际环境变量：`CODEX_HOME=D:\AI_ENV\Codex\home`
- Skill 安装根目录：`D:\AI_ENV\Codex\home\skills\`
- 用户电脑上仍存在旧的 C 盘 Codex 配置文件；本次安装以 `CODEX_HOME` 为准，**没有修改或清理 C 盘旧配置**。
- 未修改 ComfyUI、本地 H3 工作流，也未安装/下载新视频模型。

## 二、三个 Skill 的实际登记

| Skill / 仓库 | 本地安装路径（相对 CODEX_HOME） | 目标用途 | 安装文件核验 | 运行验证 |
| --- | --- | --- | --- | --- |
| [Seedance 2.5 Director](https://github.com/sjinn-ai/seedance2.5-skills) | `skills/seedance-25/SKILL.md` | 导演统筹、参考素材、镜头连续性及失败修复 | `True` | **待测** |
| [Seedance Shot Design](https://github.com/woodfantasy/Seedance-ShotDesign-Skills) | `skills/seedance-shot-design/SKILL.md` | 分镜、运镜、表演、光影和镜头诊断 | `True` | **待测** |
| [Seedance 2.5 Prompt Skill](https://github.com/xiaoliangliang/seedance-2.5-prompt-skill) | `skills/seedance-2-5/SKILL.md` | 中文视频提示词、时间轴、多模态引用 | `True` | **待测** |

用户最终一次 PowerShell 检查输出：

```text
Skill                 Installed
-----                 ---------
seedance-25                True
seedance-shot-design       True
seedance-2-5               True
```

**证据级别：** 上述仅能确认本机指定路径存在 `SKILL.md`；**不能据此声称 Codex 已识别、Skill 已实际加载、内容无冲突或生成效果合格**。三个仓库为第三方社区 Skills，正式启用前需核查其指令及脚本，不自动执行不明脚本。

## 三、已确认的双模型提示词制作方向

用户已接受：**同一镜头只保留一份统一导演设计稿，再按模型分别输出 Seedance 2.5 与 MiniMax H3 提示词**，不得直接把一份提示词无差别用于两个模型。

1. **统一导演设计：** 镜头叙事目的、情绪与表演、人物/道具动作因果、摄影机起止与运动、光影、参考资产职责、首尾状态、剪辑接口、验收标准。先确认导演逻辑，再转译至模型。
2. **Seedance 2.5：** 中文导演叙事式提示词；明确生成方式、`@图片/@视频` 角色、时间段动作、机位运镜、表演、视听及空间/身份连续性。应依实际平台和模型能力适配，不保证时间戳逐帧执行。
3. **本地 H3：** 保留现有 H3 专用工作流与英文动作执行提示词；优先描述清晰的起点、一个主要动作、可观察的物理过程、摄影机控制和终点约束；首尾帧/参考视频绑定必须对照实际 ComfyUI 节点。
4. **版本分离：** `SC01-P02-DIRECTOR-Vn`、`SC01-P02-SEEDANCE25-Vn`、`SC01-P02-H3-Vn` 和单独视频验收版本。修改某模型的提示词不自动批准另一模型或更改导演设计。
5. **权责与审批：** 继承 [导演决策与审批规则](导演决策与审批规则.md)。用户为最终导演；Skill 输出、ChatGPT 审核、Codex 技术校验均不自动批准创作变更。

这是**工作流方向已确认**，不表示三份正式规范文件已经完成或经 Codex 实测。

## 四、额度恢复后的待办测试（非已执行）

- [ ] 重启/刷新 Codex 客户端，验证它是否发现 `seedance-25`、`seedance-shot-design`、`seedance-2-5`，记录实际调用名称；不要仅凭 `SKILL.md` 存在判定成功。
- [ ] 只读检查三个 `SKILL.md`、附属脚本与依赖，排查互相覆盖的指令、未经授权外部操作或额外安装需求。
- [ ] 从现有 [Scene01 P02 导演设计稿](scene01/Scene01_P02_20261022_首帧与运镜导演设计稿_V1.md) 读取已批准和待审部分，以 **SC01-P02** 为同一对比输入；不得把候选机位或首尾帧直接记为已批准。
- [ ] **单独**调用三个 Skill，让每个生成参考素材绑定、动作时间线、机位运镜、起止姿势和 Seedance 2.5 中文提示词；不直接生成付费视频。
- [ ] 比较动作因果、空间拓扑、人物一致性、可剪辑性和提示词可执行性。主 Skill 及吸收其它规则的方式在测试后再确定，不预设哪一个表现最好。
- [ ] 编写并确认正式的 `director-standard.md`、`seedance-2.5-prompt-standard.md`、`h3-prompt-standard.md`（仅作为**拟建文件**，目前未创建），沿用已验证 H3 规范，不覆盖已有内容。
- [ ] 通过用户明确审批后，才以双模型方案对指定镜头开展生成、实际片段对比和剪辑验收。

## 五、当前状态与接续提示

**当前：三个 Skill 文件已安装；Codex 无可用额度，用户安排之后集中测试；运行测试、跨 Skill 兼容性及生成质量均未验证。** 这是一项完整任务清单，不建立每日截止时间，也不创建自动提醒。

下次继续时：先读 `AGENTS.md` → `INDEX.md` → [项目当前状态](current-state.md) → 本记录及 Scene01 相应导演设计；不能因安装新 Skill 就推翻已确认的 P01/C01/C02 镜头和资产决定。
