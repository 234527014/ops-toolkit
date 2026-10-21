import argparse


def main():
    parser = argparse.ArgumentParser(description="批量检测主机演示")
    parser.add_argument("--file", default="hosts.txt", help="主机列表文件")
    parser.add_argument("--count", type=int, default=2, help="每台主机ping的次数")
    parser.add_argument("--verbose", action="store_true", help="显示详细信息")
    args = parser.parse_args()


    print("文件:", args.file)
    print("次数:", args.count)
    if args.verbose:
        print("详细模式已开启")


if __name__ == "__main__":
    main()