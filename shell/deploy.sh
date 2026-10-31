#!/usr/bin/env bash
# 用法: deploy.sh <镜像标签>
set -euo pipefail

IMAGE=ghcr.io/234527014/ops-toolkit
STATE=${STATE_FILE:-$HOME/.ops-toolkit-current}
TAG=${1:?用法: deploy.sh <镜像标签>}
PREV=$(cat "$STATE" 2>/dev/null || true)

echo "目标版本: $TAG  当前版本: ${PREV:-无}"

docker pull "$IMAGE:$TAG"

if docker run --rm "$IMAGE:$TAG" --help >/dev/null; then
  [ -z "$PREV" ] || echo "$PREV" > "$STATE.prev"
  echo "$TAG" > "$STATE"
  echo "部署成功，当前版本: $TAG"
else
  echo "健康检查失败，保持当前版本: ${PREV:-无}" >&2
  exit 1
fi
