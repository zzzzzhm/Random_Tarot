# 🔮 Random Tarot - 随机塔罗牌网站

基于 AWS 的现代化全栈应用：React 前端 + FastAPI 后端 + Docker 容器 + GitHub Actions CI/CD + AWS EC2/S3 部署

## 🏗️ 项目架构

```
浏览器 (React)
    ↓
Nginx (反向代理)
    ↓
FastAPI (后端服务)
    ↓
SQLite/RDS (数据库)
    ↓
AWS S3 (图片存储)
```

## 🚀 快速开始

### 方案A：在 GitHub Codespaces 中开发（推荐）
```bash
# 在 GitHub 仓库页面
1. 点击 Code → Codespaces → Create codespace on main
2. 等待环境加载完成 (1分钟)
3. 在终端运行下方命令
```

### 方案B：本地 Docker 运行
```bash
git clone https://github.com/zzzzzhm/Random_Tarot.git
cd Random_Tarot
docker-compose up --build
# 打开浏览器访问 http://localhost:3000
```

### 方案C：开发环境运行

**后端**:
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**前端** (新终端):
```bash
cd frontend
npm install
npm run dev
```

## 📁 项目结构

```
Random_Tarot/
├── frontend/                    # React 应用
│   ├── src/
│   │   ├── App.jsx             # 主组件
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile
│
├── backend/                     # FastAPI 应用
│   ├── app/
│   │   ├── main.py             # 应用入口
│   │   ├── config.py           # 配置
│   │   ├── models/             # 数据模型
│   │   ├── routes/             # API 路由
│   │   └── services/           # 业务逻辑
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/                       # Nginx 配置
│   └── nginx.conf
│
├── docker-compose.yml          # 本地开发编排
├── .github/workflows/          # GitHub Actions
└── README.md
```

## 🔧 核心功能

- ✅ 随机抽塔罗牌
- ✅ 显示卡牌图片 (S3)
- ✅ 卡牌详细信息
- ✅ 抽签历史记录 (可选)

## 📦 环境变量配置

创建 `.env` 文件：
```env
# 后端
DATABASE_URL=sqlite:///./tarot.db
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
S3_BUCKET=your_bucket_name

# 前端
VITE_API_URL=http://localhost:8000
```

## 🚢 AWS 部署

### EC2 部署步骤
```bash
# 1. SSH 连接到 EC2
ssh -i "key.pem" ec2-user@your-instance-ip

# 2. 克隆仓库
git clone https://github.com/zzzzzhm/Random_Tarot.git
cd Random_Tarot

# 3. 安装 Docker
curl https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 4. 启动容器
docker-compose up -d

# 5. 配置 Nginx (包含自动化脚本)
sudo ./scripts/setup-nginx.sh
```

### S3 配置
```bash
# 创建 S3 bucket
aws s3 mb s3://tarot-images-bucket

# 上传图片
aws s3 cp ./tarot-images/ s3://tarot-images-bucket/ --recursive

# 启用公开访问 (已在 Dockerfile 中配置)
```

## 🔄 CI/CD (GitHub Actions)

推送到 main 分支自动触发：
1. ✅ 单元测试
2. ✅ Docker 镜像构建
3. ✅ 推送到 ECR/Docker Hub
4. ✅ SSH 连接 EC2 并更新

## 📚 API 文档

启动后端后，访问：
```
http://localhost:8000/docs
```

主要接口：
- `GET /api/tarot/random` - 随机抽牌
- `GET /api/tarot/all` - 获取所有卡牌
- `GET /api/tarot/{id}` - 获取卡牌详情

## 🛠️ 技术栈

| 层级 | 技术 | 版本 |
|------|------|------|
| **前端** | React | 18+ |
| 构建 | Vite | 5+ |
| **后端** | FastAPI | 0.100+ |
| 数据库 | SQLite/PostgreSQL | - |
| **容器** | Docker | 24+ |
| 编排 | Docker Compose | 2.0+ |
| **云服务** | AWS (EC2, S3, RDS) | - |
| **CI/CD** | GitHub Actions | - |

## 📝 开发指南

### 添加新卡牌
1. 编辑 `backend/app/data/tarot_cards.json`
2. 上传图片到 S3
3. 更新数据库模型

### 修改前端样式
```bash
cd frontend
npm install tailwindcss  # 或你喜欢的 CSS 框架
```

## 🐛 常见问题

**Q: 如何本地测试 AWS S3？**
```bash
pip install moto  # Mock AWS 服务
```

**Q: Docker 镜像太大？**
```bash
# 使用多阶段构建 (已在 Dockerfile 中配置)
docker build -t tarot:latest .
```

**Q: 如何配置域名？**
```nginx
# 编辑 nginx/nginx.conf
server_name yourdomain.com;
# 使用 Let's Encrypt 生成 SSL
```

## 📞 支持

如有问题，请在 GitHub Issues 提出。

## 📄 许可证

MIT License
