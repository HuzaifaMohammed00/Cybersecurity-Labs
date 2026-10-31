# 🛡️ Cybersecurity Labs & Hands-on Projects

> A personal collection of hands-on cybersecurity practice, incident response investigations, CTF walkthroughs, and custom security scripts — built by **[Huzaifa Mohammed](https://www.google.com/search?q=https://github.com/HuzaifaMohammed00)** while preparing for Software Engineering at SUST and advancing toward a career as a Cybersecurity Engineer / SOC Analyst.

---

## 📌 What's in Here

This repository serves as my practical cybersecurity engineering lab notebook. Rather than keeping abstract notes, every folder documents real, hands-on labs with complete methodology, technical explanations, command references, and defensive remediation strategies:

* 🚩 **Incident Response & Threat Hunting Walkthroughs**: End-to-end investigations analyzing malware traffic, C2 beaconing, and enterprise ransomware attacks using SIEM and forensic tools.
* 🌐 **Web Application Security & OWASP Top 10**: Practical exploitation and defense covering SQL Injection (In-Band, Blind, Time-Based), Authentication Bypasses, and secure backend remediation using Prepared Statements.
* 🔍 **Traffic & Log Analysis**: Deep packet inspection using `Wireshark` and `TShark`, paired with advanced SIEM queries using `Splunk SPL` and `Regex`.
* 🧪 **Security Scripts & Utilities**: Custom Python networking and encryption tools written from scratch (`AES.py`, TCP client-server sockets, log analyzers).

---

## 📂 Repository Structure

```text
cybersecurity-labs/
├── thm-walkthroughs/               # TryHackMe Room Walkthroughs & SOC Labs
│   ├── Conti-Ransomware-Splunk.md  # SOC L2 Capstone: ProxyShell to Conti ransomware investigation
│   ├── Splunk-Exploring-SPL.md     # In-depth SPL filtering, stats, lookup, & anomaly detection
│   ├── SQL-Injection.md            # OWASP Top 10: In-Band, Boolean & Time-Based Blind SQLi
│   ├── Cyber-Kill-Chain.md         # Lockheed Martin 7-stage attack lifecycle & defense controls
│   ├── Regular-Expressions.md      # Regex patterns for SOC log analysis & IOC extraction
│   ├── Carnage-Malware-Traffic.md  # Wireshark C2 beaconing & malspam PCAP analysis
│   └── TShark-CLI-Forensics.md     # Command-line packet analysis & protocol extraction
│
├── ctf-walkthroughs/               # CTF Challenges & Forensic Scenarios
│   ├── sql-murder-mystery.md       # Relational database forensic investigation with SQLite
│   ├── insecure-sessions.md        # Session hijacking & cookie tampering labs
│   └── cyberheroes.md              # Web authentication bypass challenge
│
├── scripts-experiments/            # Custom Python Security Scripts
│   ├── AES-CLI/                    # AES-CBC & Fernet CLI encryption/decryption tool
│   ├── try_TCP_conn/               # Low-level TCP client & server built with Python socket
│   └── log-analyzers/              # Brute-force detection scripts using SQLite & Regex
│
└── README.md                       # Main index & portfolio overview
```

---

## 📑 Featured Labs & Technical Walkthroughs

| Category | Lab / Target | Primary Tools | Key Focus & Techniques | Write-up |
| :--- | :--- | :--- | :--- | :--- |
| **Incident Response** | [Conti Ransomware](https://tryhackme.com/room/contiransomwarehgh) | `Splunk`, `Sysmon`, `IIS` | Investigated Exchange ProxyShell exploit, process injection into `lsass.exe`, and ransom note spread. | [View Walkthrough](https://www.google.com/search?q=thm-walkthroughs/Conti-Ransomware-Splunk.md) |
| **SIEM & Log Analysis** | [Splunk: Exploring SPL](https://tryhackme.com/room/splunkexploringspl) | `Splunk`, `SPL` | Structured search queries (`dedup`, `regex`), data enrichment (`iplocation`, `lookup`), and VPN anomaly hunting. | [View Walkthrough](https://www.google.com/search?q=thm-walkthroughs/Splunk-Exploring-SPL.md) |
| **Web Security** | [SQL Injection](https://tryhackme.com/room/sqlinjectionintroduction) | `Burp Suite`, `SQL` | Exploited `UNION`-based, Boolean Blind, and Time-Based SQLi; implemented defense via Prepared Statements. | [View Walkthrough](https://www.google.com/search?q=thm-walkthroughs/SQL-Injection.md) |
| **Threat Intelligence** | [Cyber Kill Chain](https://tryhackme.com/room/cyberkillchain) | Frameworks | Mapped adversary TTPs across all 7 stages (Google Dorking, Macros, Web Shells, DNS Tunneling). | [View Walkthrough](https://www.google.com/search?q=thm-walkthroughs/Cyber-Kill-Chain.md) |
| **Network Forensics** | [Carnage](https://tryhackme.com/room/c2carnage) | `Wireshark`, `VirusTotal` | Reconstructed multi-stage infection, detected Cobalt Strike C2 beaconing, and analyzed SMTP malspam. | [View Walkthrough](https://www.google.com/search?q=thm-walkthroughs/Carnage-Malware-Traffic.md) |
| **CLI Traffic Analysis** | [TShark](https://tryhackme.com/room/tshark) | `TShark` | Automated packet extraction, DNS query analysis, and credential carving directly from terminal. | [View Walkthrough](https://www.google.com/search?q=thm-walkthroughs/TShark-CLI-Forensics.md) |
| **Pattern Matching** | [Regular Expressions](https://tryhackme.com/room/catregex) | `Regex`, `grep` | Built 29 precision patterns for parsing logs, extracting IPv4 addresses, and identifying password hashes. | [View Walkthrough](https://www.google.com/search?q=thm-walkthroughs/Regular-Expressions.md) |
| **Database Forensics** | [SQL Murder Mystery](https://mystery.knightlab.com/) | `SQLite` | Solved an open-ended murder investigation using complex relational queries (`JOIN`, `LIKE`, subqueries). | [View Walkthrough](https://www.google.com/search?q=ctf-walkthroughs/sql-murder-mystery.md) |

---

## 🛠️ Tools & Lab Environment

* **Operating Systems**: Kali Linux (VMware Workstation), Ubuntu Server, Windows 10/11.
* **Security & Triage Tools**: Splunk Cloud / Enterprise, Burp Suite Community, Wireshark, TShark, Nmap, Feroxbuster, Docker.
* **Languages & Scripting**: Python 3 (Requests, Socket, Cryptography, SQLite3), Bash, SQL (MySQL / SQLite), Regular Expressions (PCRE).
* **Defensive Practices**: Prepared Statements (Parameterized Queries), Sysmon Event Correlation (Events 1, 8, 11), Log Normalization, Principle of Least Privilege.

---

## 🔗 Related Repositories & Larger Projects

Larger standalone projects are maintained in their own dedicated repositories:

* 🛡️ **[VulnShop](https://www.google.com/search?q=https://github.com/HuzaifaMohammed00/VulnShop)**: Intentionally vulnerable e-commerce web application built with Flask, SQLite, and Docker targeting OWASP Top 10 vulnerabilities (SQLi, Broken Access Control).
* 🔒 **[Password-Generator-v2](https://www.google.com/search?q=https://github.com/HuzaifaMohammed00)**: Secure password generation and hashing utility with customizable entropy rules.
* 📰 **[PulseNews](https://www.google.com/search?q=https://github.com/HuzaifaMohammed00)**: CLI news aggregator leveraging REST APIs and environment configuration.

---

## 👤 About

Maintained by **Huzaifa Mohammed** — Software Engineering student at Sudan University of Science and Technology (SUST), actively studying defensive security, penetration testing, and software development. My long-term mission is to protect organizations through technology and contribute to national cybersecurity capacity in Sudan.