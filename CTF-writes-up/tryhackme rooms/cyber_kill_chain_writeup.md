# 🕵️ Cyber Kill Chain — Walkthrough

> **Author:** [Huzaifa Mohammed](https://www.google.com/search?q=https://github.com/HuzaifaMohammed00)  
> **Platform:** [TryHackMe — Cyber Kill Chain](https://tryhackme.com/room/cyberkillchain)  
> **Category:** Threat Intelligence / Cyber Defence Frameworks

## 📌 Scenario

Developed by `Lockheed Martin` in 2011, the **Cyber Kill Chain** divides a cyberattack into seven sequential phases: `Reconnaissance`, `Weaponisation`, `Delivery`, `Exploitation`, `Installation`, `Command & Control (C2)`, and `Actions on Objectives`. This walkthrough covers the complete updated room questions and the interactive static-site classification lab.

## 🔍 Step-by-Step Walkthrough

### Task 1: Introduction

#### 1. How many phases comprise the Cyber Kill Chain?

The `Lockheed Martin` Cyber Kill Chain breaks an attack down into 7 distinct stages from initial target research to final objective execution.

```text
1. Reconnaissance -> 2. Weaponisation -> 3. Delivery -> 4. Exploitation -> 5. Installation -> 6. Command & Control (C2) -> 7. Actions on Objectives
```

**Answer:** `7`

### Task 2: Reconnaissance

#### 2. What is the term for using search engines to reveal sensitive information and confidential files?

Attackers use advanced search engine operators (such as `filetype:pdf`, `site:`, and `intitle:`) to uncover exposed files and directories without touching the target server directly.

```text
site:target.com filetype:pdf "confidential"
```

**Answer:** `Google Dorking`

#### 3. What type of reconnaissance is it where the attacker checks the social media pages?

Gathering target information from public sources like social media, `WHOIS`, and public websites without directly interacting with the target's network is classified as passive reconnaissance (and collecting employee emails during this stage is known as `Email harvesting` using tools like `OSINT Framework`).

```text
No direct network interaction with target -> Passive Reconnaissance
```

**Answer:** `Passive Reconnaissance`

### Task 3: Weaponisation

#### 4. What technique is mentioned to evade detection by making it challenging to analyse the malicious code?

Attackers scramble, encode, or pack their payload code so signature-based antivirus scanners and human analysts cannot easily read its logic.

```text
Hiding/scrambling payload code -> Obfuscation
```

**Answer:** `Obfuscation`

#### 5. What built-in feature makes creating a malicious MS Office document possible?

Attackers embed automated `VBA` scripts inside `Microsoft Word` or `Excel` files that execute a hidden payload as soon as the victim clicks "Enable Content".

```text
MS Office automated script feature -> Macro
```

**Answer:** `Macro`

### Task 4: Delivery

#### 6. What method involves showing advertisements on legitimate websites to redirect users to malicious pages?

Adversaries inject malicious ads into legitimate ad networks so visitors are redirected to exploit kits or malware downloads (or infect a trusted site frequently visited by a target group in a `Watering hole attack`).

```text
Malicious online advertisements -> Malvertising
```

**Answer:** `Malvertising`

#### 7. What phishing attack sends text messages with malicious links or instructions to download malware?

Phishing attacks delivered over mobile `SMS` text messages are referred to as `Smishing`.

```text
SMS + Phishing -> Smishing
```

**Answer:** `Smishing`

### Task 5: Exploitation

#### 8. What type of exploit is used before the vendor becomes aware of a vulnerability?

An exploit targeting an undisclosed software flaw that has zero days of vendor patches or security updates available is a `Zero-day exploit`.

```text
Unpatched / unknown software vulnerability -> Zero-day exploit
```

**Answer:** `Zero-day exploit`

#### 9. What technology is mentioned to prevent an attacker from gaining access even with valid login credentials?

Requiring a second verification factor (such as an authenticator token) stops attackers from logging in with stolen or phished passwords alone.

```text
Second authentication factor -> MFA
```

**Answer:** `MFA`

### Task 6: Installation

#### 10. What tactic allows attackers to execute operating system commands on a target via a web browser interface?

Attackers upload a persistent script (`PHP`, `ASPX`, or `JSP`) to an exploited web server to run operating system commands remotely through a browser (often hiding file modification dates using `Timestomping`).

```text
Browser-accessible backdoor script -> Web shell
```

**Answer:** `Web shell`

#### 11. What technique is mentioned to prevent the execution of unauthorised or malicious software by only allowing approved applications to run?

Application `Allowlisting` blocks any unauthorized binary or script from executing on an endpoint unless it is explicitly on the approved list.

```text
Only permit approved binaries -> Allowlisting
```

**Answer:** `Allowlisting`

### Task 7: Command and Control (C2)

#### 12. What is the name of the tactic where data is hidden within DNS queries?

Malware encodes command-and-control traffic inside continuous `DNS` lookups to a domain controlled by the attacker to bypass firewall restrictions.

```text
C2 communication hidden in DNS requests -> DNS tunnelling
```

**Answer:** `DNS tunnelling`

#### 13. What protocol would the attacker use to smuggle his data as encrypted web traffic?

Attackers use `HTTPS` (port `443`) so their `C2` beaconing traffic is encrypted and blends in with normal web browsing traffic.

```text
Encrypted web traffic on TCP port 443 -> HTTPS
```

**Answer:** `HTTPS`

### Task 8: Actions on Objectives

#### 14. What is the term for stealing sensitive files from a target network?

Once attackers reach their final goal, copying and transferring confidential data out of the victim's environment is called `Data Exfiltration`.

```text
Stealing sensitive data out of the network -> Data Exfiltration
```

**Answer:** `Data Exfiltration`

#### 15. What principle limits who can access sensitive systems and data to minimise damage caused by an attacker?

Granting users and service accounts only the minimum permissions required to perform their duties prevents lateral movement and limits blast radius.

```text
Minimum necessary access rights -> Principle of least privilege
```

**Answer:** `Principle of least privilege`

#### 16. What type of attack involves encrypting files and demanding payment in exchange for the decryption key?

`Ransomware` encrypts the victim's files (and often deletes `Windows` `Shadow Copy` backups) to extort a ransom payment.

```text
File encryption extortion attack -> Ransomware
```

**Answer:** `Ransomware`

### Task 9: Conclusion (Interactive Static Site Lab)

#### 17. What is the flag after you complete the static site?

Drag and drop each attacker action into its matching Cyber Kill Chain stage on the static site:

```text
Reconnaissance         -> Google Dorking
Weaponisation          -> Compile a Malicious Program (or powershell)
Delivery               -> SMS Phishing (or spearphishing attachment)
Exploitation           -> Exploit Public-Facing Application
Installation           -> Deploy a Web Shell (or dynamic linker hijacking)
Command & Control (C2) -> Use DNS for Communication (or fallback channels)
Actions on Objectives  -> Data Exfiltration (or data from local system)
```

**Answer:** Complete the drag-and-drop matching on the static site (classic static lab flag: `THM{7HR347_1N73L_12_4w35om3}`).

## 💡 Key Takeaways

* **Disrupting Any Stage Stops the Intrusion**: Blocking an attacker during `Delivery` (`Smishing`/`Malvertising`), `Exploitation` (`MFA`/patching), or `Installation` (`Allowlisting`) prevents them from reaching `Actions on Objectives`.
* **Passive vs. Active Reconnaissance**: `Google Dorking` and social media profiling gather intelligence silently without triggering network alerts.
* **Defense-in-Depth**: Combining `MFA`, `Allowlisting`, `DNS` monitoring, and the `Principle of least privilege` creates layered protection across all 7 stages ([TryHackMe Cyber Kill Chain](https://tryhackme.com/room/cyberkillchain)).
