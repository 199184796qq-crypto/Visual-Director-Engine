# VDE 转换核验报告

14/14 风格编号唯一且连续；速查表与详细条目的名称、年代、色调、混合视觉短语及电影列表逐项一致。

完整原文件与 JSON 原始章节保留；图片链接仅保留，未下载、分析或验证可用性。

## 待补充字段

|风格|未可靠提取的字段|
|---|---|
|style_01 三色 Technicolor 浓彩|camera, composition, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_02 新好莱坞暗调琥珀|texture, camera, composition, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_03 铅黄电影 Giallo 高饱和迷幻|texture, camera, composition, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_04 林奇式郊区怪奇|texture, camera, composition, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_05 王家卫 × 杜可风 暧昧浓彩|lighting_tonality, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_06 张艺谋大色块|texture, camera, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_07 韦斯·安德森对称粉彩|lighting_tonality, camera, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_08 热内式金绿梦幻|texture, composition, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_09 冷绿惊悚 & 漂白旁路|camera, composition, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_10 Teal & Orange 大片色|camera, composition, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_11 赛博朋克霓虹夜|texture, camera, composition, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_12 自然光魔幻时刻|texture, camera, composition, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_13 日系青春逆光|texture, camera, composition, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|
|style_14 A24 当代自然主义|camera, composition, visual_identity.mood, color.primary/secondary/accent, best_for, english_style_prompt, camera_model/lens_focal_length|

## 资料边界

- 每风格保留 6 条人物、4 条道具描述；共 84 条人物、56 条道具。三个场景章节仅保留原始图片资料，不编造文字。
- visual_identity 当前使用原风格名称，情绪语义未推断；主色、辅色、点缀色未强行排序。
- best_for、英文风格提示词及具体摄影器材需要补充资料或另行 AI 推导，并标记推导来源。
- 原文引用的 14 个 README 和美术档案未提供，不能宣称完成详细档案转换。
- 原始电影名简写、疑似错字、风格概括均照录；转换完成不等于电影研究事实已校验。
- 后续 AI 补充应写入独立 enrichment 字段，记录依据和审核状态，不覆盖 source 字段。
