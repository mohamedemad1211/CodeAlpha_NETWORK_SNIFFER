import optparse
import scapy.all as scapy
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-r", "--range", dest="network_ip", help="To enter device IP or Network Range")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Enable verbose output")
    options, arguments = parser.parse_args()

    if not options.network_ip:
        parser.error("[-] Please specify an IP Address or Network Range, use -h for help")

    if not validate_ip_range(options.network_ip):
        parser.error("[-] Please specify a valid IP Address or Network Range")

    return options

def validate_ip_range(ip_range):
    # Simple regex for validating IP range (e.g., 192.168.1.1 or 192.168.1.1/24)
    ip_range_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}(/\d{1,2})?$')
    if ip_range_pattern.match(ip_range):
        return True
    return False

def scan(network_ip, verbose=False):
    arp_request = scapy.ARP(pdst=network_ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = arp_broadcast/arp_request

    try:
        answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=verbose)[0]
    except Exception as e:
        print(f"[-] Error occurred during network scan: {e}")
        return []

    client_list = []
    for ans in answered:
        client_dict = {"ip": ans[1].psrc, "mac": ans[1].hwsrc}
        client_list.append(client_dict)

    return client_list

def display_clients(clients):
    print("IP Address\t\tMAC Address")
    print("------------------------------------------")
    for client in clients:
        print(client["ip"], "\t\t", client["mac"])

options = get_arguments()
client_list = scan(options.network_ip, options.verbose)
display_clients(client_list)
