# 智能化网络与Windows/Linux运维平台



## 平台说明

本平台集自然语言AI、网络设备、Windows/Linux服务器和VMware虚拟机于一体，自动化运维能力强大，适合企业自运维及二次开发。

```
network-AI-autoyun-system/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── ai.py
│   │   ├── network.py
│   │   ├── server.py
│   │   └── vmware.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ai.py
│   │   ├── network/
│   │   │   ├── __init__.py
│   │   │   ├── cisco.py
│   │   │   ├── juniper.py
│   │   │   ├── arista.py
│   │   │   ├── huawei.py
│   │   │   ├── h3c.py
│   │   │   ├── f5.py
│   │   │   ├── generic.py
│   │   │   └── autodetect.py
│   │   ├── server.py
│   │   └── vmware.py
│   └── utils/
│       ├── __init__.py
│       └── security.py
├── db/
│   └── schema.sql
├── .env
├── requirements.txt
└── README.md
```

## 快速部署

### 1. 系统准备

- Ubuntu 22.04 LTS
- Python 3.10+
- PostgreSQL 14+
- Node.js（如需前端）

### 2. 安装依赖

```bash
sudo apt update
sudo apt install python3-pip python3-venv postgresql postgresql-contrib git
pip install -r requirements.txt
```

### 3. 数据库初始化

```bash
sudo -u postgres psql
CREATE DATABASE netaiplat;
CREATE USER netaiuser WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE netaiplat TO netaiuser;
\q
psql -U netaiuser -d netaiplat -f db/schema.sql
```

### 4. 配置环境变量

编辑 `.env` 文件，填入数据库、OpenAI、VMware等密钥。

### 5. 启动服务

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## AI大模型支持
- OpenAI gpt-3.5-turbo
- DeepSeek
- 豆包（BigModel）  
接口任选，调用格式见`/ai/ask`接口，参数model可为openai、deepseek、doubot。

## 网络设备支持
- Cisco: IOS, IOS-XE, IOS-XR, NX-OS, WLC, ASA/FTD
- Juniper: JunOS
- Arista: EOS
- F5: BIG-IP
- Huawei/H3C: 交换机、路由器、防火墙
- 自动识别设备类型，自动适配命令执行

...

## API接口说明

- `/ai/ask`      -- 问AI助手
- `/network/devices/` -- 管理网络设备
- `/network/command/` -- 网络设备命令
- `/server/linux/`    -- Linux服务器命令
- `/server/windows/`  -- Windows服务器命令
- `/vmware/listvms/`  -- 列出VMware虚拟机

## 二次开发建议

- 集成LDAP/AD，完善权限管理。
- 增加作业调度、运维编排、告警联动。
- 拓展支持Kubernetes、Docker等云原生环境。
- 前端可用React、Vue等开发，直接调用API即可。

## 技术交流群

如需源码、定制开发、技术支持可联系作者：your@email.com

