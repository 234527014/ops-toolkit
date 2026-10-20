#python
# 读取 hosts.txt：文件读取、列表、字典

from pathlib import Path

hosts_file = Path.home() /"projects"/"ops-toolkit"/"hosts.txt"

hosts= []
for line in hosts_file.read_text().splitlines():
    line = line.strip()
    if line == "":
        continue
    hosts.append(line)

print(f"共读取 {len(hosts)}台主机")

# 字典：给每台主机记一个状态
status = {}
for host in hosts:
    if host.startswith("127."):
        status[host] = "本机"
    else:
        status[host] = "远程"

for host,kind in status.items():
    print(f"{host} -> {kind}")