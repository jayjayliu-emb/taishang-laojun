# 炼丹炉项目入口

用户要求选题、参考适配、开头、成稿、标题或反馈复盘时，先读 `skills/taishang-laojun/SKILL.md` 和其中的炉心 `references/core-mind.md`，再按目标读取必要模块。已有材料不重复询问；交付只覆盖当前请求。总入口负责衔接，叶子负责明确结果。

核心是教判断思路并帮助用户做出自己的内容，不是复制爆款模板。事实、适用条件、来源与个人素材边界遵循总入口；不要把本仓库当自动发布、安装、抓取或跨会话保存授权。

维护者更新规则后运行 `python3 scripts/build_views.py` 同步人读版、Bot 与全景图（全景图文字在 `scripts/build_mindmap.py`），再运行 `python3 scripts/check_package.py` 检查分发引用。规则真源是技能文件及其 references，不在生成副本里单独改方法。
