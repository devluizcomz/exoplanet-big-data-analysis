# 🐳 Docker Configuration

## Services Overview

| Service | Port | Purpose | Web UI |
|---------|------|---------|--------|
| **NameNode** | 9870, 9000 | HDFS Master | http://localhost:9870 |
| **DataNode** | - | HDFS Storage | - |
| **Spark Master** | 8080, 7077 | Spark Cluster Manager | http://localhost:8080 |
| **Spark Worker** | - | Spark Executor | - |
| **Hive Server** | 10000, 10002 | SQL Interface | http://localhost:10002 |
| **Hive Metastore** | 9083 | Metadata Service | - |
| **PostgreSQL** | 5432 | Metastore DB | - |

---

## 🚀 Quick Start

### Start All Services

```bash
cd docker
docker-compose up -d
