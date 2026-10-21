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