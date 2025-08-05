# 智能化网络与Windows/Linux运维平台
# network-AI-autoyun-system


## 平台说明

本平台集自然语言AI、网络设备、Windows/Linux服务器和VMware虚拟机于一体，自动化运维能力强大，适合企业自运维及二次开发。
一个基于 FastAPI + SQLAlchemy + PostgreSQL 的智能网络自动化运维平台，支持设备管理、批量命令、联机检测、用户认证/权限、定时任务等。



## 主要特性
- 设备CRUD、批量命令、Ping联机检测、操作日志
- 用户注册/登录，JWT认证，角色权限隔离
- APScheduler定时任务
- 自动API文档

## 目录结构
```text
app/
  ├── __init__.py
  ├── main.py
  ├── database.py
  ├── models.py
  ├── schemas.py
  ├── routers/
  │    ├── __init__.py
  │    ├── ai.py
  │    ├── network.py
  │    ├── server.py
  │    ├── vmware.py
  │    └── auth.py
  ├── services/
  │    ├── __init__.py
  │    ├── ai.py
  │    ├── server.py
  │    ├── vmware.py
  │    └── network/
  │         ├── __init__.py
  │         ├── autodetect.py
  │         ├── cisco.py
  │         ├── arista.py
  │         ├── juniper.py
  │         ├── huawei.py
  │         ├── h3c.py
  │         ├── f5.py
  │         ├── generic.py
  │         └── ping.py
  └── utils/
       ├── __init__.py
       ├── security.py
       └── scheduler.py
db/
  └── schema.sql
.env
requirements.txt
README.md
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

【修订】
- ## Ubuntu 22.04 安装步骤

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip postgresql postgresql-contrib

# 配置数据库
sudo -u postgres psql
-- 在psql终端:
CREATE USER netaiuser WITH PASSWORD 'yourpassword';
CREATE DATABASE netaiplat OWNER netaiuser;
GRANT ALL PRIVILEGES ON DATABASE netaiplat TO netaiuser;
\q

# 克隆代码&安装依赖
git clone https://github.com/yourname/network-AI-autoyun-system.git
cd network-AI-autoyun-system
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 初始化表结构
psql -U netaiuser -d netaiplat -f db/schema.sql

# 如遇表权限错误，执行下列SQL(以postgres身份)
sudo -u postgres psql -d netaiplat
DO $$ DECLARE r RECORD; BEGIN FOR r IN SELECT tablename FROM pg_tables WHERE schemaname = 'public' LOOP EXECUTE 'ALTER TABLE public.' || quote_ident(r.tablename) || ' OWNER TO netaiuser;'; END LOOP; END $$;
DO $$ DECLARE r RECORD; BEGIN FOR r IN SELECT sequence_name FROM information_schema.sequences WHERE sequence_schema = 'public' LOOP EXECUTE 'ALTER SEQUENCE public.' || quote_ident(r.sequence_name) || ' OWNER TO netaiuser;'; END LOOP; END $$;
\q

# 配置.env
echo "DATABASE_URL=postgresql+psycopg2://netaiuser:yourpassword@localhost:5432/netaiplat" > .env

# 启动服务
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 访问API文档: http://localhost:8000/docs
```

## 依赖
见 requirements.txt

## 常见问题
- 权限不足：请确保表/序列的owner都是netaiuser
- Pydantic警告：将orm_mode=True改为from_attributes=True
- 密码加密使用passlib[bcrypt]，jwt用python-jose
- 定时任务启动无需额外操作

## 技术交流群

如需源码、定制开发、技术支持可联系作者：847297@qq.com

