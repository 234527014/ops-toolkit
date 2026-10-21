import argparse
import logging
import subprocess
import sys
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="批量检测主机连通性")
    parser.add_argument("--file", default="hosts.txt", help="主机列表文件")
    parser.add_argument("--count", type=int, default=2, help="每台主机 ping 的次数")
    parser.add_argument("--timeout", type=int, default=3, help="每次等待秒数")
    parser.add_argument("--log", default="ping_check.log", help="日志文件")
    return parser.parse_args()


def setup_logging(log_file):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def read_hosts(path):
    lines = Path(path).read_text().splitlines()
    return [line.strip() for line in lines if line.strip()]


def check_host(host, count, timeout):
    result = subprocess.run(
        ["ping", "-c", str(count), "-W", str(timeout), host],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def main():
    args = parse_args()
    setup_logging(args.log)

    if not Path(args.file).exists():
        logging.error("主机列表文件不存在: %s", args.file)
        return 2

    hosts = read_hosts(args.file)
    logging.info("开始检测，共 %d 台主机", len(hosts))

    down = []
    for host in hosts:
        if check_host(host, args.count, args.timeout):
            logging.info("%s 正常", host)
        else:
            logging.error("%s 不通", host)
            down.append(host)

    logging.info("检测完成: 共 %d 台，异常 %d 台", len(hosts), len(down))
    if down:
        logging.warning("异常主机: %s", ", ".join(down))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())