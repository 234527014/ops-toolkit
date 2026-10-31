#!/usr/bin/env bash
# 用法: rollback.sh  （回到上一个部署的版本）
set -euo pipefail

STATE=${STATE_FILE:-$HOME/.ops-toolkit-current}
PREV_FILE="$STATE.prev"

if [ ! -f "$PREV_FILE" ]; then
  echo "没有可回滚的版本" >&2
  exit 1
fi

TARGET=$(cat "$PREV_FILE")
echo "回滚到: $TARGET"
"$(dirname "$0")/deploy.sh" "$TARGET"
