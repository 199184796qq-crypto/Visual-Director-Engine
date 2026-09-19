"""Convert the supplied 14-style research Markdown without inventing facts.

Python 3.10+, standard library only. Usage:
python convert_style_library.py SOURCE.md --output-dir ../knowledge/visual_styles
"""
import argparse
import hashlib
import json
import re
from pathlib import Path


def clean(s):
    return re.sub(r'\\([\\`*_{}\[\]()#+.!&-])', r'\1', s).strip()


def split_terms(s):
    return [clean(x) for x in re.split(r'\s+·\s+', s) if x.strip()]


def sections(text):
    headings = list(re.finditer(r'^(#{1,6})\s+(.+)$', text, re.M))
    result = []
    for i, h in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        result.append(dict(title=clean(h[2]), level=len(h[1]),
                           line=text.count('\n', 0, h.start()) + 1,
                           raw=text[h.start():end]))
    return result


RULES = {
    'lighting_tonality': r'光|低照|高曝|过曝|高对比',
    'texture': r'颗粒|染料转印|微缩质感|DI 干净渐变',
    'camera': r'慢门|鱼眼',
    'composition': r'框中框|中心对称|大色块铺满',
}


def convert(source):
    blob = source.read_bytes()
    text = blob.decode('utf-8-sig')
    parts = sections(text)
    styles = []
    for p in parts:
        m = re.match(r'^(\d{2})\s*·\s*(.+)$', p['title'])
        if not m or '**核心色调**' not in p['raw']:
            continue
        number, name = int(m[1]), m[2]
        meta = next(x for x in p['raw'].splitlines() if '**核心色调**' in x)
        fields = {k: clean(v) for k, v in re.findall(r'\*\*(.+?)\*\*：\s*(.*?)(?=\s*｜|$)', meta)}
        content = re.search(r'^\*\*内容关键词\*\*：(.+)$', p['raw'], re.M)
        if content is None:
            raise ValueError(f'Missing content keywords: {number}')
        keywords = clean(content[1].split('（详细解析')[0])
        mixed = split_terms(fields['质感/影调'])
        s = dict(style_id=f'style_{number:02d}', source_number=number, name=name,
                 era=clean(meta.split('｜')[0]),
                 visual_identity={'label': name, 'mood': [], 'status': 'source_title_only'},
                 color={'description': fields['核心色调'], 'primary': None,
                        'secondary': None, 'accent': None},
                 **{k: [v for v in mixed if re.search(pattern, v)] for k, pattern in RULES.items()},
                 reference_films=[clean(x) for x in fields['代表电影'].split(' / ')],
                 environment_content_dna=split_terms(keywords),
                 prompt_keywords={'style': list(dict.fromkeys([fields['核心色调']] + mixed)),
                                  'content': split_terms(keywords),
                                  'method': 'source_phrases_only; no translation or model parameters'},
                 best_for=[],
                 source_mixed_texture_tonality=fields['质感/影调'],
                 unclassified_visual_terms=[v for v in mixed if not any(re.search(r, v) for r in RULES.values())],
                 asset_examples=[],
                 source={'file': 'style_library_source.md', 'heading': p['title'],
                         'line': p['line'], 'raw_markdown': p['raw']},
                 evidence={}, notes=[])
        for key in ('name', 'era', 'visual_identity', 'color', 'lighting_tonality', 'texture', 'camera', 'composition', 'reference_films', 'environment_content_dna', 'prompt_keywords'):
            s['evidence'][key] = {'line': p['line'], 'section': p['title'],
                                    'method': 'source_title' if key in ('name', 'visual_identity') else 'extract_or_route_source_phrase'}
        s['notes'] = [
            '年代为来源中的风格年代，不能直接用作场景年代。',
            '字段分类是转换规则；词句保留原文。混合短语可属于多个字段，不推断镜头型号、焦段或胶片规格。',
            '空列表/null 表示本次未可靠提取，不表示该风格不存在该特征。',
            '详细 README、美术与场景档案及英文风格 prompt 未随本文件提供。',
            '人物与道具测试仅作为有出处的资产例子，不自动注入风格光线或摄影字段。',
        ]
        if number == 11:
            s['notes'].append('代表电影中的“2049”为来源简写，未擅自扩展片名。')
        for a in parts:
            am = re.match(r'^(\d{2})\s*·', a['title'])
            if not am or int(am[1]) != number or a is p:
                continue
            kind = next((x for x in ('三个场景', '六角色', '四道具') if x in a['title']), None)
            if kind is None:
                continue
            label = re.search(r'^\*\*(.*?)\*\*：(.+)$', a['raw'], re.M)
            examples = [clean(x) for x in label[2].split(' / ')] if label else []
            s['asset_examples'].append(dict(kind=kind, heading=a['title'], line=a['line'],
                                            items=examples, raw_markdown=a['raw'],
                                            scope='generation_test_only'))
        s['missing_fields'] = [k for k in RULES if not s[k]] + ['visual_identity.mood', 'color.primary/secondary/accent', 'best_for', 'english_style_prompt', 'camera_model/lens_focal_length']
        styles.append(s)
    ids = [s['source_number'] for s in styles]
    if sorted(ids) != list(range(1, 15)):
        raise ValueError(f'Expected exactly unique styles 01–14; got {ids}')
    table = {}
    for line in text.splitlines():
        if re.match(r'^\|\d{2}\|', line):
            cells = [clean(x) for x in line.strip('|').split('|')]
            table[int(cells[0])] = cells[1:]
    if sorted(table) != list(range(1, 15)):
        raise ValueError('Overview table does not contain exactly 14 styles')
    for s in styles:
        expected = [s['name'], s['era'], s['color']['description'], s['source_mixed_texture_tonality'], ' / '.join(s['reference_films'])]
        if table[s['source_number']] != expected:
            raise ValueError(f'Overview/detail conflict: {s["style_id"]}')
        for a in s['asset_examples']:
            n = {'六角色': 6, '四道具': 4}.get(a['kind'])
            if n and len(a['items']) != n:
                raise ValueError(f'Unexpected example count: {s["style_id"]}, {a["kind"]}')
    return {'schema_version': '1.0', 'source': {'original_filename': source.name,
            'author': 'B站 SevnFading', 'sha256': hashlib.sha256(blob).hexdigest(),
            'preserved_file': 'style_library_source.md'},
            'policy': 'Source-only extraction; no external fact checking, image analysis, or AI enrichment. Raw sections and original bytes retained.',
            'styles': styles}, blob


def write_outputs(data, blob, out):
    out.mkdir(parents=True, exist_ok=True)
    (out / 'style_library_source.md').write_bytes(blob)
    (out / 'style_library_vde.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    md = ['# VDE Visual Style Library', '', '来源：B站 SevnFading《电影美学风格资产生成（14 风格）》；14/14 风格。', '',
          '原始文件逐字节保留为 [style_library_source.md](style_library_source.md)。JSON 保存字段出处、原始章节及测试资产。', '',
          '以下为来源限定的结构化记录。空字段是待补充项；prompt_keywords 由原文短语组织，不是补写的英文提示词。', '']
    for s in data['styles']:
        md += [f'## {s["style_id"]} · {s["name"]}', '', f'出处：原文第 {s["source"]["line"]} 行；年代按来源记录。', '']
        compact = {k: v for k, v in s.items() if k not in ('source', 'evidence', 'asset_examples')}
        md += ['```json', json.dumps(compact, ensure_ascii=False, indent=2), '```', '', '### 来源中的测试资产', '']
        for a in s['asset_examples']:
            md += [f'**{a["kind"]}**（原文第 {a["line"]} 行；仅测试用途）', '']
            md += [f'- {x}' for x in a['items']] or ['原文此节仅含图片，未提供场景文字；未从图片推断。']
            md += ['']
    (out / 'style_library_vde.md').write_text('\n'.join(md), encoding='utf-8')
    report = ['# VDE 转换核验报告', '', '14/14 风格编号唯一且连续；速查表与详细条目的名称、年代、色调、混合视觉短语及电影列表逐项一致。', '',
              '完整原文件与 JSON 原始章节保留；图片链接仅保留，未下载、分析或验证可用性。', '',
              '## 待补充字段', '', '|风格|未可靠提取的字段|', '|---|---|']
    report += [f'|{s["style_id"]} {s["name"]}|{", ".join(s["missing_fields"])}|' for s in data['styles']]
    report += ['', '## 资料边界', '',
               '- 每风格保留 6 条人物、4 条道具描述；共 84 条人物、56 条道具。三个场景章节仅保留原始图片资料，不编造文字。',
               '- visual_identity 当前使用原风格名称，情绪语义未推断；主色、辅色、点缀色未强行排序。',
               '- best_for、英文风格提示词及具体摄影器材需要补充资料或另行 AI 推导，并标记推导来源。',
               '- 原文引用的 14 个 README 和美术档案未提供，不能宣称完成详细档案转换。',
               '- 原始电影名简写、疑似错字、风格概括均照录；转换完成不等于电影研究事实已校验。',
               '- 后续 AI 补充应写入独立 enrichment 字段，记录依据和审核状态，不覆盖 source 字段。', '']
    (out / 'conversion_report.md').write_text('\n'.join(report), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--output-dir', type=Path, default=Path('knowledge/visual_styles'))
    args = parser.parse_args()
    data, blob = convert(args.source)
    write_outputs(data, blob, args.output_dir)
    print(f'Validated and converted {len(data["styles"])} styles to {args.output_dir}')


if __name__ == '__main__':
    main()
