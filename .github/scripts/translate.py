#!/usr/bin/env python3
"""
Auto-translation script: translates Korean markdown files to English.

Uses GitHub Models (Azure OpenAI via GITHUB_TOKEN) for context-aware,
agentic translation that understands the full document at once.
No extra secrets required — GITHUB_TOKEN is available in every
GitHub Actions workflow automatically.

Run from repository root.
"""

import os
import re
import sys

try:
    from openai import OpenAI
except ImportError:
    print("openai package not installed. Run: pip install openai")
    raise

# ---------------------------------------------------------------------------
# GitHub Models endpoint — powered by Azure OpenAI, authenticated with
# the workflow's GITHUB_TOKEN (no extra secrets needed).
# ---------------------------------------------------------------------------
_GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
if not _GITHUB_TOKEN:
    print("ERROR: GITHUB_TOKEN environment variable is not set.", file=sys.stderr)
    sys.exit(1)

_client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=_GITHUB_TOKEN,
)

_MODEL = "gpt-4o-mini"   # Fast, cost-efficient, excellent translation quality

_SYSTEM_PROMPT = """\
You are a professional technical translator specialising in Microsoft documentation.

Translate the Korean markdown content provided by the user into natural, professional English.

Rules you MUST follow:
1. Return ONLY the translated markdown — no explanations, no wrapping, no extra text.
2. Preserve ALL markdown formatting exactly: headings (#), bold (**), italic (*),
   tables (|), code fences (```), blockquotes (>), lists (- / * / 1.), and
   Jekyll-specific directives ({: .classname }).
3. Do NOT translate content inside fenced code blocks (``` ... ```).
4. In the YAML front matter (between --- delimiters):
   - Translate only the value of the `title:` key.
   - Leave all other front-matter keys and values (nav_order, layout, lang, etc.) unchanged.
5. Preserve all URLs, file paths, product names (Copilot Studio, Teams, Power Automate,
   SharePoint, M365, etc.), variable names, and HTML tags unchanged.
6. Keep Korean-language user-interface labels that appear inside code fences unchanged.
7. Maintain the exact same line count and blank-line spacing as the source.
"""


def translate_document(content: str) -> str:
    """Send the full markdown document to GitHub Models for translation."""
    try:
        response = _client.chat.completions.create(
            model=_MODEL,
            messages=[
                {"role": "system", "content": _SYSTEM_PROMPT},
                {"role": "user", "content": content},
            ],
            temperature=0.1,   # Low temperature for maximum translation consistency
        )
    except Exception as exc:
        print(f"  ERROR: GitHub Models API call failed — {exc}", file=sys.stderr)
        raise

    result = response.choices[0].message.content
    if not result:
        raise ValueError(
            "GitHub Models returned an empty response. "
            "This may indicate content filtering or a service issue."
        )
    return result


def add_lang_en(content: str) -> str:
    """Ensure 'lang: en' is present in the front matter."""
    if not content.startswith("---\n"):
        return content
    end = content.index("\n---\n", 4)
    fm = content[:end]
    rest = content[end:]
    if "lang:" not in fm:
        return fm + "\nlang: en" + rest
    # Replace any existing lang value with 'en'
    return re.sub(r"(^|\n)lang:\s*\S+", r"\1lang: en", content, count=1)


def process_file(src: str, dst: str) -> None:
    print(f"  {src} → {dst}")
    with open(src, encoding="utf-8") as f:
        content = f.read()

    translated = translate_document(content)
    translated = add_lang_en(translated)

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(translated)


def main() -> None:
    repo_root = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    src_dst_pairs = [("index.md", "en/index.md")]

    docs_dir = os.path.join(repo_root, "docs")
    for name in sorted(os.listdir(docs_dir)):
        if name.endswith(".md"):
            src_dst_pairs.append((f"docs/{name}", f"en/docs/{name}"))

    print(f"Translating {len(src_dst_pairs)} file(s) via GitHub Models ({_MODEL})...")
    for src_rel, dst_rel in src_dst_pairs:
        src = os.path.join(repo_root, src_rel)
        dst = os.path.join(repo_root, dst_rel)

        # Skip files that haven't been updated since the last translation run
        if os.path.exists(dst):
            if os.path.getmtime(dst) >= os.path.getmtime(src):
                print(f"  (skip, up to date) {src_rel}")
                continue

        process_file(src, dst)

    print("Done.")


if __name__ == "__main__":
    main()
