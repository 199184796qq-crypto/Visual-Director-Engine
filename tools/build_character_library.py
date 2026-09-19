import json
from pathlib import Path

root = Path(__file__).parents[1]
style_path = root / 'knowledge' / 'visual_styles' / 'style_library_vde.json'
out = root / 'knowledge' / 'character'
data = json.loads(style_path.read_text(encoding='utf-8'))
out.mkdir(parents=True, exist_ok=True)
characters = []
for style in data['styles']:
    assets = next((x for x in style['asset_examples'] if x['kind'] == '六角色'), None)
    if not assets:
        continue
    for index, description in enumerate(assets['items'], 1):
        prefix = f"{style['style_id']}_char_{index:02d}"
        characters.append({
            'character_id': prefix,
            'style_id': style['style_id'],
            'style_name': style['name'],
            'source_line': assets['line'],
            'asset_role': f'角色 {chr(64 + index)}',
            'description': description,
            'identity': None,
            'appearance': None,
            'wardrobe': None,
            'signature': None,
            'performance': None,
            'source': 'source_asset_description',
            'status': 'reference_asset_only',
            'notes': ['原文只提供一段测试角色描述；未将其推断为完整项目角色。', '人物圣经字段需在具体项目中确认。']
        })
payload = {
    'schema_version': '1.0',
    'purpose': 'VDE reference character asset index',
    'source': 'knowledge/visual_styles/style_library_source.md',
    'policy': 'Raw descriptions are preserved; empty Character Bible fields require project confirmation.',
    'characters': characters
}
(out / 'character_library.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
md = ['# VDE Character Asset Library', '', '来源：14 风格测试资料中的“六角色”描述，共 84 条。它们是参考资产，不是已批准的项目角色。', '', '按 `character_id` 查询；具体项目使用时复制到 Character Bible 主档案并补充身份、外貌、服装状态和剧情状态。', '']
for c in characters:
    md += [f"## {c['character_id']} · {c['style_name']} · {c['asset_role']}", '', c['description'], '', f"来源：原文第 {c['source_line']} 行；状态：{c['status']}", '']
(out / 'character_library.md').write_text('\n'.join(md), encoding='utf-8')
print(f'Generated {len(characters)} character reference assets')
