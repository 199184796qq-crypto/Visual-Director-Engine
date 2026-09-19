# VDE 电影风格知识库转换

已将用户提供的电影风格 Markdown 转为 14 条来源限定的结构化记录。

- `tools/convert_style_library.py`：Python 3.10+，仅标准库，无联网或模型调用。
- `knowledge/visual_styles/style_library_vde.md`：可读知识库。
- `knowledge/visual_styles/style_library_vde.json`：机器调用版本，入口为 `styles` 数组。
- `knowledge/visual_styles/style_library_source.md`：逐字节保留的原始文件。
- `knowledge/visual_styles/conversion_report.md`：逐风格缺失项与资料边界。

在 VDE 目录中运行：

```powershell
python tools/convert_style_library.py knowledge/visual_styles/style_library_source.md --output-dir knowledge/visual_styles
```

转换器针对本资料的标题、速查表与字段格式；编号重复、遗漏、表格与详情冲突会中止生成。其他版式应调整解析规则后再导入。

按 `style_id` 查找风格，组合 `prompt_keywords.style` 与任务所需的 `prompt_keywords.content`。不要无条件拼接所有内容词。`asset_examples` 是生成测试资料，其统一棚拍条件不属于母风格特征。原始图像链接保留在 JSON 与原始 MD，未验证可访问性。

`evidence` 提供来源章节与起始行号。词句只去掉 Markdown 转义或按原有分隔符拆分；`lighting_tonality`、`texture`、`camera`、`composition` 使用显式规则归类，完整混合描述仍在 `source_mixed_texture_tonality`。同一短语可能同时涉及多个维度。

`best_for`、情绪、具体器材、英文风格提示词等缺乏依据时留空。后续推导请另存 `enrichment` 并记录依据和审核状态。原文来源说明与图片使用说明完整保留在原始 MD 中。
