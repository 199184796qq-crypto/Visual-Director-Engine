# VDE Reference Analysis Library
# 参考图视觉分析引擎 v1.0


================================================

# 核心目标


当用户提供图片时：

不要简单描述图片内容。


需要回答：

1. 这张图为什么有这种视觉效果？
2. 使用了什么摄影语言？
3. 使用了什么美术语言？
4. 哪些元素决定了它的风格？
5. 如何转换成 AI 图像 Prompt？


输出：

Reference Visual DNA


================================================

# Module 01
# Single Image Analysis
# 单图分析


分析顺序：


Image
 ↓
Content Layer
 ↓
Visual Layer
 ↓
Technical Layer
 ↓
Style Layer
 ↓
Prompt Layer



================================================

# 01 Content Layer
# 内容分析


## Subject


分析：

- 人物/物体身份
- 年龄
- 性别
- 外貌
- 服装
- 道具


输出：

Example:


Subject:

A middle-aged Chinese warrior.

Appearance:

weathered face,
dark traditional clothing,
rough texture.


------------------------------------------------


## Action


分析：

- 动作
- 姿态
- 方向
- 情绪


不要只写：

standing


需要：

standing still,
slightly lowered head,
quiet and restrained posture



------------------------------------------------


## Environment


分析：

空间：

- 室内
- 室外
- 城市
- 自然
- 建筑


环境作用：

不是列物体。

需要分析：

环境如何服务主体。


Example:


不是：

old street


而是：

narrow historical alley creating a sense of isolation



================================================

# 02 Visual Layer
# 视觉语言分析


## Composition DNA


分析：


主体位置：

- center
- left third
- right third


空间：

- negative space
- layered depth
- foreground framing


Example:


Composition:

centered character,
large empty background,
strong visual balance



------------------------------------------------


## Perspective DNA


分析：

摄影视角。


包括：

Eye level:

平等、真实


Low angle:

力量


High angle:

弱小


Top view:

空间关系


------------------------------------------------


## Depth DNA


分析：

空间层次。


包括：

Foreground

Middle ground

Background


输出：

Layered cinematic composition



================================================

# 03 Camera DNA
# 摄影分析


分析：


## Lens Estimation


判断：


24mm:

空间夸张


35mm:

电影叙事


50mm:

自然视觉


85mm:

人物情绪


Macro:

细节


输出：


Estimated camera:

35mm cinematic lens



------------------------------------------------


## Camera Body Style


根据质感判断：

电影：

ARRI Alexa style


商业：

Hasselblad style


人文：

Leica style


胶片：

35mm film photography



================================================

# 04 Lighting DNA
# 光影分析


分析：

## Light Direction


例如：

soft light from left side


## Light Quality


判断：

hard light

soft light

diffused light


## Shadow


分析：

high contrast

low key

soft shadow



输出：


Lighting:

soft directional sunlight,
gentle shadows,
cinematic atmosphere



================================================

# 05 Color DNA
# 色彩分析


分析：


## Dominant Color


主色。


## Supporting Color


辅助色。


## Accent Color


强调色。


## Saturation


判断：

high saturation

muted colors

desaturated


## Temperature


warm

cold

mixed



输出：


Color:

muted blue-gray palette,
warm highlights



================================================

# 06 Material DNA
# 材质分析


分析：

人物：

- skin
- hair
- fabric


环境：

- wood
- stone
- metal


输出：


Material:

realistic skin texture,
weathered fabric,
aged surfaces



================================================

# 07 Emotion DNA
# 情绪分析


图片最重要。


分析：


视觉情绪：

- lonely
- peaceful
- tense
- luxurious
- mysterious
- heroic


不要使用：

beautiful


使用：

specific emotion



================================================


# Module 02
# Multi Image Style Extraction


多张图片输入。


目标：

提取共同视觉语言。


流程：


Image 1
Image 2
Image 3

↓

Individual Analysis

↓

Find Common Features

↓

Remove Accidental Elements

↓

Generate Style Bible



================================================

# Common Feature Extraction


寻找：


## Camera Commonality


例如：

所有图片：

35mm lens

shallow depth of field



## Color Commonality


例如：

所有图片：

cold blue-gray palette



## Lighting Commonality


例如：

soft natural light



## Composition Commonality


例如：

minimalist framing



## Emotional Commonality


例如：

quiet melancholy



================================================

# Style Bible Output Format


# VISUAL STYLE BIBLE


## Visual Identity


一句话总结。



Example:


Realistic cinematic photography with cold minimalist atmosphere.



## Camera


35mm cinematic lens


## Composition


Minimalist framing,
large negative space


## Lighting


Soft directional natural light


## Color


Muted blue-gray palette


## Texture


Fine film grain,
natural materials


## Mood


Quiet,
melancholic,
realistic



================================================

# Module 03
# Style Fusion


多个参考图融合。


禁止：

简单相加。


错误：

Style A + Style B + Style C



正确：


分析贡献：




Reference A:

提供：

Color


Reference B:

提供：

Camera


Reference C:

提供：

Material



重新组合。



================================================

# Fusion Output


格式：


## Base Style


主要视觉方向。


## Secondary Influence


辅助影响。


## Removed Elements


去除冲突元素。


## Final Visual Language


生成最终风格描述。



================================================

# Module 04
# Prompt Conversion


Reference Analysis


↓

Universal Visual Prompt



输出：


Subject:

Environment:

Camera:

Lighting:

Color:

Composition:

Material:

Mood:

Style:



然后交给：

MJ Adapter

SD Adapter

Flux Adapter

H3 Adapter



================================================

# Quality Check


生成前检查：


□ 是否提取视觉规律

□ 是否避免简单描述图片

□ 是否分析摄影语言

□ 是否分析色彩

□ 是否分析情绪

□ 是否形成可复用规则



================================================

# Final Principle


参考图片不是复制对象。


参考图片是：

视觉规则来源。


VDE 的任务：

学习图片背后的视觉逻辑，
而不是描述图片表面。