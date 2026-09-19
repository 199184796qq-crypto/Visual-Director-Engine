# VDE｜Visual Director Engine

## AI 视觉导演引擎 v1.0

VDE 是一套面向 AI 图像、视频和影视项目的视觉设计 Agent 基础系统。

它把用户的文字需求、参考图片和项目规范，整理为可执行的视觉方案与模型提示词。VDE 关注的不只是“写一段 prompt”，还包括人物连续性、风格选择、摄影、构图、光影、色彩、材质和质量检查。

## 系统能力

```text
用户需求 / 参考图
        ↓
输入分析
        ↓
视觉方向设计
        ↓
人物与场景设计
        ↓
摄影、构图、光影、色彩设计
        ↓
Universal Visual Prompt
        ↓
模型适配
        ↓
质量检查
```

VDE 目前包含：

- `skill.md`：VDE 的角色、原则和输出格式
- `core/workflow.md`：从输入到最终提示词的执行流程
- `knowledge/visual_styles/`：14 种电影视觉风格知识库
- `knowledge/character/`：Character Bible 和 84 条人物参考资产
- `knowledge/project/`：项目级视觉圣经
- `knowledge/camera/`：摄影语言
- `knowledge/lighting/`：光影语言
- `knowledge/color/`：色彩规则
- `knowledge/composition/`：构图规则
- `knowledge/reference/`：参考图视觉 DNA 分析
- `knowledge/negative/`：常见视觉错误和冲突
- `knowledge/adapter/`：Midjourney、SDXL、Flux、即梦、H3 等模型适配
- `evaluation/`：提示词质量评估

## 最简单的使用方式

单张参考图可以直接上传给 AI，不需要先建目录。上传图片后，使用简化指令：

```text
VDE看图：提取这张图的视觉DNA，并生成可复用的提示词。
```

把参考图改成新画面：

```text
VDE借风格：不要复制原图人物和具体物体，只借鉴视觉语言；为一个雨夜石桥侠客生成即梦提示词。
```

锁定人物并生成连续镜头：

```text
VDE锁人物：保持图中人物的脸、发型、体型和服装特征，让他出现在雪夜客栈门口，输出 H3 提示词。
```

完整简化指令见 [`QUICK_COMMANDS.md`](QUICK_COMMANDS.md)。

## 作为 Agent 使用

将以下文件作为系统指令和知识库提供给 AI：

1. `skill.md`
2. `core/workflow.md`
3. 与任务相关的知识库文件
4. 项目任务中的 `project_bible.md` 和 `character_bible.md`

之后可以这样发起任务：

```text
你现在是 VDE Visual Director Engine。
请读取 VDE 的 skill.md 和 workflow.md，按完整流程处理下面需求。
先做视觉分析和视觉方案，再输出目标模型提示词。

需求：一个雨夜山城中的孤独侠客，输出即梦提示词。
```

## 人物圣经

`knowledge/character/character_bible.md` 用于固定角色的身份、外貌、服装、标志道具、动作习惯和剧情状态。

人物参考资产在：

- `knowledge/character/character_library.json`
- `knowledge/character/character_library.md`

库中 84 条人物描述来自原始 14 风格测试资料，属于参考资产，不等同于已批准的项目角色。正式项目需要建立自己的角色记录并标记状态。

## 视觉风格库

正式入口：

- `knowledge/visual_styles/style_library.md`
- `knowledge/visual_styles/style_library_vde.json`

原始研究资料逐字保留在 `knowledge/visual_styles/style_library_source.md`。转换脚本位于 `tools/convert_style_library.py`，核验结果位于 `knowledge/visual_styles/conversion_report.md`。

## 设计原则

- 先理解，再生成。
- 用户要求优先于项目规范，项目规范优先于参考图，参考图优先于风格库默认规则。
- 风格库提供视觉语言，不自动覆盖人物身份。
- 参考图提取稳定规律，不复制偶然物体、文字和背景噪声。
- 来源不支持的字段留空或放入独立的 `enrichment`，不伪装成原始事实。

## 当前状态

这是一个 Agent 知识与规则系统，可接入 ChatGPT、Claude、Codex、本地模型或图像/视频生成模型。仓库本身不直接生成图片或视频；它负责视觉分析、规范管理和模型提示词生成。


================================================

# Overview


VDE（Visual Director Engine）

是一个面向 AI 图像生成的视觉导演系统。


它不是 Prompt Generator。


它模拟：

- 导演
- 美术指导
- 摄影指导
- 视觉设计师


将用户模糊想法转换为：

专业视觉方案

↓

模型可执行 Prompt



================================================

# Core Philosophy


传统流程：


用户一句话

↓

关键词堆叠

↓

生成图片



VDE流程：


用户想法

↓

视觉理解

↓

美术设计

↓

摄影设计

↓

风格设计

↓

Prompt生成

↓

模型适配

↓

质量审核



================================================

# System Architecture


================================================

# Visual Style Knowledge Base

正式风格库入口：

`knowledge/visual_styles/style_library.md`

机器调用入口：

`knowledge/visual_styles/style_library_vde.json`

原始研究资料：

`knowledge/visual_styles/style_library_source.md`

转换脚本：

`tools/convert_style_library.py`

转换报告：

`knowledge/visual_styles/conversion_report.md`

## 调用规则

1. 先按题材、时代、情绪、场景和用途筛选风格。
2. 按 `style_id` 读取 JSON；组合 `prompt_keywords.style` 与任务所需的 `prompt_keywords.content`。
3. `asset_examples` 是人物与道具测试素材，不是默认风格规则。
4. `source_mixed_texture_tonality` 是原文完整短语；分类字段只用于检索，不覆盖原文。
5. 空字段表示来源没有可靠证据。不得把旧的艺术家风格清单或模型常识写回来源字段。
6. 若要补充 `best_for`、情绪、器材、英文提示词等，写入独立 `enrichment`，附依据和审核状态。

旧版泛化风格清单保留在 `knowledge/visual_styles/style_library_legacy.md`，仅用于兼容旧项目引用。

# Character Bible

人物连续性规范：`knowledge/character/character_bible.md`

人物参考资产索引：`knowledge/character/character_library.json`

人物可读清单：`knowledge/character/character_library.md`

人物库目前收录来源中的 14 个风格、每风格 6 条角色描述，共 84 条。它们属于参考资产，不能直接当作某个项目的正式角色；正式项目应复制角色记录，补齐 `identity`、`appearance`、`wardrobe`、`signature`、`performance` 和 `story_state`，然后标记 `approved`。

日常使用的简化指令见 `QUICK_COMMANDS.md`。单张图可以直接上传给 AI；只有需要长期复用、多人协作或连续镜头时，才需要保存到项目目录。

## 与 AI 视频项目框架协同

VDE 是视觉设计层，可与 E:\H3的技能 协同：VDE 负责视觉 DNA、色卡、人物圣经和场景规范；AI 视频项目框架负责项目状态、素材、分镜、模型提示词、续写和归档。H3、Wan3、Seedance 是模型分支，不是项目名称。详见 integrations/ai_video_project_bridge.md。

