# ops-toolkit

运维小工具集，第 0 阶段练习仓库。用 Shell 实现几个日常运维场景的小脚本，参数可配置，带基本的错误处理。

## 脚本一览

| 脚本 | 作用 |
|---|---|
| `shell/disk_check.sh` | 检查根分区使用率，超过阈值输出告警 |
| `shell/log_clean.sh` | 压缩超过 7 天的 `.log`，删除超过 30 天的 `.gz` |
| `shell/ping_check.sh` | 读取主机列表，批量检测是否在线并统计离线数量 |

## 用法

```bash
# 磁盘巡检（阈值在脚本开头的 THRESHOLD 变量里修改）
bash shell/disk_check.sh

# 日志清理（默认处理 testlogs/，也可以指定目录）
bash shell/log_clean.sh
bash shell/log_clean.sh /var/log/myapp

# 批量 ping（默认读取 hosts.txt，每行一个 IP 或域名，也可以指定文件）
bash shell/ping_check.sh
bash shell/ping_check.sh my_hosts.txt
```

## 运行环境

- Ubuntu 24.04（WSL2）
- Bash

## 后续计划

- 用 cron 定时运行巡检脚本
- 用 Python 重写并扩展，加入告警通知
- 磁盘告警后自动触发日志清理# ops-toolkit运维小工具集，第 0 阶段练习仓库
