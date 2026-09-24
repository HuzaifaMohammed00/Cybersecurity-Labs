import datetime
import re
import string

# log = "Sep 20 01:47:19 prod-web01 sshd[10003]: Failed password for invalid user administrator from 203.0.113.45 port 47315 ssh2"
counter_ip_failed = {}
counter_ip_seccuss = {}
# Compromised-IPs = []
with open(r"C:\Cybersecurity-Labs\Cybersecurity-Labs\log triage\auth.log") as log:
    for line in log:
        lines = line.strip()
        if "Failed password" in lines:
            ip = "".join(re.findall(r"from ([\d.]+)", lines))
            counter_ip_failed[ip] = counter_ip_failed.get(ip, 0) + 1
        if "Accepted password" in lines:
            ip = "".join(re.findall(r"from ([\d.]+)", lines))
            counter_ip_seccuss[ip] = counter_ip_seccuss.get(ip, 0) + 1
        
print(sum(counter_ip_failed.values()))
print(sum(counter_ip_seccuss.values()))
print(max(counter_ip_failed.values()))
print(max(counter_ip_seccuss.values()))
print((counter_ip_failed))
print((counter_ip_seccuss))
# def greater_failed(ips):
