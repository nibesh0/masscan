import ipaddress
import threading
import subprocess

def is_alive(ip):
    try:
        result = subprocess.run(["ping", "-c", "1", str(ip)], capture_output=True, text=True, timeout=5)
        return "1 packets transmitted, 1 received" in result.stdout
    except subprocess.TimeoutExpired:
        return False

def scan_ip(ip, output_file):
    if is_alive(ip):
        with open(output_file, "a") as f:
            f.write(str(ip) + "\n")
def ips(startip,endip):
    ip = []
    start=(255)
    ending=255
    for i in range(255):
        for j in range(255):
            ip.append(startip[0:6]+f"{i}.{j}")
    return ip
def main(start_ip, end_ip, num_threads, output_file):
    ip_range = ips(start_ip,end_ip)
    threads = []

    for ip in ip_range:
        thread = threading.Thread(target=scan_ip, args=(ip, output_file))
        threads.append(thread)
        thread.start()

        if len(threads) >= num_threads:
            for thread in threads:
                thread.join()
            threads = []


    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_ip = "10.10.0.0"
    end_ip = "10.10.255.255"
    num_threads = 100000
    output_file = "alive_ips.txt"
    main(start_ip, end_ip, num_threads, output_file)
