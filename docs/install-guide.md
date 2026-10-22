# 安装指南：把炼丹炉装进你的智能体

> 太上老君·AI炼丹炉 是一套**跨智能体**技能包。内容只维护一份（`skills/`），各家智能体各装各的入口。下面是每种装法。

---

## 一、豆包 / Doubao Work（零适配，直接复制）

豆包支持从本地 skills 目录发现技能。

1. 把 `skills/` 下的全部目录（`taishang-laojun`、`tslj-select`、`tslj-idea`、`tslj-open`、`tslj-title`、`tslj-script`、`tslj-monetize`）复制到豆包的技能目录（`.doubaowork/agent_mode/workspace/.user_skills/` 或客户端对应位置）。
2. 重启豆包。之后你只要说"帮我选题/写标题/改开头/想变现"，豆包就会自动路由到对应模块。
3. 不想装整套？把 `skills/taishang-laojun/SKILL.md` 单独复制进去，也有完整路由能力（模块缺了它会提示）。

## 二、Claude Code（加 marketplace）

1. 项目里已带 `.claude-plugin/marketplace.json`，在 Claude Code 中把本仓库作为 marketplace 添加：
   ```bash
   claude plugin marketplace add <本仓库地址>
   claude plugin install tslj@<本仓库地址>
   ```
2. 或把 `skills/` 目录复制进 `~/.claude/skills/`。
3. Claude Code 会读取 `AGENTS.md` 作为项目入口规则。

## 三、Codex（读 AGENTS.md）

Codex 支持项目级规则文件。把本仓库作为项目打开即可——Codex 会读取根目录 `AGENTS.md`，按其中规则调用 `skills/` 里的技能。

## 四、Grok / 其他支持 Skills 的 Agent

- 支持 Skills 目录的 Agent：复制 `skills/` 即可，零适配。
- 不支持 Skills、只支持 system prompt 的 Agent/Bot 平台（Grok 生成 bot、扣子等）：用 `bot-prompt/liuye-bot-prompt.md` —— 整段粘贴成 system prompt，它就变成炼丹炉。

## 五、人读版

不装任何东西，直接看：
- 方法全集：`docs/formulas.md`
- 直播/视频/沙龙讲稿：`docs/presentation-outline.md`
- 一图看懂：`docs/mindmap/炼丹炉全景图.html`（浏览器打开）

---

## 验证装好了没有

对任意智能体说一句话：**"我想拍个视频但不知道拍什么"**。
- 装好了：它会进入"看火"模块，出 3 个选题菜单让你选。
- 没装上：它只会泛泛回答"你可以拍你擅长的……"——这时检查安装位置。

## 常见问题

**Q：只装总入口够吗？**
够。总入口会按状态路由，缺模块时会告诉你该用哪个模块、为什么。

**Q：想给客户用但客户不装技能怎么办？**
用 Bot 版（`bot-prompt/`）——任何平台粘贴即用，零门槛。

**Q：能商用吗？**
项目是 CC BY-NC 4.0（署名-非商业性使用）。你自己用、给客户做服务没问题；不能把技能包本身拿去转卖或商用分发。
