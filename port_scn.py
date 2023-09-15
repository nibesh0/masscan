import subprocess

class PortChecker:
    def __init__(self, ip_addresses):
        self.ip_addresses = ip_addresses

    def check_port_with_nmap(self, ip, port):
        try:
            command = ["nmap", "-p", str(port), ip]
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)

            if f"{port}/tcp open" in output:
                return True
            else:
                return False
        except subprocess.CalledProcessError:
            return False

    def check_ports(self, port):
        results = {}
        for ip in self.ip_addresses:
            is_open = self.check_port_with_nmap(ip, port)
            results[ip] = is_open
        return results

def save_results_to_file(results, filename, port):
    with open(filename, "w") as f:
        for ip, is_open in results.items():
            f.write(f"Port {port} is {'open' if is_open else 'closed'} on {ip}\n")

def main():
    ip_addresses = ["192.168.1.1", "192.168.1.2", "10.0.0.1"]  
    port = 80
    output_filename = "port_scan_results.txt"

    port_checker = PortChecker(ip_addresses)
    results = port_checker.check_ports(port)
    save_results_to_file(results, output_filename, port)

if __name__ == "__main__":
    main()
