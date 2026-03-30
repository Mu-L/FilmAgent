<p align="center">
  <img src="aigc-director-pics/banner.png" width="100%" />
</p>

<h2 align="center">
  AIGC-Claw: AI 创意视频生成员工
</h2>

<h4 align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue.svg" alt="Version">
  <a href="https://github.com/HITsz-TMG/AIGC-Claw/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/HITsz-TMG/AIGC-Claw?style=flat-square" alt="License">
  </a>
  <a href="https://github.com/HITsz-TMG/AIGC-Claw/stargazers">
    <img src="https://img.shields.io/github/stars/HITsz-TMG/AIGC-Claw?style=flat-square&logo=github" alt="Stars">
  </a>
  <a href="https://github.com/HITsz-TMG/AIGC-Claw/fork">
    <img src="https://img.shields.io/github/forks/HITsz-TMG/AIGC-Claw?style=flat-square&logo=github" alt="Forks">
  </a>
  <img src="https://img.shields.io/badge/Python-3.9+-purple.svg" alt="Python">
  <a href="#openclaw-integration">
    <img src="https://img.shields.io/badge/OpenClaw-Compatible-ff4444?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6IiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg==" alt="OpenClaw Compatible">
  </a>
</h4>

<p align="center">
  <b><i><font size="5">直接与 <a href="#方式二openclaw-自动配置">OpenClaw</a> 对话："研究 X" → 搞定。</font></i></b>
</p>

<div align="center">

🎬  [**视频演示**](https://www.youtube.com/@imryanxu)  📖  [**集成指南**](#方式二openclaw-自动配置)  🦀  [**ClawHub**](https://clawhub.ai/hit-cxf/aigc-director)

<a href="https://trendshift.io/repositories/12871" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12871" alt="HITsz-TMG%2FFilmAgent | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

---

## 💥 News

- `2026/3/27`: 🚀 AIGC-Claw 正式发布，支持视频生成全流程

---



## 📖 项目介绍

AIGC-Claw 是一个 AI 创意视频生成系统。你只需要输入一个创意主题，系统会将其转化为可交付的视频作品。

流程覆盖完整影视制作链路：剧本创作、角色设计、分镜规划、参考图生成、视频生成、后期剪辑。每个阶段都会产出可视化结果并支持确认后继续，兼顾自动化效率与可控性。

---

## 📺 AIGC-Claw 示例

<details>
<summary><b>Web 前端界面</b></summary>
<div align="center">

| | |
|:---:|:---:|
| ![Stage 1](./aigc-director-pics/workflow_demo/stage_1.png) | ![Stage 2](./aigc-director-pics/workflow_demo/stage_2.png) |
| ![Stage 3](./aigc-director-pics/workflow_demo/stage_3.png) | ![Stage 4](./aigc-director-pics/workflow_demo/stage_4.png) |
| ![Stage 5](./aigc-director-pics/workflow_demo/stage_5.png) | ![Stage 6](./aigc-director-pics/workflow_demo/stage_6.png) |

</div>
</details>

<details>
<summary><b>微信交互</b></summary>
<div align="center">

| | | | |
|:---:|:---:|:---:|:---:|
| ![WeChat 1](./aigc-director-pics/wechat_demo/wechat_1.jpg) | ![WeChat 2](./aigc-director-pics/wechat_demo/wechat_2.jpg) | ![WeChat 3](./aigc-director-pics/wechat_demo/wechat_3.jpg) | ![WeChat 4](./aigc-director-pics/wechat_demo/wechat_4.jpg) |

</div>
</details>

<details>
<summary><b>飞书交互</b></summary>
<div align="center">

| | | | |
|:---:|:---:|:---:|:---:|
| ![Feishu 1](./aigc-director-pics/feishu_demo/feishu_1.jpg) | ![Feishu 2](./aigc-director-pics/feishu_demo/feishu_2.jpg) | ![Feishu 3](./aigc-director-pics/feishu_demo/feishu_3.jpg) | ![Feishu 4](./aigc-director-pics/feishu_demo/feishu_4.jpg) |

</div>
</details>

## ✨ 功能特性

| 阶段 | 功能 | 描述 |
|:---:|---|---|
| 1 | 🎭 **剧本生成** | 输入创意自动生成结构化剧本，支持长视频和微电影模式 |
| 2 | 👤 **角色设计** | AI 生成角色设定图（四视图）和场景背景图 |
| 3 | 🎬 **分镜设计** | 智能拆分镜头脚本，设计镜头语言 |
| 4 | 🖼️ **参考图生成** | 为每个镜头生成高精度参考图 |
| 5 | 🎥 **视频生成** | 图生视频 / 文生视频 |
| 6 | ✂️ **后期剪辑** | 自动拼接视频片段，添加转场效果 |

---

## 🚀 快速开始

### 方式一：手动安装

```bash
# 1. 克隆项目
git clone https://github.com/HITsz-TMG/AIGC-Claw.git
cd AIGC-Claw

# 2. 配置并启动后端
cd aigc-director/aigc-claw/backend

# 创建虚拟环境并安装依赖
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 填入 API Key

# 启动后端
python api_server.py
# 服务运行在 http://localhost:8000
```

```bash
# 3. 配置并启动前端（新终端）
cd aigc-director/aigc-claw/frontend
npm install
npm run build
npm start
# 访问 http://localhost:3000
```

### 方式二：OpenClaw 自动配置

向 OpenClaw 发送消息：

```
帮我克隆git仓库：https://github.com/HITsz-TMG/AIGC-Claw.git
然后把AIGC-Claw中的aigc-director文件夹递归复制到.openclaw/workspace/skills目录下，用作AIGC相关的skill
```

使用时建议指明 "使用 aigc-director"：

```
用aigc-director来生成一个视频，内容是"一条狗的使命"
```

### 方式三：通过 ClawHub 安装

请确保本地安装了clawhub-cli

打开终端，输入命令，所有询问均选择yes

```bash
clawhub install aigc-director
```

安装完成后，ClawHub 会将 `aigc-director` 复制到 `workspace/skills`（或指定的 skills 目录）。

之后可以参考方式一手动安装自行构建项目并运行，也可以使用OpenClaw完成后续项目构建。

在第一次使用 `aigc-director` 时，如果没有手动构建项目，OpenClaw会自动构建前后端并运行，无需手动初始化（构建项目需要配置环境和编译，请耐心等待）。


---


## 📁 项目结构

```
AIGC-Claw/
├── aigc-director/                    # 🎯 OpenClaw Agent Skill
│   ├── SKILL.md                      # Agent 工作流规则定义
│   ├── CLAUDE.md                     # Claude Code 开发指引
│   ├── README.md                     # Skill 项目说明
│   ├── references/                   # API 参考文档
│   │   ├── init_project/             # 项目初始化指南
│   │   ├── run_project/              # 服务启动指南
│   │   ├── workflow/                 # 六阶段工作流 API
│   │   ├── sandbox/                  # 临时工作台 API
│   │   └── send_message/             # 消息推送集成
│   └── aigc-claw/                    # 💻 实际代码项目
│       ├── backend/                  # Python FastAPI 后端
│       │   ├── api_server.py         # API 入口
│       │   ├── core/                 # 核心模块
│       │   │   ├── orchestrator.py   # 工作流引擎
│       │   │   └── agents/           # 6 个阶段 Agent
│       │   └── tool/                 # 外部 API 客户端
│       └── frontend/                 # Next.js 前端
├── FilmAgent/                        # 🎬 原FilmAgent项目
└── README.md                         # 主 README
```

---

## 🔧 配置说明

### 环境要求

- **Python**: 3.9+
- **Node.js**: 18+
- **npm**: 9+

### 后端环境变量

在 `aigc-claw/backend/.env` 中配置：

```bash
# LLM 配置
LLM_MODEL=qwen3.5-plus
VLM_MODEL=qwen-vl-plus

# 图像生成
IMAGE_T2I_MODEL=doubao-seedream-5-0-260128
IMAGE_IT2I_MODEL=doubao-seedream-5-0-260128

# 视频生成
VIDEO_MODEL=wan2.6-i2v-flash
VIDEO_RATIO=16:9

# API Keys
DASHSCOPE_API_KEY=your_key
ARK_API_KEY=your_key
DEEPSEEK_API_KEY=your_key
```

### 可用模型

| 类型 | 模型 |
|:---:|:---|
| **LLM** | qwen3.5-plus, deepseek-chat, gpt-4o, gemini-2.5-flash |
| **VLM** | qwen-vl-plus, gemini-2.5-flash-image |
| **文生图** | doubao-seedream-5-0, jimeng_t2i_v40, wan2.6-t2i |
| **图生图** | doubao-seedream-5-0, jimeng_t2i_v40, wan2.6-image |
| **视频生成** | wan2.6-i2v-flash, kling-v3, jimeng_ti2v_v30_pro |


## 📚 系列工作

| 框架图 | 论文信息 |
|:---:|---|
| <img src="https://github.com/HITsz-TMG/FilmAgent/blob/main/pics/framework.png?raw=true" width="420" alt="FilmAgent framework"/> | **FilmAgent: Automating Virtual Film Production Through a Multi-Agent Collaborative Framework**<br>Authors: Xu, Zhenran; Wang, Jifang; Wang, Longyue; Li, Zhouyi; Shi, Senbao; Hu, Baotian; Zhang, Min<br>[[Paper](https://doi.org/10.1145/3681758.3698014)] [[GitHub](https://github.com/HITsz-TMG/AIGC-Claw/blob/main/FilmAgent.md)] |
| <img src="https://github.com/HITsz-TMG/Anim-Director/blob/main/Anim-Director/assets/visualeg.png" width="420" alt="Anim-Director result"/> | **Anim-Director: A Large Multimodal Model Powered Agent for Controllable Animation Video Generation**<br>Authors: Li, Yunxin; Shi, Haoyuan; Hu, Baotian; Wang, Longyue; Zhu, Jiashun; Xu, Jinyi; Zhao, Zhen; Zhang, Min<br>[[Paper](https://doi.org/10.1145/3680528.3687688)] [[GitHub](https://github.com/HITsz-TMG/Anim-Director/tree/main/Anim-Director)] |
| <img src="https://raw.githubusercontent.com/HITsz-TMG/Anim-Director/main/AniMaker/assets/pipeline.png" width="420" alt="AniMaker pipeline"/> | **AniMaker: Multi-Agent Animated Storytelling with MCTS-Driven Clip Generation**<br>Authors: Shi, Haoyuan; Li, Yunxin; Chen, Xinyu; Wang, Longyue; Hu, Baotian; Zhang, Min<br>[[Paper](https://doi.org/10.1145/3757377.3764009)] [[GitHub](https://github.com/HITsz-TMG/Anim-Director/tree/main/AniMaker)] |

<p align="center">
  <sub>Built with 🦞 by the HITsz-TMG team</sub>
</p>
