#!/bin/bash
# 批量 ping 检测：读取主机列表，报告每台是否在线
HOSTS_FILE="${1:-$HOME/projects/ops-toolkit/hosts.txt}"

check_host() {
    local host="$1"
    if ping -c 2 -W 3 "$host" > /dev/null 2>&1; then
        echo "[在线] $host"
        return 0
    else
        echo "[离线] $host"
        return 1
    fi
}

if [ ! -f "$HOSTS_FILE" ]; then
    echo "[错误] 主机列表不存在: $HOSTS_FILE"
    exit 1
fi

total=0
down=0

while read -r host; do
    [ -z "$host" ] && continue
    total=$((total + 1))
    check_host "$host" || down=$((down + 1))
done < "$HOSTS_FILE"

echo "共检测 $total 台，离线 $down 台"