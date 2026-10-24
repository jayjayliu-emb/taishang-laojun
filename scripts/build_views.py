"""Build reader and standalone Bot views from the maintained skill files."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ORDER = ['taishang-laojun', 'tslj-select', 'tslj-idea', 'tslj-open', 'tslj-script', 'tslj-title', 'tslj-monetize']

def body(path):
    text = path.read_text(encoding="utf-8")
    if text.startswith('---\n'):
        text = text.split('---\n', 2)[2]
    return text.strip()

def render(bot=False):
    sources = [ROOT / 'skills' / name / 'SKILL.md' for name in ORDER]
    sources += [ROOT / 'skills/taishang-laojun/references' / (name + '.md') for name in
                ['flavor-interview', 'material-card', 'deai-rulebook', 'edit-six-cuts', 'feedback-review', 'creator-perspective']]
    parts = []
    for path in sources:
        def link(match):
            label, target = match.groups()
            if '://' in target or target.startswith('#'):
                return match.group(0)
            if bot:
                return label + '（见本文件相应章节）'
            import os
            relative = os.path.relpath(path.parent / target, ROOT / 'docs').replace("\\", "/")
            return f'[{label}]({relative})'
        parts.append(re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, body(path)))
    if bot:
        heading = ('# 太上老君·AI炼丹炉：Bot完整流程\n\n'
                   '本文自包含。下面“读取模块/参考”均指本文件内对应章节，不要求另找仓库路径。'
                   '按需使用章节，不按目录顺序逐项执行。宿主权限和用户请求优先；无工具能力时不假装执行。'
                   '本文件由技能源生成，不要单独维护另一套规则。\n\n')
        parts.append('## 分发许可与第三方说明\n\n' + '本体版权归柳爷，许可 CC BY-NC 4.0：https://creativecommons.org/licenses/by-nc/4.0/ 。项目：https://github.com/liuhaisi2026212-maker/taishang-laojun 。本修订调整了流程与适用条件，第三方许可如下。' + '\n\n' + (ROOT/'THIRD-PARTY-NOTICES.md').read_text(encoding="utf-8"))
    else:
        heading = ('# 炼丹炉配方全集\n\n由技能源生成的人读版；案例经验和推导不等于所有赛道效果验证。'
                   '使用时按当前请求选章节，不要求完整走完所有模块。\n\n')
    return (heading + '\n\n---\n\n'.join(parts)).rstrip() + '\n'

def main():
    (ROOT/'docs/formulas.md').write_text(render(), encoding="utf-8")
    (ROOT/'bot-prompt/liuye-bot-prompt.md').write_text(render(True), encoding="utf-8")
    refs = ROOT/'skills/taishang-laojun/references'
    for name in ['LICENSE', 'THIRD-PARTY-NOTICES.md']:
        (refs/name).write_text((ROOT/name).read_text(encoding="utf-8"), encoding="utf-8")

if __name__ == '__main__':
    main()
