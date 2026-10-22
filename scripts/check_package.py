"""Verify portable skill references and generated views without installing anything."""
from pathlib import Path
import json
import re
import shutil
import tempfile
from build_views import ROOT, ORDER, render

def check():
    errors = []
    market = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text(encoding="utf-8"))
    plugin = json.loads((ROOT/'.claude-plugin/plugin.json').read_text(encoding="utf-8"))
    if not isinstance(market.get('owner'), dict) or not isinstance(market.get('plugins'), list):
        errors.append('Invalid marketplace owner/plugins')
    if market['plugins'][0]['name'] != plugin['name'] or market['plugins'][0]['version'] != plugin['version']:
        errors.append('Plugin identity/version mismatch')
    with tempfile.TemporaryDirectory() as tmp:
        installed = Path(tmp)/'skills'
        shutil.copytree(ROOT/'skills', installed)
        for name in ORDER:
            entry = installed/name/'SKILL.md'
            text = entry.read_text(encoding="utf-8")
            if not text.startswith('---\n') or f'name: {name}\n' not in text.split('---\n', 2)[1]:
                errors.append(f'Missing skill identity: {name}')
        for path in installed.rglob('*.md'):
            # Third-party notice contains descriptive root paths, not runtime links.
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text(encoding="utf-8")):
                if '://' in target or target.startswith('#'):
                    continue
                dest = (path.parent/target.split('#')[0]).resolve()
                if not dest.is_relative_to(installed.resolve()) or not dest.is_file():
                    errors.append(f'Broken isolated-install reference: {path.relative_to(installed)} -> {target}')
    for filename, content in [('docs/formulas.md', render()), ('bot-prompt/liuye-bot-prompt.md', render(True))]:
        if (ROOT/filename).read_text(encoding="utf-8") != content:
            errors.append(f'Stale generated view: {filename}')
    for name in ['LICENSE', 'THIRD-PARTY-NOTICES.md']:
        if (ROOT/'skills/taishang-laojun/references'/name).read_bytes() != (ROOT/name).read_bytes():
            errors.append(f'Stale distribution notice: {name}')
    # Also verify repository Markdown links, including documentation entry points.
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text(encoding="utf-8")):
            if '://' not in target and not target.startswith('#'):
                if not (path.parent/target.split('#')[0]).exists():
                    errors.append(f'Broken repository link: {path.relative_to(ROOT)} -> {target}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('PASS: 7 skill identities, isolated copied-package references, repository links, synchronized views and notices')

if __name__ == '__main__':
    check()
