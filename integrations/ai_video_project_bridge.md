# VDE × AI 视频项目协同桥接

VDE（D:\MyAiVDE）是视觉设计层，负责视觉 DNA、色卡、图样、视觉风格词段、人物圣经和场景规范。
AI 视频项目框架（E:\H3的技能）是执行层，负责项目、视频、剧情、分镜、素材、音频、模型提示词、续写、审核和归档。MiniMax H3、Wan3、Seedance 是模型分支，不是项目名称。

## 推荐流程

1. 确认项目地址并读取项目入口。
2. 用 VDE 分析文字和参考图，生成 visual_style_words.md、色卡、风格图样、character_bible.md 和 scene_bible.md。
3. 将这些文件放入项目的“视觉规范”目录并登记版本。
4. AI 视频项目框架读取视觉规范，审核故事后选择 H3、Wan3 或其他模型分支。
5. 模型分支把已确认的视觉规范转换成对应提示词，不自行改变视觉身份。
6. 生成视频后，用 VDE 对照色卡、人物和整体视觉 DNA 做偏差检查。

## 建议目录

项目根目录/视觉规范/visual_style_words.md、visual_style_card.png、visual_style_atlas.png、character_bible.md、scene_bible.md。

VDE 不覆盖 AI 视频项目框架的模型输出协议；AI 视频项目框架不反向改写 VDE 的原始风格资料。
