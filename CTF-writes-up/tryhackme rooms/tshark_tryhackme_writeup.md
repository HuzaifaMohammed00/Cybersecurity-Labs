# TShark — Network Forensics (Easy) — TryHackMe

## Challenge Description

TShark is a powerful command-line network protocol analyzer developed by the Wireshark team. This lab focuses on analyzing packet captures (`.cap` / `.pcap`) directly from the terminal, filtering DNS records, extracting specific fields, and investigating a DNS data exfiltration attack to recover an encoded flag.

**Room Link:** [TryHackMe - TShark](https://tryhackme.com/room/tshark)

---

## Walkthrough

### Task 1: Pre-Reqs & Installation

Verifying that `tshark` is installed and inspecting its version:

```bash
tshark -v
```

---

### Task 2: Reading PCAP Files (`dns.cap`)

#### 1. How many packets are in the dns.cap file?
To count the total number of packets without a GUI, read the capture with `-r` and pipe the output to `wc -l`:

```bash
tshark -r dns.cap | wc -l
```
**Answer:** `38`

#### 2. How many A records are in the capture? (Including responses)
Filter specifically for DNS A records using display filter `-Y "dns.qry.type == 1"`:

```bash
tshark -r dns.cap -Y "dns.qry.type == 1" | wc -l
```
*Note: In the DNS protocol, Type 1 represents an IPv4 address (A record). Since responses also echo query details, this filter captures both.*

**Answer:** `6`

#### 3. Which A record was present the most?
Extract the queried domain names using `-T fields -e dns.qry.name`, then chain standard Linux pipeline tools (`sort` and `uniq -c`) to aggregate and count occurrences automatically:

```bash
tshark -r dns.cap -Y "dns.qry.type == 1" -T fields -e dns.qry.name | sort | uniq -c | sort -nr | head -n 1
```

**Answer:** `GRIMM.utelsystems.local`

---

### Task 3: DNS Exfil Investigation (`dns_exfil.pcap`)

An alert indicated that a host on the network was exfiltrating data covertly over DNS queries.

#### 1. How many packets are in this capture?
```bash
tshark -r dns_exfil.pcap | wc -l
```
**Answer:** `125`

#### 2. How many DNS queries are in this pcap? (Not responses!)
To isolate client queries from server responses, apply the boolean filter `dns.flags.response == 0`:

```bash
tshark -r dns_exfil.pcap -Y "dns.flags.response == 0" | wc -l
```
**Answer:** `56`

#### 3. What is the DNS transaction ID of the suspicious queries (in hex)?
Inspecting the capture in Wireshark for the initial queries revealed an anomalous hardcoded transaction ID across the suspicious domain lookups:

- **Path:** `Domain Name System (query)` -> `Transaction ID`

**Answer:** `0xbeef`

#### 4. What is the string extracted from the DNS queries?
Each DNS query exfiltrated a single character encoded within the first position of the subdomain prefix. We can automate the extraction using `tshark`, slice the first character with `cut -c 1`, and strip newline characters with `tr -d '\n'` to assemble the contiguous payload:

```bash
tshark -r dns_exfil.pcap -Y "dns.flags.response == 0" -T fields -e dns.qry.name | cut -c 1 | tr -d '\n'
```

**Extracted String:** `MZWGCZ33ORUDC427NFZV65BQOVTWQX3XNF2GQMDVG5PXI43IGRZGWIL5`

#### 5. What is the flag?
Examining the character set (strictly uppercase A–Z and digits 2–7) identifies the payload as **Base32** encoding (RFC 4648). Decoding it via the terminal:

```bash
echo -n "MZWGCZ33ORUDC427NFZV65BQOVTWQX3XNF2GQMDVG5PXI43IGRZGWIL5" | base32 -d
```

**Flag:** `flag{th1s_is_t0ugh_with0u7_tsh4rk!}`

---

## Key Takeaways

- **CLI Speed vs. GUI Clarity**: While Wireshark provides quick visual identification for anomalous fields (like Transaction ID `0xbeef`), `tshark` combined with Unix pipelines (`wc`, `cut`, `sort`, `uniq`, `tr`) enables rapid, scalable data carving and extraction.
- **DNS Exfiltration Signatures**: Attackers frequently abuse DNS queries to bypass perimeter firewalls. Key indicators include high volumes of unique subdomains, low TTLs, anomalous transaction IDs, and encoded prefixes (Base32/Base64/Hex).
- **Encoding Recognition**: Base32 uses only `A-Z` and `2-7`, making it ideal for DNS query payloads where case sensitivity might be flattened by intermediate resolvers.

---

## Tools Used

- **TShark** (CLI Packet Analyzer)
- **Wireshark** (GUI Inspection)
- **Linux Coreutils** (`wc`, `cut`, `tr`, `sort`, `uniq`, `base32`)
