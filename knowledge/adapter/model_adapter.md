# VDE Model Adapter Library
# 多模型提示词转换规则 v1.0


================================================

# 核心原则


VDE 输出分为两层：


Layer 1:

Universal Visual Prompt

（视觉导演层）


Layer 2:

Model Prompt

（模型适配层）


禁止：

不同模型直接共用同一个 Prompt。


原因：

不同模型理解语言方式不同。


================================================


# Universal Prompt结构


所有模型转换前必须包含：


## Concept

视觉概念。


## Subject

主体。


## Appearance

外观。


## Action

动作。


## Environment

环境。


## Composition

构图。


## Camera

摄影。


## Lighting

光影。


## Color

色彩。


## Material

材质。


## Mood

情绪。


## Style

风格。



================================================


# Adapter 01
# Midjourney Adapter


## 模型特点


Midjourney 更理解：

- 视觉概念
- 艺术方向
- 摄影语言
- 氛围词


不适合：

过长结构化说明。


================================================


# MJ转换规则


保留：

Subject

Environment

Style

Camera

Lighting


压缩：

Technical explanation


================================================


# MJ Prompt格式

