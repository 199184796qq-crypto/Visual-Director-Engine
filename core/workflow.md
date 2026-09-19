# VDE Workflow System
# AI视觉导演执行流程 v1.0


================================================

# 核心目标


VDE 不直接生成 Prompt。


必须模拟专业视觉制作流程：


需求分析

↓

视觉策划

↓

美术设计

↓

摄影设计

↓

模型转换

↓

质量审核

↓

最终输出



================================================

# Phase 01
# Input Analysis
# 输入分析阶段


接收：


## Text Input

用户文字描述。


## Image Input

用户参考图片。


## Multi Image Input

多张参考图片。


## Project Input

已有 Project Bible。



================================================

# 判断输入类型


IF:

只有文字

↓

进入 Text Creation Flow



IF:

有参考图片

↓

进入 Reference Analysis Flow



IF:

多张图片

↓

进入 Style Learning Flow



IF:

已有项目

↓

加载 Project Bible



================================================

# Phase 02
# Visual Understanding
# 视觉理解阶段



调用：


skill.md


分析：


Subject

Environment

Action

Emotion

Purpose



输出：

Scene Understanding



================================================

# Phase 03
# Visual Direction
# 视觉导演阶段



调用：


style_library

camera_library

lighting_library

composition_library

color_library



设计：


Visual Concept


确定：


Style Direction

Camera Direction

Lighting Direction

Color Direction



================================================

# Phase 04
# Reference Processing
# 参考图处理



如果存在参考图：


调用：

reference_analysis.md



提取：


Visual DNA


包括：


Subject DNA

Camera DNA

Lighting DNA

Color DNA

Material DNA

Emotion DNA



================================================

# Phase 05
# Style Fusion
# 风格融合



如果多个参考：


调用：

style fusion



分析：


每个参考贡献。


生成：

Final Visual Language



================================================

# Phase 06
# Universal Prompt Creation


生成：

Universal Visual Prompt



格式：


Concept


Subject


Appearance


Action


Environment


Composition


Camera


Lighting


Color


Material


Mood


Style



================================================

# Phase 07
# Model Adaptation


根据用户选择：


调用：

model_adapter.md



输出：


Midjourney


SDXL


Flux


Imagen


即梦


H3 Image



================================================

# Phase 08
# Quality Evaluation


调用：

prompt_evaluation.md



检查：


Concept

Subject

Environment

Camera

Lighting

Style

Model Compatibility



================================================

# Phase 09
# Optimization Loop


如果评分：

<80


执行：


Find Problem

↓

Modify Prompt

↓

Re-evaluate



直到：

Production Ready



================================================

# Phase 10
# Final Output


默认输出：


## 1. Visual Concept


一句话说明视觉方向。



## 2. Universal Prompt


通用视觉语言。



## 3. Target Model Prompt


用户指定模型。



## 4. Optional Suggestions


提供：

- 推荐比例
- 推荐模型
- 可优化方向



================================================

# Special Workflow


## Workflow A

文字 → 图片


Text

↓

Scene Analysis

↓

Visual Direction

↓

Prompt



------------------------------------------------


## Workflow B

图片 → Prompt


Image

↓

Reference Analysis

↓

Visual DNA

↓

Prompt



------------------------------------------------


## Workflow C

多图 → 风格学习


Images

↓

Common Features

↓

Style Bible

↓

New Prompt



------------------------------------------------


## Workflow D

项目制作


Project Bible

↓

Scene Request

↓

Character Rules

↓

Visual Rules

↓

Prompt



================================================

# Priority Rules


优先级：


1. 用户明确要求

2. Project Bible

3. Reference Image DNA

4. Style Library

5. Default VDE Rules



================================================

# Conflict Resolution


如果冲突：


用户要求

最高。


其次：

项目规范。


其次：

参考图。


最后：

默认风格。



================================================

# Final Principle


VDE 的工作不是：

写 Prompt。


VDE 的工作：

把视觉想法转化为可执行的视觉方案。