#!/usr/bin/env python3
"""
Extract main article content from HTML, convert to clean markdown.

Uses readability-lxml to identify main content region, then pandoc to convert
the cleaned HTML to GFM markdown. Strips remaining inline HTML.

Usage: html-to-clean-md.py <input.html> <output.md> [--title T] [--url U]
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from lxml import html as lxml_html


def main():
    if len(sys.argv) < 3:
        print("usage: html-to-clean-md.py <input.html> <output.md> [--title T] [--url U] [--selector CSS]", file=sys.stderr)
        return 2
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    title_override = ""
    url = ""
    selector = "article"  # default — works for most blog/news templates
    if "--title" in sys.argv:
        title_override = sys.argv[sys.argv.index("--title") + 1]
    if "--url" in sys.argv:
        url = sys.argv[sys.argv.index("--url") + 1]
    if "--selector" in sys.argv:
        selector = sys.argv[sys.argv.index("--selector") + 1]

    raw_html = src.read_text(encoding="utf-8")
    tree = lxml_html.fromstring(raw_html)
    nodes = tree.cssselect(selector)
    if not nodes:
        print(f"WARNING: selector {selector!r} matched 0 elements; falling back to full body", file=sys.stderr)
        nodes = tree.cssselect("body")
    cleaned_html = "\n".join(lxml_html.tostring(n, encoding="unicode") for n in nodes)
    title = title_override or (tree.cssselect("title")[0].text_content() if tree.cssselect("title") else "Untitled")

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp:
        tmp.write(cleaned_html)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ["/usr/local/bin/pandoc", "-f", "html", "-t", "gfm", "--wrap=none", tmp_path],
            capture_output=True, text=True, check=True,
        )
        md = result.stdout
    finally:
        Path(tmp_path).unlink(missing_ok=True)

    # Strip residual inline HTML attributes / class soup
    md = re.sub(r'\{[^}]*\}', '', md)
    md = re.sub(r'<div[^>]*>|</div>', '', md)
    md = re.sub(r'<span[^>]*>|</span>', '', md)
    # Drop inline base64 images entirely (decorative SVG icons)
    md = re.sub(r'<img\s+src="data:image/[^"]*"[^>]*/?>', '', md)
    # Convert <a href="X" ...>text</a> → [text](X), preserving the URL
    md = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', md, flags=re.DOTALL)
    # Strip remaining standalone tags
    md = re.sub(r'<u>|</u>', '', md)
    md = re.sub(r'<em>|</em>', '*', md)
    md = re.sub(r'<strong>|</strong>', '**', md)
    # Strip remaining img tags (non-base64 CDN images we don't want to embed)
    md = re.sub(r'<img\s+[^>]*/?>', '', md)
    md = re.sub(r'\n{3,}', '\n\n', md)
    # Truncate at common "related posts" markers — these are template noise, not article body
    for cutoff in ('## Keep reading', '## Related', '## More from', '## Continue reading'):
        idx = md.find(cutoff)
        if idx > 200:  # safety: only truncate if cutoff appears past header noise
            md = md[:idx].rstrip() + '\n'
            break

    header = [f"# {title}\n"]
    if url:
        header.append(f"> Source URL: {url}\n")
    header.append(f"> Extracted from: {src.name}\n> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)\n")

    dst.write_text("\n".join(header) + "\n" + md, encoding="utf-8")
    print(f"wrote {dst} — title: {title!r} | output size: {len(md)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
