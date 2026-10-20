import subprocess


def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

code, out, err = run(["echo", "hello"])
print("退出码:", code)
print("输出:", out)

code, out, err = run(["ping", "-c", "2", "-W", "3", "127.0.0.1"])
print("退出码:", code)
print("输出最后一行:", out.splitlines()[-1])

code, out, err = run(["ping", "-c", "2", "-W", "3", "192.0.2.1"])
print("不通地址码:", code)

code, out, err = run(["ls", "/不存在的目录"])
print("出错退出码:", code)
print("ls 的错误信息:", err)
