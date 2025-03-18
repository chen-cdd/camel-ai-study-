# CAMEL AI 学习笔记

本仓库记录了学习 CAMEL (Communicative Agents for "Mind" Exploration of Large Language Model Society) 框架的过程和示例代码。CAMEL 是一个用于构建 AI 智能体社会的开源框架。

## 项目结构
.
├── Modelfile              # Modelfile 配置文件
├── ai_society            # AI 社会模拟相关代码
│   ├── role_playing.py   # 角色扮演示例
│   └── test.ipynb       # 测试文件
├── chapter2              # 基础消息处理
│   ├── message.py        # 基本消息示例
│   ├── dif-messag.py    # 不同类型消息示例
│   └── multi.py         # 多模态消息示例
├── chapter3              # 高级特性实现
│   ├── 1.agent.ipynb    # Agent 基础示例
│   ├── 1.1agent.py      # Agent 基础实现
│   ├── 2.agent_ad.py    # Agent 进阶应用
│   ├── 3.CrticAgent.py  # 评论家 Agent 实现
│   ├── 4.1workforce.ipynb # 工作组 Jupyter 示例
│   └── 4.workfore.py    # 工作组实现
├── chat-agent           # 聊天 Agent 实现
│   ├── ChatAgentResponse.py # Agent 响应处理
│   ├── direct.py        # 直接对话实现
│   ├── CoT_agent.py     # Chain of Thought Agent
│   └── basemessage.py   # 基础消息处理
├── tools                # 工具集成示例
│   └── math.ipynb       # 数学计算工具示例
└── tryTools             # 自定义工具实现
├── fiction_tools.py # 小说推荐工具
└── main.py         # 工具使用示例


## 主要功能模块

### 1. AI 社会模拟 (ai_society)
- **角色扮演系统**: 实现了基于 CAMEL 的多智能体角色扮演
- **测试环境**: 提供完整的测试用例和环境配置

### 2. 基础消息处理 (Chapter 2)
- **基本消息**: 实现消息的创建、发送和接收
- **多类型消息**: 支持文本、图像等多种类型消息
- **多模态交互**: 实现多模态消息的处理机制

### 3. 高级特性 (Chapter 3)
- **基础 Agent**: 
  - Agent 的创建和初始化
  - 基本对话能力实现
- **进阶应用**: 
  - 复杂任务处理
  - 多轮对话管理
- **评论家系统**: 
  - 实现对话质量评估
  - 提供改进建议
- **工作组系统**: 
  - 多 Agent 协作
  - 任务分配和管理

### 4. 聊天 Agent (chat-agent)
- **直接对话**: 实现基本的问答交互
- **CoT 推理**: 实现基于思维链的推理过程
- **响应处理**: 规范化的响应格式和处理机制

### 5. 工具集成
- **数学工具**: 实现基本的数学计算功能
- **小说推荐**: 自定义的小说推荐系统

## 环境要求

- Python 3.11+
- CAMEL AI 框架
- 通义千问模型 API 访问权限
