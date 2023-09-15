import ipaddress
import threading
import socket

def is_alive(ip):
    try:
        socket.setdefaulttimeout(1)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((str(ip), 80))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def scan_ip(ip, output_file):
    if is_alive(ip):
        with open(output_file, "a") as f:
            f.write(str(ip) + "\n")

def main(subnet, num_threads, output_file):
    ip_network = ipaddress.IPv4Network(subnet)
    threads = []

    for ip in ip_network.hosts():
        thread = threading.Thread(target=scan_ip, args=(ip, output_file))
        threads.append(thread)
        thread.start()

        # Limit the number of threads to 'num_threads'
        if len(threads) >= num_threads:
            for thread in threads:
                thread.join()
            threads = []

    # Wait for remaining threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    subnet = "10.10.39.0/24"
    num_threads = 10
    output_file = "alive_ips.txt"
    main(subnet, num_threads, output_file)
