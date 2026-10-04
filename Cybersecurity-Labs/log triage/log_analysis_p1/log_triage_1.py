import datetime
import re
import string

# log = "Sep 20 01:47:19 prod-web01 sshd[10003]: Failed password for invalid user administrator from 203.0.113.45 port 47315 ssh2"
counter_ip_failed = {}
counter_ip_seccuss = {}
most_failed_ip = None
most_failed_num = None
# Compromised-IPs = []
with open(
    r"C:\Cybersecurity-Labs\Cybersecurity-Labs\log triage\log_analysis_p1\auth.log"
) as log:
    for line in log:
        lines = line.strip()
        if "Failed password" in lines:
            ip = "".join(re.findall(r"from ([\d.]+)", lines))
            counter_ip_failed[ip] = counter_ip_failed.get(ip, 0) + 1
        if "Accepted password" in lines:
            ip = "".join(re.findall(r"from ([\d.]+)", lines))
            counter_ip_seccuss[ip] = counter_ip_seccuss.get(ip, 0) + 1
    # get the most ip that make faild log in
    for key, val in counter_ip_failed.items():
        if most_failed_num is None or val > most_failed_num:
            most_failed_num = val
            most_failed_ip = key
    most_failed_ip = str(most_failed_ip)
    # get the username that connect to the most ip repeated or has falid log in
    if most_failed_ip:
        name = re.findall(r"user (\S+)", lines)


print((counter_ip_failed))
print((counter_ip_seccuss))
print(most_failed_num, most_failed_ip)
# def greater_failed(ips):
print(name)
