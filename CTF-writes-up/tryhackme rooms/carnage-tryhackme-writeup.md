# **🕵️ TryHackMe: Carnage — Walkthrough**

**Author:** Huzaifa Mohammed  
**Platform:** [TryHackMe — Carnage](https://tryhackme.com/room/c2carnage)  
**Category:** Network Forensics (Wireshark & VirusTotal)

# **📌 Scenario**

An employee (Eric Fischer, IP: `10.9.23.102`) opened a malicious Word document from a phishing email and clicked **"Enable Content."** We need to analyze the PCAP file in Wireshark to track the attack step by step.

**Setup Step before starting:**  
Set the time format in `Wireshark` to UTC so all timestamps match the room format (yyyy-mm-dd hh:mm:ss):

`View -> Time Display Format -> UTC Date and Time of Day`

# **🔍 Step-by-Step Walkthrough**

## **1\. What was the date and time for the first HTTP connection to the malicious IP?**

Filter for HTTP traffic and look for the first request where the victim (10.9.23.102) downloads a file:

http In Frame `1735`, we see `GET /documents.zip`. Check the `Time` column.

**Answer:** `2021-09-24 16:44:38`

## **2\. What is the name of the zip file that was downloaded?**

Look at the Info column of the same packet (GET /documents.zip HTTP/1.1).

**Answer:** `documents.zip`

## **3\. What was the domain hosting the malicious zip file?**

Right-click Frame 1735 \-\> Follow \-\> HTTP Stream. Look at the Host header in the red request section.

**Answer:** `attirenepal.com`

## **4\. Without downloading the file, what is the name of the file in the zip file?**

Stay in the same HTTP Stream window and scroll down to the blue server response. .zip files start with PK and store the filenames inside them in plain text right after `PK`:

`PK..........chart-1530076591.xls`  
**Answer:** `chart-1530076591.xls`

## **5\. What is the name of the webserver of the malicious IP from which the zip file was downloaded?**

In the same `HTTP Stream` window, check the `Server` header in the blue response section.

**Answer:** `LiteSpeed`

## **6\. What is the version of the webserver from the previous question?**

Right below the Server header, look at the X-Powered-By header.

**Answer:** `PHP/7.2.34`

## **7\. Malicious files were downloaded to the victim host from multiple domains. What were the three domains involved with this activity?**

Even though `HTTPS` is encrypted, the first handshake packet (Client Hello, type 1\) shows the domain name in plain text inside the `SNI (Server Name Indication)` field. Using the room's time hint (16:45:11 to 16:45:30), apply this filter:

`tls.handshake.type == 1 && frame.time >= "2021-09-24 16:45:11" && frame.time <= "2021-09-24 16:45:30"`Check the `Server Name` field in those packets and ignore normal Microsoft domains.

**Answer:** `finejewels.com.au, thietbiagt.com, new.americold.com`

## **8\. Which certificate authority issued the SSL certificate to the first domain from the previous question?**

Filter for SSL Certificate packets (type 11\) at the same time as the first domain (`16:45:11`):

`tls.handshake.type == 11` Open the packet details: `Transport Layer Security -> Handshake Protocol: Certificate -> Certificates -> issuer -> rdnSequence`.

**Answer:** `GoDaddy`

## **9\. What are the two IP addresses of the Cobalt Strike servers?**

Open the IP conversation list in `Wireshark`:

`Statistics -> Conversations -> IPv4`Copy the external IPs communicating with the victim and search them on [VirusTotal](https://www.virustotal.com/). Check the Community tab for each IP to see which ones are flagged by researchers as Cobalt Strike C2 servers.

**Answer:** `185.106.96.158, 185.125.204.174`

## **10\. What is the Host header for the first Cobalt Strike IP address from the previous question?**

Filter for HTTP traffic to the first Cobalt Strike IP (or check its details on VirusTotal):

ip.addr \== 185.106.96.158 && httpOpen the HTTP request headers to see the fake `Host` header used to disguise the traffic.

**Answer:** `ocsp.verisign.com`

## **11\. What is the domain name for the first IP address of the Cobalt Strike server?**

Search `185.106.96.158` on [VirusTotal](https://www.virustotal.com/) and check the Relations / Community tab (or filter dns.a \== 185.106.96.158 in `Wireshark`).

**Answer:** `survmeter.live`

## **12\. What is the domain name of the second Cobalt Strike server IP?**

Search the second IP (185.125.204.174) on [VirusTotal](https://www.virustotal.com/) (or filter `dns.a == 185.125.204.174` in Wireshark).

**Answer**: securitybusinpuff.com

## **13\. What is the domain name of the post-infection traffic?**

After infection, the malware sends data out using `HTTP POST` requests. Filter for `POST` requests:

`http.request.method == "POST"` Check the Host header of the first suspicious POST request sent by the victim.

**Answer:** `maldivehost.net`

## **14\. What are the first eleven characters that the victim host sends out to the malicious domain involved in the post-infection traffic?**

Right-click that first `POST` packet \-\> `Follow` \-\> `HTTP Stream`. Read the first 11 characters sent at the top of the red request (`POST /zLIisQRWZI9...`).

**Answer:** `zLIisQRWZI9`

## **15\. What was the length for the first packet sent out to the C2 server?**

Look at the Length column in Wireshark for that same first POST packet.

**Answer:** `281`

## **16\. What was the Server header for the malicious domain from the previous question?**

In the same HTTP Stream window for maldivehost.net, check the Server header in the blue response section.

**Answer:** `Apache/2.4.49 (cPanel) OpenSSL/1.1.1l mod_bwlimited/1.4`

## **17\. The malware used an API to check for the IP address of the victim's machine. What was the date and time when the DNS query for the IP check domain occurred?**

To find the DNS query where the malware checks the victim's public IP via an API, filter for `dns` packets containing the word `"api"`:

`dns && frame contains "api"` Look at the `Time` column of the first query for `api.ipify.org`.

**Answer:** `2021-09-24 17:00:04 UTC`

## **18\. What was the domain in the DNS query from the previous question?**

Read the domain name from the Info column of that same DNS packet.

**Answer:** `api.ipify.org`

## **19\. Looks like there was some malicious spam (malspam) activity going on. What was the first MAIL FROM address observed in the traffic?**

Filter for SMTP email traffic containing FROM:

smtp contains "FROM"Check the first packet in the list to see the sender email address.

**Answer:** `farshin@mailfa.com`

## **20\. How many packets were observed for the SMTP traffic?**

Filter for all `SMTP` traffic:

`smtp`Look at the bottom bar of `Wireshark` next to **`Display:`** to see the total packet count.

**Answer:** `🙂 find it by your self (:`

# **💡 Key Takeaways**

* **Read ZIP contents without extracting:** `Follow -> HTTP Stream` lets you see filenames inside a `.zip` archive right after the `PK` header bytes.  
* **Spot domains in encrypted HTTPS:** `tls.handshake.type == 1` (`Client Hello`) reveals requested domains in plain text via `SNI`, and `tls.handshake.type == 11` reveals the SSL Certificate issuer.  
* **Use VirusTotal Community:** When an IP looks clean on the main scan page, the **Community** tab often reveals `Cobalt Strike` C2 servers.

