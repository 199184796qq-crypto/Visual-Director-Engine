# VDE Negative Knowledge Library
# AI视觉错误预防数据库 v1.0


================================================

# 核心原则


负面知识不是禁止生成。

而是：

提前识别视觉风险，
避免模型产生错误理解。


流程：


Prompt

↓

Risk Detection

↓

Conflict Analysis

↓

Correction



================================================

# Category 01
# Subject Problems
# 主体问题


================================================

## 01. 主体过于模糊


错误：

a beautiful woman


问题：

模型不知道：

- 年龄
- 身份
- 外观
- 气质


优化：


增加：

Age

Appearance

Clothing

Emotion



Example:


Before:

beautiful woman


After:

a 28-year-old woman with natural facial features,
wearing a linen dress,
calm expression



================================================

## 02. 人物特征冲突


错误：

young old woman


问题：

年龄冲突。


处理：

选择：

young woman

或者

elderly woman



================================================

## 03. 身份与服装冲突


错误：

medieval knight wearing modern business suit


处理：

确认时代一致性。



================================================


# Category 02
# Style Conflict
# 风格冲突


================================================

## 01. 写实与非写实冲突


错误：


photorealistic

+
cartoon

+
oil painting


问题：

模型不知道主要方向。


规则：


选择：

主风格

+
辅助质感



正确：

photorealistic portrait,
with painterly color atmosphere



================================================

## 02. 过多艺术家风格


错误：

Van Gogh,
Picasso,
Disney,
Nolan,
Wong Kar-wai


问题：

视觉方向混乱。


规则：

最多：

1个主要风格来源

2个辅助视觉元素



================================================

# Category 03
# Camera Conflict
# 摄影冲突


================================================

## 01. 景别冲突


错误：

macro close-up

+
aerial wide shot


问题：

镜头无法同时成立。



解决：

选择主要镜头。


或者：

拆成多个镜头。



================================================

## 02. 镜头与主体不匹配


错误：

85mm portrait lens

+
huge battlefield


问题：

空间表现不足。


建议：

战场：

24mm / 35mm


人物：

85mm



================================================

# Category 04
# Lighting Conflict
# 光影冲突


================================================

## 01. 时间冲突


错误：

sunrise

+
midnight


解决：

选择时间。



================================================

## 02. 光源冲突


错误：

soft candle light

+
bright studio flash


解决：

确定主光源。



================================================

# Category 05
# Color Conflict
# 色彩冲突


================================================

## 01. 颜色过多


错误：

red blue green purple gold neon


问题：

视觉焦点消失。



规则：

主色：

1种


辅助色：

1-2种



================================================

## 02. 色彩与情绪冲突


错误：

horror scene

+
bright cheerful colors


解决：

匹配情绪。



================================================

# Category 06
# Material Problems
# 材质错误


================================================

## 01. 塑料皮肤


常见：

AI portrait


检测词：

plastic skin

perfect skin


优化：

natural skin texture

skin pores

realistic imperfections



================================================

## 02. 服装错误


问题：

布料没有重量。


优化：

fabric texture

natural wrinkles

material details



================================================

# Category 07
# AI Common Failure


================================================

## 人物


避免：


bad anatomy

extra fingers

deformed hands

asymmetrical eyes

unnatural face



================================================

## 产品


避免：


floating object

wrong perspective

fake reflection

distorted logo



================================================

## 建筑


避免：


impossible structure

wrong perspective

floating building



================================================

# Category 08
# Prompt Pollution
# 无效关键词污染


避免大量：

masterpiece

best quality

8k

ultra HD


原因：

现代模型理解有限。


替换：

具体视觉信息。



错误：

8k beautiful cinematic


正确：

ARRI Alexa photography,
natural skin texture,
soft cinematic lighting



================================================

# Category 09
# Reference Image Conflict


当用户提供参考图：


不要复制：

- 随机物体
- 偶然颜色
- 背景噪声


提取：

视觉规律。



================================================

# Category 10
# VDE Correction Rules


发现问题：


不要删除用户创意。


流程：


保留核心意图

↓

修正冲突

↓

补充视觉信息

↓

生成优化版本



================================================

# Final Principle


优秀生成不是添加更多词。

而是：

减少歧义。

减少冲突。

增加视觉确定性。


VDE 优先保证：

Subject clarity

+
Visual consistency

+
Style coherence