#!/bin/bash
# 日志清理：压缩超过 7 天的 .log，删除超过 30 天的 .gz

LOG_DIR="${1:-$HOME/projects/ops-toolkit/testlogs}"
COMPRESS_DAYS=7
DELETE_DAYS=30

if [ ! -d "$LOG_DIR" ]; then
    echo "[错误] 目录不存在: $LOG_DIR"
    exit 1
fi

find "$LOG_DIR" -name "*.log" -mtime +$COMPRESS_DAYS -exec gzip {} \;
find "$LOG_DIR" -name "*.gz" -mtime +$DELETE_DAYS -delete
echo "[完成] 日志处理结束"