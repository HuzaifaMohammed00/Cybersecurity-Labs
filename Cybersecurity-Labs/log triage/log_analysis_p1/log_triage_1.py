import datetime
import re
import string

counter_ip_failed = {}
counter_ip_seccuss = {}
file = open(
    r"C:\Cybersecurity-Labs\Cybersecurity-Labs\log triage\log_analysis_p1\auth.log"
).read()

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


def most_faild_ip():
    most_failed_ip = None
    most_failed_num = None
    for key, val in counter_ip_failed.items():
        if most_failed_num is None or val > most_failed_num:
            most_failed_num = val
            most_failed_ip = key
    most_failed_ip = str(most_failed_ip)
    return most_failed_ip

    # get the username that connect to the most ip repeated or has falid log in


def get_name_of_most_falid_ip():
    ip = most_faild_ip()
    if ip in file:
        name = re.findall(r"user ([\S]+) from 185.220.101.5", file)
    return name


blocks_ip = {}


def filter_ip():
    for key, value in counter_ip_failed.items():
        if value >= 3:
            blocks_ip[key] = blocks_ip.get(key, "Block")
    return blocks_ip


def f():
    for key, value in filter_ip().items():
        if key in "Accepted password":
            print(key, value + "yes")


print(f())
