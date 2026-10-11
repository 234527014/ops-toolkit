#!/bin/bash
#磁盘使用率巡检，超过阈值警告
THRESHOLD=80
usage=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')
if [ "$usage" -ge "$THRESHOLD" ]; then
echo "[告警]根分区使用率 ${usage}%,超过阈值 ${THRESHOLD}%"
else 
echo "[正常]根分区使用率 ${usage}%"
fi