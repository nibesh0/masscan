

def ips(startip,endip):
    ip = []
    start=(255)
    ending=255
    for i in range(255):
        for j in range(255):
            ip.append(startip[0:6]+f"{i}.{j}")
    return ip

start_ip = "10.10.0.0"
end_ip = "10.10.1.0"
ip_list = ips(start_ip, end_ip)

for ip in ip_list:
    print(ip)