# AI Prompt Optimizer (AI提示词优化器)

一个基于 AI 的提示词优化工具，帮助用户生成更有效的 AI 提示词。

## 功能特点

- 🎯 智能优化提示词
- 💡 提供详细的优化建议
- 🔄 实时优化反馈
- 📝 优化历史记录
- 🎨 美观的用户界面

## 技术栈

- Python 3.10+
- Streamlit
- OpenAI API
- Pandas

## 本地开发设置

### 1. 克隆项目

git clone <your-repository-url>

git clone <your-repository-url>

cd ai-prompt-optimizer

### 2. 创建虚拟环境

# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

### 3. 安装依赖

pip install -r requirements.txt

### 4. 配置环境变量

1. 在项目根目录创建 `.env` 文件
2. 添加以下配置：

OPENAI_API_KEY=your-api-key-here
OPENAI_API_BASE=https://api.siliconflow.cn/v1/

### 5. 运行项目

streamlit run app.py

## 部署说明

### Zeabur 部署步骤

1. 在 Zeabur 控制台创建新项目
2. 连接 GitHub 仓库
3. 在项目设置中添加环境变量：
   - `OPENAI_API_KEY`
   - `OPENAI_API_BASE`（可选）
4. 部署项目

### 其他部署方式

- 使用 Docker 部署
- 使用 Kubernetes 部署
- 使用 AWS 部署
- 使用 Azure 部署
- 使用 Google Cloud 部署

## 项目结构

- `app.py` - 主应用文件
- `prompt.py` - 提示词优化逻辑
- `requirements.txt` - 依赖列表
- `README.md` - 项目说明

## 贡献者

- [@your-github-username](https://github.com/your-github-username)

## 许可证

MIT

## 致谢

- [OpenAI](https://openai.com)
- [Streamlit](https://streamlit.io)
- [Pandas](https://pandas.pydata.org)
- [Zeabur](https://zeabur.com)
   