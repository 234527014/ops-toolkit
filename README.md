# ops-toolkit

运维小工具集，第 0 阶段练习仓库。

## 脚本列表

### Shell

| 脚本 | 作用 |
|---|---|
| `shell/disk_check.sh` | 检查根分区使用率，超过阈值输出告警 |
| `shell/log_clean.sh` | 压缩超过 7 天的 `.log`，删除超过 30 天的 `.gz` |
| `shell/ping_check.sh` | 读取主机列表，批量检测是否在线并统计离线数量 |

### Python

| 脚本 | 作用 |
|---|---|
| `python/ping_check.py` | 批量检测主机连通性，支持命令行参数和日志，用退出码表示结果 |
| `python/disk_check.py` | 检查磁盘使用率，超过阈值返回退出码 1 |
| `python/read_hosts.py` | 读取主机列表并分类显示 |
| `python/run_cmd.py` | subprocess 演示：运行命令并获取退出码和输出 |
| `python/args_demo.py` | argparse 演示：命令行参数 |
| `python/log_demo.py` | logging 演示：日志级别和输出到文件 |
| `python/hello.py` | Python 语法练习 |

## 用法

```bash
# 磁盘巡检（阈值在脚本开头的 THRESHOLD 变量里修改）
bash shell/disk_check.sh

# 日志清理（默认处理 testlogs/，也可以指定目录）
bash shell/log_clean.sh
bash shell/log_clean.sh /var/log/myapp

# 批量 ping（Shell 版，默认读取 hosts.txt，每行一个 IP 或域名）
bash shell/ping_check.sh
bash shell/ping_check.sh my_hosts.txt

# 批量 ping（Python 版，在仓库根目录运行）
python python/ping_check.py
python python/ping_check.py --file my_hosts.txt --count 3 --timeout 2 --log check.log
python python/ping_check.py --help
```

`python/ping_check.py` 的退出码：0 全部正常，1 有主机不通，2 主机列表文件不存在。

## 运行环境

- Ubuntu 24.04（WSL2）
- Bash
- Python 3.12（虚拟环境 `~/venvs/base`）

## 后续计划

- 用 cron 定时运行巡检脚本
- 磁盘告警后自动触发日志清理
- 加入告警通知

## Docker 用法

构建镜像：

```bash
docker build -t ops-toolkit:v1 .
```

运行（挂载主机列表）：

```bash
docker run --rm -v "$(pwd)/hosts.txt:/app/hosts.txt" ops-toolkit:v1
```

自定义参数并把日志写回本机：

```bash
mkdir -p logs
docker run --rm -v "$(pwd)/hosts.txt:/app/hosts.txt" -v "$(pwd)/logs:/app/logs" ops-toolkit:v1 --file hosts.txt --count 1 --timeout 2 --log logs/check.log
```

说明：镜像基于 python:3.12-slim，并安装 iputils-ping；hosts.txt 和日志不打进镜像，运行时通过 `-v` 挂载。
## Docker Compose 用法

在仓库根目录运行（hosts.txt 和 logs 目录由 compose.yaml 自动挂载）：

```bash
docker compose build
docker compose run --rm ops-toolkit
```

退出码和直接运行脚本一致：0 全部正常，1 有主机不通。

`compose-lab/` 是练习目录，演示命名卷：

```bash
cd compose-lab
docker compose run --rm app     # 每次运行日志都会累积在卷里
docker compose down             # 删容器和网络，保留卷
docker compose down -v          # 连卷一起删，数据丢失
## Docker 进阶

镜像瘦身：把基础镜像从 python:3.12-slim 换成 python:3.12-alpine，镜像从 181MB 降到 74MB，脚本输出与退出码保持一致。

```bash
docker build -f Dockerfile.alpine -t ops-toolkit:alpine .
```

多阶段构建：编译工具只留在第一阶段，最终镜像只拷贝成品（示例见 multistage-lab，单阶段 398MB，多阶段 12.9MB）。

健康检查：Dockerfile 中用 HEALTHCHECK 定期探测服务是否真的可用，docker ps 的 STATUS 会显示 healthy 或 unhealthy（示例见 health-lab）。
## 版本说明（分支演示）
## Git 分支与冲突

- 新建并切换分支：git switch -c 分支名
- 合并分支：先 git switch main，再 git merge 分支名
- 无分叉时是 Fast-forward；两个分支改了同一行会产生冲突，在 VS Code 里点选保留哪一边，再 git add、git commit 完成合并
- 放弃一次合并：git merge --abort