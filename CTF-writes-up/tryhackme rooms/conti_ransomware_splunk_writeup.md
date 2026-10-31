# 🕵️ Conti Ransomware (Splunk) — Walkthrough

> **Author:** [Huzaifa Mohammed](https://www.google.com/search?q=https://github.com/HuzaifaMohammed00)  
> **Platform:** [TryHackMe — Conti](https://tryhackme.com/room/contiransomwarehgh)  
> **Category:** SOC Level 2 / Incident Response & Threat Hunting (`Splunk` + `Sysmon` + `IIS`)

## 📌 Scenario

An organization's `Microsoft Exchange` server (`WIN-AOQKG2AS2Q7.bellybear.local`) was compromised via the `ProxyShell` exploit chain and hit with **Conti Ransomware**. Employees cannot access `Outlook`, the administrator is locked out of the `Exchange Admin Center`, and `readme.txt` ransom notes have appeared across the server. Using `Splunk` over **All time**, we investigate `Sysmon` (`EventCode` 1, 8, 11) and `IIS` logs to reconstruct the entire attack.

## 🔍 Step-by-Step Walkthrough

### 0. Initial Triage — Discovering Indexes, Sourcetypes, and Field Names

Before running specific queries, set the time picker to **All time** and inspect the available `sourcetypes` in `index=main`. Note that this `Splunk` instance parses Windows Event IDs under the field name `EventCode` (rather than `EventID`).

```spl
index=* | stats count by index sourcetype
```

### 1. Can you identify the location of the ransomware?

Filter `Sysmon` file creation events (`EventCode=11`) or process creation events (`EventCode=1`) for suspicious `.exe` binaries executing outside standard system paths. A fake `cmd.exe` binary is located inside the Administrator's `Documents` folder.

```spl
index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1 "*cmd.exe"
| table _time Image ParentImage CommandLine
```

**Answer:** `C:\Users\Administrator\Documents\cmd.exe`

### 2. What is the Sysmon event ID for the related file creation event?

In `Sysmon`, whenever a file is created or overwritten on disk, it logs Event ID `11` (`FileCreate`).

```text
Sysmon FileCreate Event -> 11
```

**Answer:** `11`

### 3. Can you find the MD5 hash of the ransomware?

Look at the `Sysmon` process creation event (`EventCode=1`) for `C:\Users\Administrator\Documents\cmd.exe` and inspect the `Hashes` field (`EventCode=1` logs file hashes, whereas `EventCode=11` does not).

```spl
index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1 Image="C:\\Users\\Administrator\\Documents\\cmd.exe"
| table _time Image Hashes
```

**Answer:** `290C7DFB01E50CEA9E19DA81A781AF2C`

### 4. What file was saved to multiple folder locations?

Query `Sysmon` file creation events (`EventCode=11`) where the initiating process `Image` is the ransomware binary `C:\Users\Administrator\Documents\cmd.exe` to see the ransom note dropped across 18 user profile directories.

```spl
index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=11 Image="C:\\Users\\Administrator\\Documents\\cmd.exe"
| stats count by TargetFilename
```

**Answer:** `readme.txt`

### 5. What WAS the command the attacker used to add a new user to the compromised system?

Search `Sysmon` process creation events (`EventCode=1`) for `net user` commands (`CommandLine="*net*user*"`). Format the command with single spaces to match the answer mask.

```spl
index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1 CommandLine="*net*user*"
| table _time CommandLine
```

**Answer:** `net user /add securityninja hardToHack123$`

### 6. The attacker migrated the process for better persistence. What is the migrated process image (executable), and what is the original process image (executable) when the attacker got on the system?

Filter for `Sysmon` `CreateRemoteThread` events (`EventCode=8`), which detect process injection and migration. Only two events exist: `powershell.exe` migrating into `unsecapp.exe` (a legitimate `WMI` process), followed by `unsecapp.exe` injecting into `lsass.exe`.

```spl
index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=8
| table _time SourceImage TargetImage
```

**Answer:** `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe,C:\Windows\System32\wbem\unsecapp.exe`

### 7. The attacker also retrieved the system hashes. What is the process image used for getting the system hashes?

From the second row of the `EventCode=8` (`CreateRemoteThread`) query above, `unsecapp.exe` injects into the Local Security Authority Subsystem Service (`lsass.exe`) to dump credentials from memory.

```spl
index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=8
| table _time SourceImage TargetImage
```

**Answer:** `C:\Windows\System32\lsass.exe`

### 8. What is the web shell the exploit deployed to the system?

Search `IIS` logs (`sourcetype=iis`) or search across `index=main` for `.aspx` files (`*.aspx*`). An `attrib.exe` command reveals the malicious `.aspx` web shell staged inside the `Exchange` `owa\auth\` folder.

```spl
index=main "*.aspx*" NOT sourcetype=iis
| stats count by CommandLine EventCode
```

**Answer:** `i3gfPctK1c2x.aspx`

### 9. What is the command line that executed this web shell?

Copy the exact raw `CommandLine` value returned by the query in Question 8 (including the double space after `attrib.exe` and the `UNC` path to `C$`).

```spl
index=main EventCode=1 "*i3gfPctK1c2x.aspx*"
| table CommandLine
```

**Answer:** `attrib.exe -r \\\\win-aoqkg2as2q7.bellybear.local\C$\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\i3gfPctK1c2x.aspx`

### 10. What three CVEs did this exploit leverage? (Provide the answer in ascending order)

Based on the `CISA` Conti Ransomware threat advisory referenced in Task 1, list the three critical vulnerabilities commonly exploited by Conti operators in ascending numerical order.

```text
FortiOS & SMBGhost CVEs from CISA Advisory (Ascending Order)
```

**Answer:** `CVE-2018-13374,CVE-2018-13379,CVE-2020-0796`

## 💡 Key Takeaways

* **`EventCode` vs. `EventID` in `Splunk`**: Different `Splunk` add-ons parse the Windows Event ID into either `EventCode` or `EventID`. Always run `index=* | stats count by index sourcetype` first and inspect the **Left Fields Sidebar** instead of guessing field names.
* **High-Signal `Sysmon` Event Codes**:
  * `EventCode=1` (`Process Create`): Reveals suspicious paths (`Documents\cmd.exe`), `MD5` hashes, and attacker commands (`net user /add`, `attrib.exe`).
  * `EventCode=8` (`CreateRemoteThread`): Immediately exposes process migration (`powershell.exe` -> `unsecapp.exe`) and credential dumping (`lsass.exe`).
  * `EventCode=11` (`FileCreate`): Tracks ransomware note drops (`readme.txt`) across the filesystem ([TryHackMe Conti](https://tryhackme.com/room/contiransomwarehgh)).
