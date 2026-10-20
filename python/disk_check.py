# 磁盘巡检（Python 版）：超过阈值就告警

import shutil
import sys

THRESHOLD = 80


def get_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    return used * 100 // total


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "/"
    usage = get_usage(path)

    if usage >= THRESHOLD:
        print(f"[告警] {path} 使用率 {usage}%,超过阈值 {THRESHOLD}%")
        return 1

    print(f"[正常] {path} 使用率 {usage}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())