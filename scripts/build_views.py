"""Build reader and standalone Bot views from the maintained skill files."""
from pathlib import Path
import os
import re

import build_mindmap

ROOT = Path(__file__).resolve().parents[1]
ORDER = ['taishang-laojun', 'tslj-select', 'tslj-idea', 'tslj-open', 'tslj-script', 'tslj-title', 'tslj-monetize']

def body(path):
    text = path.read_text(encoding="utf-8")
    if text.startswith('---\n'):
        text = text.split('---\n', 2)[2]
    return text.strip()

REFERENCES = ['core-mind', 'case-book', 'flavor-interview', 'material-card', 'deai-rulebook', 'edit-six-cuts', 'feedback-review']
LITE = ['taishang-laojun', 'core-mind'] + ORDER[1:]
LICENSE_NOTE = ('本体版权归柳爷，许可 CC BY-NC 4.0：https://creativecommons.org/licenses/by-nc/4.0/ 。'
                '项目：https://github.com/liuhaisi2026212-maker/taishang-laojun 。')


def sources(lite=False):
    paths = [ROOT / 'skills' / name / 'SKILL.md' for name in ORDER]
    paths += [ROOT / 'skills/taishang-laojun/references' / (name + '.md') for name in REFERENCES]
    if lite:
        paths = [p for p in paths if (p.parent.name if p.name == 'SKILL.md' else p.stem) in LITE]
        paths.insert(1, paths.pop(-1))  # core-mind right after the entry
    return paths


def render(bot=False, lite=False):
    included = {p.resolve() for p in sources(lite)}
    parts = []
    for path in sources(lite):
        def link(match):
            label, target = match.groups()
            if '://' in target or target.startswith('#'):
                return match.group(0)
            if bot:
                if (path.parent / target).resolve() in included:
                    return label + '（见本文件相应章节）'
                return label + '（完整版 Bot 文件 liuye-bot-prompt.md 中有该章节）'
            relative = os.path.relpath(path.parent / target, ROOT / 'docs').replace("\\", "/")
            return f'[{label}]({relative})'
        parts.append(re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, body(path)))
    if lite:
        heading = ('# 太上老君·AI炼丹炉：Bot精简版\n\n'
                   '适合系统提示词有长度限制的智能体（如各类 Bot 的人设设定框）。包含总入口、炉心和六个模块；'
                   '案例库、访谈、去AI味、改稿六刀和复盘细则在完整版 Bot 文件里，可作为知识库附件一起上传。'
                   '本文件由技能源生成，不要单独维护另一套规则。\n\n')
        parts.append('## 许可\n\n' + LICENSE_NOTE + '第三方声明见完整版。')
    elif bot:
        heading = ('# 太上老君·AI炼丹炉：Bot完整流程\n\n'
                   '本文自包含。下面“读取模块/参考”均指本文件内对应章节，不要求另找仓库路径。'
                   '按需使用章节，不按目录顺序逐项执行。宿主权限和用户请求优先；无工具能力时不假装执行。'
                   '本文件由技能源生成，不要单独维护另一套规则。\n\n')
        parts.append('## 分发许可与第三方说明\n\n' + LICENSE_NOTE + '本修订调整了流程与适用条件，第三方许可如下。'
                     + '\n\n' + (ROOT/'THIRD-PARTY-NOTICES.md').read_text(encoding="utf-8"))
    else:
        heading = ('# 炼丹炉配方全集\n\n由技能源生成的人读版；案例经验和推导不等于所有赛道效果验证。'
                   '使用时按当前请求选章节，不要求完整走完所有模块。\n\n')
    return (heading + '\n\n---\n\n'.join(parts)).rstrip() + '\n'


GENERATED = {'docs/formulas.md': lambda: render(),
             'bot-prompt/liuye-bot-prompt.md': lambda: render(True),
             'bot-prompt/liuye-bot-lite.md': lambda: render(True, True)}


def main():
    for name, build in GENERATED.items():
        (ROOT/name).write_text(build(), encoding="utf-8")
    build_mindmap.main(ROOT)
    refs = ROOT/'skills/taishang-laojun/references'
    for name in ['LICENSE', 'THIRD-PARTY-NOTICES.md']:
        (refs/name).write_text((ROOT/name).read_text(encoding="utf-8"), encoding="utf-8")

if __name__ == '__main__':
    main()
