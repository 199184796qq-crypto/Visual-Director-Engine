# VDE Visual Style Library
# AI视觉风格数据库 v1.0


# 使用规则

风格选择不能随机添加。

必须根据：

- 题材
- 时代
- 情绪
- 场景
- 用户用途
- 人物身份

进行匹配。


禁止：

直接堆叠多个风格名称。

错误：

"Christopher Nolan + Wong Kar-wai + Apple style"


正确：

分析每个风格贡献：

Nolan:
空间规模、真实摄影、结构感

Wong Kar-wai:
情绪、色彩、时间感

Apple:
简洁、高级材质


融合后生成新的视觉语言。


================================================

# Category 01
# Cinematic Film Style
# 电影视觉风格


------------------------------------------------
## 01. Wong Kar-wai Inspired
## 王家卫港风

适用：

- 都市
- 爱情
- 回忆
- 孤独
- 夜晚


视觉特点：

- 情绪优先
- 时间停滞感
- 人物孤独感
- 强烈色彩情绪


Camera:

35mm film photography

slow shutter motion blur

anamorphic lens

shallow depth of field


Lighting:

neon reflection

mixed color lighting

practical lights


Color:

deep red

emerald green

warm orange

dark shadows


Texture:

film grain

analog photography


Prompt语言：

Wong Kar-wai inspired Hong Kong cinema,
moody neon atmosphere,
35mm film look,
emotional urban loneliness


------------------------------------------------

## 02. Christopher Nolan Inspired
## 诺兰式电影现实主义


适用：

- 科幻
- 战争
- 史诗
- 现实主义剧情


视觉特点：

- 巨大空间
- 真实物理感
- 强结构构图


Camera:

IMAX photography

large format cinema

wide angle lens


Lighting:

natural dramatic lighting

high contrast


Color:

cold gray

desaturated tones


Prompt语言：

realistic cinematic photography,
IMAX film look,
large scale composition,
dramatic natural lighting


------------------------------------------------

## 03. Denis Villeneuve Inspired
## 维伦纽瓦式冷峻科幻


适用：

- 科幻
- 悬疑
- 荒凉世界


视觉特点：

- 极简
- 压迫
- 孤独


Camera:

wide cinematic shot

slow visual rhythm


Lighting:

soft diffused light

heavy atmosphere


Color:

sand tone

cold blue

muted palette


Prompt语言：

Denis Villeneuve inspired cinematic style,
minimalist sci-fi atmosphere,
muted colors,
large scale environment


------------------------------------------------

## 04. Zhang Yimou Inspired
## 张艺谋东方色彩美学


适用：

- 中国历史
- 武侠
- 东方叙事


视觉特点：

- 大色块
- 强视觉符号
- 对称构图


Composition:

symmetrical framing

strong visual balance


Color:

deep red

gold

black

pure color blocks


Lighting:

dramatic natural light


Prompt语言：

Chinese cinematic color composition,
bold color palette,
symmetrical framing,
traditional visual storytelling


================================================

# Category 02
# Photography Style
# 摄影风格


------------------------------------------------

## 05. Documentary Photography
## 纪录片摄影


适用：

- 真实生活
- 社会
- 人物故事


特点：

真实
自然
不刻意摆拍


Camera:

35mm documentary photography


Lighting:

available natural light


Prompt：

documentary photography,
authentic human moment,
natural lighting,
realistic atmosphere


------------------------------------------------

## 06. Leica Street Photography
## 莱卡街头摄影


适用：

- 城市
- 人文
- 旅行


特点：

- 观察感
- 瞬间捕捉


Camera:

Leica M11

35mm lens


Texture:

film grain


Prompt：

Leica street photography,
candid moment,
natural urban atmosphere


------------------------------------------------

## 07. Vogue Editorial
## 高级时尚摄影


适用：

- 模特
- 服装
- 美妆


特点：

- 高级
- 精致
- 强造型


Camera:

85mm portrait lens


Lighting:

studio lighting


Composition:

fashion editorial


Prompt：

Vogue editorial photography,
luxury fashion style,
high-end portrait,
clean composition


------------------------------------------------

## 08. Apple Product Photography
## 苹果极简商业摄影


适用：

- 产品
- 科技
- 高端品牌


特点：

- 极简
- 干净
- 精准


Background:

clean space


Lighting:

soft studio lighting


Material:

premium material detail


Prompt：

minimalist product photography,
premium technology aesthetic,
clean studio lighting


================================================

# Category 03
# Fantasy & Game Style
# 奇幻游戏风格


------------------------------------------------

## 09. Dark Fantasy


适用：

- 魔幻
- 黑暗世界
- 战斗


特点：

- 压迫
- 神秘
- 厚重


Lighting:

dramatic shadows

fog


Color:

dark tones

desaturated colors


Prompt：

dark fantasy concept art,
epic atmosphere,
dramatic lighting,
high detail


------------------------------------------------

## 10. Cyberpunk


适用：

- 未来城市
- 科技


特点：

- 霓虹
- 机械
- 信息密度


Color:

neon blue

magenta

purple


Lighting:

rain reflection

holographic light


Prompt：

cyberpunk city,
neon lights,
rainy streets,
futuristic atmosphere


------------------------------------------------

## 11. Studio Ghibli Inspired


适用：

- 温暖
- 奇幻
- 儿童


特点：

- 手绘
- 温柔
- 自然


Color:

soft pastel


Lighting:

warm sunlight


Prompt：

hand painted animation style,
soft natural environment,
warm storytelling atmosphere


================================================

# Category 04
# Realistic Commercial Style


------------------------------------------------

## 12. Luxury Advertisement


适用：

- 奢侈品
- 高端品牌


特点：

- 精致
- 高价值感


Lighting:

controlled studio lighting


Material:

premium texture


Prompt：

luxury advertising photography,
premium materials,
high-end commercial aesthetic


------------------------------------------------

## 13. Cinematic Realism


通用默认写实风格


适用：

大多数影视画面。


Camera:

ARRI Alexa 65

35mm cinema lens


Lighting:

natural cinematic lighting


Texture:

real skin texture


Prompt：

cinematic realism,
ARRI Alexa 65,
natural textures,
realistic lighting


================================================

# Style Selection Logic


## 情绪匹配


孤独：

优先：

- Wong Kar-wai
- Documentary
- Japanese minimalist


温暖：

优先：

- Korean drama
- Ghibli inspired
- Lifestyle photography


压迫：

优先：

- Villeneuve
- Dark fantasy
- Low key cinema


高级：

优先：

- Vogue
- Luxury advertisement
- Apple style


史诗：

优先：

- Nolan
- Ridley Scott
- Epic fantasy


================================================

# 默认规则


如果用户没有指定风格：

不要随机添加艺术家名字。


默认：

Cinematic Realism


如果用户提供参考图：

优先学习：

Reference Visual DNA

而不是调用固定风格。

