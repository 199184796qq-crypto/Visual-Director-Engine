# VDE Character Bible
# 人物圣经 v1.0

Character Bible 是项目级人物连续性规范。它把“这个人是谁、长什么样、穿什么、怎么表现、哪些特征不能变”固定下来，供生图、分镜、视频和海报共同调用。

## 使用优先级

用户明确要求 > 项目 Character Bible > 角色资产库 > 风格库 > 默认 VDE 规则。

风格可以改变光线、色彩和环境，但不能随意改变角色身份、年龄区间、体型、发型、服装标志和道具标志。

## 角色主档案

每个主要角色建立一份记录，字段保持稳定：

```yaml
character_id: char_001
name: 角色名
project_id: project_id
role: 主角 / 配角 / 群像
identity:
  age_range: 年龄区间
  gender_presentation: 性别呈现
  occupation: 身份或职业
  social_status: 社会位置
appearance:
  face: 脸型与显著面部特征
  skin: 肤色与皮肤质感
  hair: 发型、发色、长度
  body: 身高、体型、比例
wardrobe:
  base: 固定主服装
  palette: 固定服装色
  material: 面料与磨损程度
  variations: 随剧情允许的变化
signature:
  face: 不可改变的脸部标志
  costume: 不可改变的服装标志
  prop: 标志性道具
  gesture: 常用姿态或动作
  expression: 默认情绪基线
story_state:
  unchanged: 全片必须保持
  progression: 随剧情变化
  forbidden: 禁止出现
performance:
  posture: 身体姿态
  gaze: 视线习惯
  movement: 动作节奏
  emotional_range: 情绪范围
visual_constraints:
  keep: 必须保留
  avoid: 必须避免
reference_images: []
status: draft
source: user / reference / generated / approved
```

## 连续性规则

1. 首次建立角色时，优先生成正面、侧面、背面和全身资产；同一批资产锁定脸、发型、体型和服装比例。
2. 后续镜头只改变景别、姿态、表情和环境。年龄、发色、发际线、疤痕、眼镜、制服徽章等身份特征不得漂移。
3. 服装变化必须记录时间、地点、剧情原因和替换前后差异；没有记录时沿用上一场服装。
4. 角色道具必须绑定到角色或场景，不能在镜头间无原因出现、消失或变形。
5. 参考图用于锁定视觉 DNA；偶然背景、路人、文字和随机饰品不写入人物主档案。
6. 风格迁移只改造光色、材质和环境表达，不覆盖角色主档案。

## 资产包规范

每个角色建议保存：

- `character_front`：正面全身，明确服装和鞋
- `character_side`：侧面全身，确认轮廓和鼻口比例
- `character_back`：背面全身，确认发型、衣服背面和道具携带方式
- `character_closeup`：面部近景，确认肤质、眼睛和表情基线
- `character_expression_sheet`：平静、喜悦、愤怒、恐惧、悲伤、疲惫
- `character_action_sheet`：站立、行走、奔跑、坐姿、持物
- `character_costume_sheet`：固定服装与允许变化

统一生成约束：人物细节清晰、姿态完整、背景和光线按项目要求锁定；不要把测试用的浅灰棚拍背景和均匀布光误当成角色的世界观。

## 提示词拼装顺序

```text
[角色身份] + [外貌锁定] + [服装锁定] + [标志道具]
+ [动作与表情] + [场景关系] + [镜头]
+ [项目视觉风格] + [连续性限制]
```

角色主档案字段为空时，不用模型常识擅自补齐；先保留空值，或写入独立 `enrichment` 字段并记录依据与审核状态。

## 交付前检查

- 身份、年龄区间和职业是否一致
- 脸型、发型、肤色和体型是否一致
- 固定服装、颜色、材质和标志物是否一致
- 动作与情绪是否符合当前剧情状态
- 角色与场景的时代、道具和社会环境是否冲突
- 是否把参考图偶然元素错误写成角色特征
- 是否记录了本次新增或改变的角色状态

## 版本记录

- v1.0：建立角色字段、连续性规则、资产包和检查表
- v1.1：新增角色或服装状态
- v1.2：新增表情、动作或道具资产
- v2.0：项目整体人物体系变更
