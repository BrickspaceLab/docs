#!/usr/bin/env python3
"""Check the repository's Knowing publication contract without network access."""
import html
import json
import pathlib
import re
import subprocess
import sys
import urllib.parse
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent


def body(source):
    return re.sub(r'^---\n.*?\n---\n', '', source, count=1, flags=re.S)


def without_code(source):
    # Ignore fenced examples and inline code, including literal Liquid examples.
    source = re.sub(r'^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', source, flags=re.M | re.S)
    return re.sub(r'`+[^`\n]*`+', '', source)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = []

    def handle_starttag(self, tag, attrs):
        self.values.extend(value for name, value in attrs if name in ('href', 'src') and value)


def links(source):
    parser = Links()
    parser.feed(source)
    values = parser.values
    for match in re.finditer(r'!?\[[^\]\n]*\]\((<[^>]+>|[^\s()]+(?:\([^()]*\)[^\s()]*)*)(?:\s+["\'][^\n]*?["\'])?\)', source):
        values.append(html.unescape(match[1].strip('<>')))
    values.extend(re.findall(r'\{%\s*(?:content-ref|embed|file)\s+url=["\']([^"\']+)', source))
    return values


def target_for(page, value):
    url = urllib.parse.urlsplit(value)
    if url.scheme or url.netloc or not url.path:
        return None
    return (page.parent / urllib.parse.unquote(url.path)).resolve()


def check():
    paths = subprocess.check_output(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=ROOT
    ).decode().split('\0')
    pages = {}
    errors = []
    for name in dict.fromkeys(paths):
        if not name.endswith('.md'):
            continue
        page = ROOT / name
        source = page.read_text()
        if re.search(r'^published: false$', source.split('---', 2)[1] if source.startswith('---\n') else '', re.M):
            continue
        pages[page.resolve()] = source
        content = without_code(body(source))
        if len(re.findall(r'^# ', content, re.M)) != 1:
            errors.append(f'{name}: expected exactly one H1 outside code')
        metadata = re.match(r'^---\n(.*?)\n---\n', source, re.S)
        if not metadata or not re.search(r'^index: \d+$', metadata[1], re.M):
            errors.append(f'{name}: missing integer navigation index')
        for key in ('title', 'published', 'navigation', 'index', 'tier'):
            if metadata and len(re.findall(r'^' + key + ':', metadata[1], re.M)) > 1:
                errors.append(f'{name}: duplicate {key} metadata')
        if re.search(r'broken://|/broken/pages/|app\.gitbook\.com|data-action="ask"', content):
            errors.append(f'{name}: unresolved GitBook link or action')
        stack = []
        containers = {'hint', 'stepper', 'step', 'code', 'prompt', 'tabs', 'tab', 'updates', 'update', 'content-ref'}
        for token in re.finditer(r'\{%\s*([\w-]+)\b[^%]*%\}', content):
            kind = token[1]
            if kind in containers:
                stack.append(kind)
            elif kind.startswith('end') and kind[3:] in containers:
                if not stack or stack.pop() != kind[3:]:
                    errors.append(f'{name}: mismatched {kind} block')
        if stack:
            errors.append(f'{name}: unclosed blocks: {stack}')
        for value in links(content):
            target = target_for(page, value)
            if target is None:
                continue
            if not target.is_relative_to(ROOT):
                errors.append(f'{name}: link escapes repository: {value}')
            elif not target.exists():
                errors.append(f'{name}: missing target: {value}')
            elif target.is_dir():
                errors.append(f'{name}: use an explicit README.md: {value}')
            elif target.suffix == '.md' and target not in pages:
                # The target may be visited later; check its metadata directly.
                if re.search(r'^published: false$', target.read_text().split('---', 2)[1] if target.read_text().startswith('---\n') else '', re.M):
                    errors.append(f'{name}: link to unpublished page: {value}')
    inventory = json.loads((ROOT / '.migration/live-pages.json').read_text())
    for item in inventory:
        if (ROOT / item['path']).resolve() not in pages:
            errors.append(f"Live page missing from publication: {item['url']}")
    sizes = [len(source.encode()) for source in pages.values()]
    if len(paths) > 1000 or sum(sizes) > 10 * 1024 * 1024 or max(sizes, default=0) > 500 * 1024:
        errors.append('Repository exceeds Knowing sync limits')
    for error in errors:
        print(error)
    print(f'{len(pages)} published pages; {len(inventory)} live pages covered; {sum(sizes):,} Markdown bytes; {len(errors)} errors.')
    return bool(errors)


if __name__ == '__main__':
    assert links('[Page](../a.md) <img src="img%20one.png">') == ['img%20one.png', '../a.md']
    assert without_code('```liquid\n{% hint %}\n```\n# Title') == '\n# Title'
    assert body('---\nindex: 0\n---\n# Title') == '# Title'
    sys.exit(check())
