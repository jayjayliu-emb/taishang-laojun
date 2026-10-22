# 太上老君·AI炼丹炉（taishang-laojun）

> **别人的爆款，都是你炼丹的原料。太上老君AI炼丹炉——把你的选题喂进去，炼出能火的视频。**

「太上老君·AI炼丹炉」是一套教 AI 帮内容创作者做事的技能包（Skills）。把创作者"柳爷"的真实爆款复盘（50万播放/88万播放等真实案例）炼成可执行的判断标准，任何支持 Skills 的智能体安装后，在对话框里直接就能用。

## 一图看懂炼丹炉

**点击下方链接，直接看交互式全景图**（浏览器打开，点模块展开细节）：

- ▶ **[在线预览 · 交互式思维导图](https://raw.githack.com/liuhaisi2026212-maker/taishang-laojun/main/docs/mindmap/preview.html)**
- ▶ **[备用预览链接](https://htmlpreview.github.io/?https://raw.githubusercontent.com/liuhaisi2026212-maker/taishang-laojun/main/docs/mindmap/preview.html)**

（本地文件也可以直接打开：`docs/mindmap/炼丹炉全景图.html`）

## 它能做什么

**先认识你，再帮你炼丹。** 第一步先弄清三件事：

- **你是谁**：行业 / 账号定位
- **给谁看**：目标客户长什么样
- **你在哪一步**：有对标？有选题？有稿？拍完？剪完？还是要变现？

不了解使用者就出选题、出标题，等于闭眼炼丹——所以炉子会先问你这些，再按需输出能直接开拍的东西：

- **选题 ×3**：给谁看、为什么能拍、标题示例（不是十个用不上的泛选题）
- **开头改写稿**：前 2 秒钩子原话 + 第二画面证据链
- **标题 ×3**：按"跟我有关"三源出，每条附理由
- **拍摄清单**：场景/画面/动作
- **验证标注**：已验证 vs 待验证（不虚构、不吹牛）

输入可以是：一条对标的视频/逐字稿、一个场景、一个热点、或一句"我想拍点什么"。

## 核心方法（来自真实爆款复盘）

| 模块 | 名称 | 一句话 |
|---|---|---|
| 选材 | 掂量三关 | 复读测试（口吻像不像我）→ 客户测试（目标客户会不会点头）→ 替换测试（形式换成我的能不能做到） |
| 看火 | 选题五要素 | 人群广 × 认知基础 × 心理钩子 × 事实可验证 × 低门槛 |
| 开炉 | 五段式骨架 | 钩子 → 证据 → 承诺 → 条件 → 指令 |
| 开炉 | 勾证衔接 | 开头负责勾，第二个画面负责证，勾和证之间不能断 |
| 收丹 | 跟我有关三源 | 认人（名人）/ 认事（共识）/ 认心（观众潜意识里藏着的想法） |
| 回炉 | 借观点不借脉络 | 观点相同没问题，流程脉络大差不差会被扒 |
| 成丹 | 合规承接 | GitHub 开源/公开产品承接，禁私聊引流 |

## 怎么安装

| 智能体 | 安装方式 |
|---|---|
| 豆包 / 豆包工作 | 把 `skills/` 目录复制到技能目录即可（零适配） |
| Claude Code | 复制 `skills/` + 配置 `.claude-plugin/marketplace.json` |
| Codex | 复制 `skills/` + `AGENTS.md` 入口 |
| Grok | 复制 `skills/`（Grok Build 支持） |
| 生成 Bot（豆包 Bot / Coze 等） | 用 `bot-prompt/liuye-bot-prompt.md` 直接粘贴为 system prompt |

详细见 [docs/install-guide.md](docs/install-guide.md)。

## 仓库结构

```text
taishang-laojun/
├── README.md
├── AGENTS.md                 # 多智能体薄入口
├── skills/
│   ├── taishang-laojun/      # 总入口（炉子调度台）
│   ├── tslj-select/          # 选材：对标筛选（掂量三关）
│   ├── tslj-idea/            # 看火：选题判断
│   ├── tslj-open/            # 开炉：开头/结构
│   ├── tslj-title/           # 收丹：标题
│   ├── tslj-script/          # 回炉：文案转写
│   └── tslj-monetize/        # 成丹：变现承接
├── bot-prompt/               # 给 Bot 平台的 system prompt
└── docs/
    ├── install-guide.md
    ├── formulas.md           # 配方全集（人读版）
    └── mindmap/              # 炼丹炉全景图（浏览器打开）
```

## 项目背景

- 创作者：柳爷（抖音"柳爷不迷糊"，AI 内容创作者/视频操盘手）
- 方法来源：真实爆款视频复盘（Claude封号 20万+/Grok上手指南 10万+/海边 500+粉/机场置顶/扣袋 88万/一人公司 11万/世界杯 18万/AI打工仔 50万+涨粉四五千）
- 结构借鉴：dbskill（dontbesilent2025）的开源 Skills 设计；方法内容全部为柳爷原创复盘

## License

本仓库以 [CC BY-NC 4.0](LICENSE)（署名-非商业性使用）开源。结构设计借鉴 dbskill（CC BY-NC 4.0），方法内容版权归作者所有。
