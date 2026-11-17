"""
Project: HTTP Forensic Log Sanitizer & Analyzer (Meta Python - Module 3)
Author: Huzaifa Mohammed (HuzaifaMohammed00)

What does this project do?
This project analyzes raw HTTP server logs using Procedural and Functional Programming:
1. Parses raw log strings and divides them into structured fields (ip, method, endpoint, status).
2. Stores each request cleanly in a dictionary using map().
3. Detects suspicious SQLi, XSS, and Path Traversal payloads using filter().
4. Generates security alerts and IP activity summaries using Set and List Comprehensions.
5. Calculates URL endpoint depth using Recursion and sanitizes payloads using Pure Functions.
"""

RAW_HTTP_LOGS = [
    " 192.168.1.10 | GET | /home/index.html | 200 ",
    "10.0.0.55 | POST | /login?user=admin' OR 1=1-- | 403",
    " 172.16.0.9 | GET | /search?q=<script>alert(1)</script> | 400 ",
    "192.168.1.10 | GET | /api/v1/users/profile/settings | 200",
    "10.0.0.55 | GET | /download?file=../../etc/passwd | 403",
    "192.168.1.25 | POST | /checkout/pay | 500",
]


def add_log_entry_pure(log_list, new_entry):
    """Pure function: returns a new list with the added entry without mutating the original list."""
    new_log_list = log_list.copy()
    new_log_list.append(new_entry)
    return new_log_list


def parse_log_single(log_str):
    """Pure transformation function: parses a raw HTTP log line into a structured dictionary."""
    Http = {}
    line = [part.strip() for part in log_str.strip().split("|")]

    Http["ip"] = line[0]
    Http["method"] = line[1].upper()
    Http["endpoint"] = line[2]
    Http["status"] = int(line[-1])
    return Http


parsed_logs = list(map(parse_log_single, RAW_HTTP_LOGS))


def is_suspicious_request(dict_log):
    """Predicate function for filter(): checks if an endpoint contains known web attack patterns."""
    attack_way = ["or 1=1--", "../../etc", "admin", "<script>", "union", "../"]
    endpoint = dict_log["endpoint"].lower()
    result = any(item in endpoint for item in attack_way)
    return result


suspicious_logs = list(filter(is_suspicious_request, parsed_logs))


def display_suspicious():
    """Displays all filtered suspicious HTTP requests."""
    print(f"\n[!] Suspicious Requests detected {len(suspicious_logs)} times:")
    for susreq in suspicious_logs:
        ip = susreq["ip"]
        meth = susreq["method"]
        endpoint = susreq["endpoint"]
        print(f"  - [{meth}] {ip} -> {endpoint}")


def generate_security_reports():
    """Generates unique attacker IPs, failed status alerts (>= 400), and IP request counts."""
    ip_active_count = {}
    attacker_ips = {susreq["ip"] for susreq in suspicious_logs}

    for ip in parsed_logs:
        ip_active_count[ip["ip"]] = ip_active_count.get(ip["ip"], 0) + 1

    print("\n[+] Unique Attacker IPs:", attacker_ips)
    failed_alerts = [
        f"[ALERT {item['status']}] {item['ip']} -> {item['endpoint']}"
        for item in parsed_logs
        if item["status"] >= 400
    ]
    print("\n[+] Failed Alerts (>= 400):")
    for failed in failed_alerts:
        print(" ", failed)
    print("\n[+] IP Activity Summary:", ip_active_count)


def extract_path_segments(endpoint_path):
    """Helper function: strips query strings and splits URL path into segments."""
    clean_path = endpoint_path.split("?")[0]
    stripped_path = clean_path.strip("/")
    if not stripped_path:
        return []
    return stripped_path.split("/")


def count_segments_recursive(segment_list):
    """Recursive function: counts URL path segments without len() or loops."""
    if segment_list == []:
        return 0
    return count_segments_recursive(segment_list[1:]) + 1


def display_endpoint_depths():
    """Displays the recursive path depth for each parsed HTTP log."""
    print("\n[+] URL Endpoint Depth Analysis (via Recursion):")
    for log in parsed_logs:
        segments = extract_path_segments(log["endpoint"])
        depth = count_segments_recursive(segments)
        print(f"  - Endpoint Depth for {log['endpoint']} : {depth}")


def sanitize_log(log_dict):
    """Pure function: returns a sanitized copy of a log dictionary with dangerous symbols redacted."""
    sanitized_dict = log_dict.copy()
    bad_symbols = ["'", "<", "..", ">"]
    clean_endpoint = sanitized_dict["endpoint"]

    for symbol in bad_symbols:
        clean_endpoint = clean_endpoint.replace(symbol, "[REDACTED]")
        sanitized_dict["endpoint"] = clean_endpoint
    return sanitized_dict


def display_sanitized_logs():
    """Sanitizes suspicious logs using map() and displays the cleaned endpoints."""
    print("\n[+] Sanitized Malicious Endpoints (Pure Function + map):")
    sanitized_list = list(map(sanitize_log, suspicious_logs))
    for item in sanitized_list:
        print(f"  - {item['ip']} -> {item['endpoint']}")
    print(
        f"  [Check] Original suspicious_logs untouched? "
        f"{'<script>' in suspicious_logs[1]['endpoint']}"
    )


def run_all_checks():
    """Runs the complete forensic log analysis pipeline."""
    display_suspicious()
    print("-" * 50)
    generate_security_reports()
    print("-" * 50)
    display_endpoint_depths()
    print("-" * 50)
    display_sanitized_logs()


def main():
    """Interactive CLI menu for the HTTP Forensic Log Sanitizer."""
    global RAW_HTTP_LOGS, parsed_logs, suspicious_logs

    while True:
        print("\n" + "=" * 55)
        print("   HTTP Forensic Log Sanitizer (Meta Python Module 3)")
        print("=" * 55)
        print("1. Show Suspicious Requests (filter)")
        print("2. Generate Security Reports (Set & List Comprehensions)")
        print("3. Analyze URL Endpoint Depth (Recursion)")
        print("4. Sanitize Malicious Payloads (Pure Function & map)")
        print("5. Add New Log Entry Safely (Immutability Test)")
        print("6. Run Full Forensic Analysis Pipeline (All Checks)")
        print("0. Exit")
        print("=" * 55)

        choice = input("Select an option (0-6): ").strip()

        if choice == "1":
            display_suspicious()
        elif choice == "2":
            generate_security_reports()
        elif choice == "3":
            display_endpoint_depths()
        elif choice == "4":
            display_sanitized_logs()
        elif choice == "5":
            new_log = input(
                "Enter raw log (e.g. 10.0.0.99 | GET | /admin/config | 401): "
            ).strip()
            if new_log and len(new_log.split("|")) == 4:
                updated_logs = add_log_entry_pure(RAW_HTTP_LOGS, new_log)
                print(
                    f"[+] Original RAW_HTTP_LOGS count: {len(RAW_HTTP_LOGS)} (Untouched!)"
                )
                print(f"[+] New updated_logs count:       {len(updated_logs)}")
            else:
                print("[!] Invalid format. Use: IP | METHOD | ENDPOINT | STATUS")
        elif choice == "6":
            run_all_checks()
        elif choice == "0":
            print("Exiting HTTP Forensic Log Sanitizer. Stay secure!")
            break
        else:
            print("[!] Invalid choice. Please enter a number from 0 to 6.")


if __name__ == "__main__":
    main()
