# VDE Prompt Evaluation System
# AI视觉提示词质量评估与优化模块 v1.0


================================================

# 模块定位


Prompt Evaluation 是 VDE 的视觉质量审核系统。


作用：

对生成后的 Universal Visual Prompt 和模型 Prompt 进行检查。


目标：

不是判断文字是否漂亮。

而是判断：

这个 Prompt 是否能够稳定表达目标视觉。


流程：

Prompt生成

↓

质量检测

↓

问题定位

↓

自动优化建议

↓

最终输出



================================================

# Evaluation Framework


评估维度：

1. Concept
2. Subject
3. Environment
4. Action
5. Composition
6. Camera
7. Lighting
8. Color
9. Material
10. Style
11. Model Compatibility



================================================

# 01 Concept Evaluation
# 视觉概念检查


检查：

是否一句话说明画面核心。


合格：

"A lonely warrior standing in a frozen battlefield."


不合格：

"beautiful amazing cinematic image"


问题：

缺少视觉主题。


优化：

增加：

- 时间
- 地点
- 人物关系
- 情绪



================================================

# 02 Subject Evaluation
# 主体检查


检查：


## Identity

是否明确：

- 人
- 动物
- 产品
- 建筑


## Appearance

是否包含：

- 年龄
- 外观
- 服装
- 材质


## Distinctive Features

是否有记忆点。


例如：

普通：

a warrior


优化：

a middle-aged scar-faced Chinese swordsman wearing worn dark robes



评分：

0-5


0:
无主体


3:
基本明确


5:
具有视觉识别度



================================================

# 03 Environment Evaluation
# 环境检查


检查：


是否包含：


Location:

地点


Time:

时间


Atmosphere:

环境氛围


Spatial Relationship:

空间关系



错误：

"a man in forest"


优化：

"a man standing deep inside an ancient misty forest surrounded by giant trees"



================================================

# 04 Action Evaluation
# 动作检查


静态图片也需要状态。


检查：


- 姿态
- 动作趋势
- 视线方向
- 身体状态



错误：

woman


优化：

woman standing by the window,
looking outside quietly



================================================

# 05 Composition Evaluation
# 构图检查


检查：


主体位置：

- center
- left
- right


空间：

- foreground
- middle ground
- background


视觉引导：

- leading lines
- symmetry
- negative space



缺失：

自动补充建议。



================================================

# 06 Camera Evaluation
# 摄影检查


检查：


## Shot Size


是否明确：

- close-up
- medium shot
- full shot
- wide shot



## Lens


是否合理：


人物：

85mm


环境：

24mm


电影：

35mm



## Perspective


是否明确：

- low angle
- eye level
- high angle



================================================

# 07 Lighting Evaluation
# 光影检查


检查：


Light Source:

光源


Direction:

方向


Quality:

软硬


Mood:

情绪



错误：

beautiful lighting


优化：

soft golden hour sunlight from the left side,
gentle shadows



================================================

# 08 Color Evaluation
# 色彩检查


检查：


Primary Color

主色


Secondary Color

辅助色


Mood Color

情绪色



避免：

随机添加颜色。



错误：

red blue green purple cinematic


优化：

cold blue-gray palette with warm highlights



================================================

# 09 Material Evaluation
# 材质检查


适用于：

人物：

- skin
- hair
- fabric


物体：

- metal
- glass
- wood


环境：

- weathering
- texture



目标：

增加真实感。



================================================

# 10 Style Evaluation
# 风格检查


检查：


## Style Consistency


是否冲突。


错误：

anime style

+
photorealistic

+
oil painting


处理：

选择主风格。


规则：

主风格：

70%

辅助风格：

20%

细节风格：

10%



================================================

# 11 Model Compatibility
# 模型适配检查



## Midjourney


检查：

- 是否过长
- 是否关键词堆积
- 是否有参数


优化：

减少解释性文字。



-------------------------------


## SDXL


检查：

- 是否有正向提示
- 是否有负向提示


-------------------------------


## Flux


检查：

是否自然语言。


-------------------------------


## 即梦


检查：

是否符合中文描述逻辑。


-------------------------------


## H3 Image


检查：

是否包含：

- 空间关系
- 摄影语言
- 影视感



================================================

# Prompt Conflict Detection
# 冲突检测


检测：


## Style Conflict


例如：

古代武侠

+

未来赛博城市

需要用户确认。


---

## Lighting Conflict


例如：

sunset

+

midnight

冲突。


---

## Camera Conflict


例如：

macro close-up

+

wide aerial shot

冲突。



================================================

# Auto Optimization Rules


发现问题后：

不要直接重写。


先输出：


## Problem

问题。


## Reason

原因。


## Suggestion

优化方向。


## Revised Prompt

修正版。



================================================

# Final Evaluation Score


总分：

100


评分：

Concept:
10

Subject:
15

Environment:
10

Action:
10

Composition:
15

Camera:
10

Lighting:
10

Color:
5

Material:
5

Style:
5

Model Compatibility:
5



等级：


90-100:

Production Ready


75-90:

Good


60-75:

Needs Improvement


<60:

Rewrite Recommended



================================================

# Final Rule


好的 Prompt 不是更长。

而是：

视觉信息完整，
模型理解明确，
风格方向统一。


VDE 输出必须经过 Evaluation 后，
才认为完成。