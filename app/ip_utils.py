# app/ip_utils.py
import re
import ipaddress

def extract_ips(line):
    """Extract and normalize IPv4 addresses"""
    ipv4_pattern = r'(?:::ffff:)?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    matches = re.findall(ipv4_pattern, line)
    normalized_ips = []
    for ip in matches:
        try:
            # Normalize IP to canonical form (e.g., 192.168.1.1)
            normalized_ip = str(ipaddress.IPv4Address(ip))
            normalized_ips.append(normalized_ip)
        except ipaddress.AddressValueError:
            pass  # Skip invalid IPs
    return normalized_ips

def is_private_ip(ip):
    """Check if IP is private"""
    try:
        return ipaddress.IPv4Address(ip).is_private
    except:
        return False