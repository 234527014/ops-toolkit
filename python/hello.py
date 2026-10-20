#python
# 第一个 Python 脚本：变量、条件、循环、函数
hosts = ["web-01","web-02","db-01","web-03"]


def greet(name):
    return f"检查主机: {name}"


for host in hosts:
    if host.startswith("web"):
        print(greet(host),"(web服务器)")
    else:
        print(greet(host),"(其他)")
        
print(f"共 {len(hosts)}台")