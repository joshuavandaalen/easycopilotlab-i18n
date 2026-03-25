#!/usr/bin/env python3
"""
Auto-translation script: translates Korean markdown files to English.
Preserves markdown formatting, front matter, and code blocks.
Run from repository root.
"""

import os
import re
import time

try:
    from deep_translator import GoogleTranslator
    translator = GoogleTranslator(source='ko', target='en')
except ImportError:
    print("deep-translator not installed. Run: pip install deep-translator")
    raise


def translate_text(text: str) -> str:
    """Translate a chunk of text from Korean to English."""
    if not text or not text.strip():
        return text
    try:
        result = translator.translate(text)
        return result if result else text
    except Exception as exc:
        print(f"  Warning: translation failed — {exc}")
        return text


def translate_front_matter_value(value: str) -> str:
    """Translate a YAML front matter string value."""
    stripped = value.strip().strip('"').strip("'")
    if not stripped:
        return value
    translated = translate_text(stripped)
    return f'"{translated}"'


def translate_table_row(row: str) -> str:
    """Translate cells in a markdown table row."""
    if re.match(r'^[\|\s:\-]+$', row):
        return row  # separator row — skip
    cells = row.split('|')
    result = []
    for cell in cells:
        stripped = cell.strip()
        if stripped and not re.match(r'^[\s:\-]+$', stripped):
            translated = translate_text(stripped)
            result.append(f' {translated} ')
        else:
            result.append(cell)
    return '|'.join(result)


def translate_markdown(content: str) -> str:
    """Translate full markdown content, preserving structure."""
    lines = content.split('\n')
    out = []
    in_front_matter = False
    front_matter_done = False
    in_code_block = False
    fm_dash_count = 0

    for line in lines:
        # --- front matter ---
        if line.strip() == '---' and not front_matter_done:
            fm_dash_count += 1
            if fm_dash_count == 1:
                in_front_matter = True
            elif fm_dash_count == 2:
                in_front_matter = False
                front_matter_done = True
            out.append(line)
            continue

        if in_front_matter:
            # Translate title value; leave everything else as-is
            m = re.match(r'^(title:\s*)(.*)', line)
            if m:
                raw_val = m.group(2)
                out.append(m.group(1) + translate_front_matter_value(raw_val))
            else:
                out.append(line)
            continue

        # --- code blocks ---
        if re.match(r'^\s*```', line):
            in_code_block = not in_code_block
            out.append(line)
            continue
        if in_code_block:
            out.append(line)
            continue

        # --- blank lines / pure formatting ---
        if not line.strip():
            out.append(line)
            continue
        if line.strip() in ('---', '{: .no_toc }', '1. TOC', '{:toc}'):
            out.append(line)
            continue
        if line.strip().startswith('{:'):
            out.append(line)
            continue

        # --- table rows ---
        if '|' in line and line.strip().startswith('|'):
            out.append(translate_table_row(line))
            time.sleep(0.05)
            continue

        # --- headings ---
        m = re.match(r'^(#{1,6}\s+)(.*)', line)
        if m:
            heading_prefix, heading_text = m.group(1), m.group(2)
            if heading_text.strip() and not heading_text.strip().startswith('{'):
                out.append(heading_prefix + translate_text(heading_text))
                time.sleep(0.05)
            else:
                out.append(line)
            continue

        # --- list items ---
        m = re.match(r'^(\s*[-*+]|\s*\d+\.)\s+(.*)', line)
        if m:
            marker, rest = m.group(1), m.group(2)
            if rest.strip():
                out.append(f'{marker} {translate_text(rest)}')
                time.sleep(0.05)
            else:
                out.append(line)
            continue

        # --- blockquotes ---
        m = re.match(r'^(>\s*)(.*)', line)
        if m:
            prefix, rest = m.group(1), m.group(2)
            if rest.strip() and not rest.strip().startswith('{'):
                out.append(prefix + translate_text(rest))
                time.sleep(0.05)
            else:
                out.append(line)
            continue

        # --- regular paragraph text ---
        out.append(translate_text(line))
        time.sleep(0.05)

    return '\n'.join(out)


def add_lang_en(content: str) -> str:
    """Add 'lang: en' to the front matter if not already present."""
    if not content.startswith('---\n'):
        return content
    end = content.index('\n---\n', 4)
    fm = content[:end]
    rest = content[end:]
    if 'lang:' not in fm:
        return fm + '\nlang: en' + rest
    return content


def process_file(src: str, dst: str) -> None:
    print(f'  {src} → {dst}')
    with open(src, encoding='utf-8') as f:
        content = f.read()
    translated = translate_markdown(content)
    translated = add_lang_en(translated)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(translated)


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    src_dst_pairs = []

    # index.md
    src_dst_pairs.append(('index.md', 'en/index.md'))

    # docs/*.md
    docs_dir = os.path.join(repo_root, 'docs')
    for name in sorted(os.listdir(docs_dir)):
        if name.endswith('.md'):
            src_dst_pairs.append((f'docs/{name}', f'en/docs/{name}'))

    print(f'Translating {len(src_dst_pairs)} files...')
    for src_rel, dst_rel in src_dst_pairs:
        src = os.path.join(repo_root, src_rel)
        dst = os.path.join(repo_root, dst_rel)
        # Skip if source hasn't changed since last translation
        if os.path.exists(dst):
            src_mtime = os.path.getmtime(src)
            dst_mtime = os.path.getmtime(dst)
            if dst_mtime >= src_mtime:
                print(f'  (skip, up to date) {src_rel}')
                continue
        process_file(src, dst)

    print('Done.')


if __name__ == '__main__':
    main()
