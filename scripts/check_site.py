#!/usr/bin/env python3
"""Check local HTML/CSS links and image references without network dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = ['index.html', 'people.html', 'publications.html', 'teaching.html', 'contact.html']

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.references = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        for key in ('src', 'href', 'poster'):
            if attrs.get(key):
                self.references.append(attrs[key])
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            match = re.search(r'url\s*=\s*(.+)', attrs.get('content', ''), re.I)
            if match:
                self.references.append(match[1])

def local_target(source, reference):
    url = urlsplit(reference)
    if url.scheme or url.netloc:
        return None
    path = unquote(url.path)
    if path.startswith('/lab/'):
        target = ROOT / path[5:]
    elif path.startswith('/'):
        return None
    else:
        target = source.parent / path if path else source
    target = target.resolve()
    if not target.is_relative_to(ROOT):
        return None
    if target.is_dir():
        target /= 'index.html'
    return target, unquote(url.fragment)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--include-archive', action='store_true', help='Also report historical missing resources in archived pages')
    args = parser.parse_args()
    queue = [ROOT / page for page in PAGES]
    queue += [p for p in ROOT.rglob('*.html') if not p.is_relative_to(ROOT / 'archive')]
    if args.include_archive:
        queue += list((ROOT / 'archive').rglob('*.html')) + list((ROOT / 'archive').rglob('*.css'))
    seen, errors, historical = set(), [], []
    while queue:
        source = queue.pop()
        if source in seen or source.suffix not in ('.html', '.css'):
            continue
        seen.add(source)
        text = source.read_text()
        references = Document(text).references if source.suffix == '.html' else [v.strip('"\' ') for v in re.findall(r'url\(([^)]+)\)', text)]
        for reference in references:
            resolved = local_target(source, reference)
            if resolved is None:
                continue
            target, fragment = resolved
            failure = None
            if not target.is_file():
                failure = 'missing ' + str(target.relative_to(ROOT))
            elif fragment and target.suffix == '.html' and fragment not in Document(target.read_text()).ids:
                # Compatibility entrypoints forward their fragments to the archived page.
                if 'http-equiv="refresh"' not in target.read_text():
                    failure = 'missing anchor ' + reference
            if failure:
                entry = str(source.relative_to(ROOT)) + ': ' + failure
                (historical if source.is_relative_to(ROOT / 'archive') else errors).append(entry)
            elif target.suffix in ('.html', '.css') and (args.include_archive or not target.is_relative_to(ROOT / 'archive')):
                queue.append(target)
    for entry in sorted(set(historical)):
        print('ARCHIVE:', entry)
    for entry in sorted(set(errors)):
        print('ERROR:', entry)
    print(f'Checked {len(seen)} HTML/CSS files; {len(set(errors))} active errors; {len(set(historical))} historical warnings.')
    return bool(errors)

if __name__ == '__main__':
    sys.exit(main())
