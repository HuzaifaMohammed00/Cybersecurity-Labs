# Transfer Protocol — Forensics (Medium) — picoCTF 2021

## Challenge Description
> Figure out how the flag was moved, and get me the flag.
> **Hint:** What are some other ways to hide data?

**Provided file:** `tftp.pcapng`

## Walkthrough

### 1. Getting the capture into Wireshark
Downloaded the provided capture file (`tftp.pcapng`) with `wget`, then opened it in Wireshark for analysis.

### 2. Reading the challenge name as a clue
The challenge title itself was the first hint: "Transfer Protocol" points directly at **TFTP (Trivial File Transfer Protocol)**. Applied a `tftp` display filter in Wireshark to isolate the relevant traffic.

### 3. Following the stream
Right-clicked the first TFTP packet → **Follow → UDP Stream** (TFTP runs over UDP) to read the reassembled conversation. Inside the stream was a short block of encoded/encrypted-looking text.

### 4. Decoding the hidden note
Copied the encoded string and ran it through an online cipher decoder. It decoded to a plaintext note along the lines of:

> "TFTP does not encrypt our traffic, so we must discover a way to hide the flag. I'll take a look at **the plan**."

The phrase *"the plan"* stood out as a deliberate clue rather than filler text.

### 5. Exporting the transferred files
Back in Wireshark: **File → Export Objects → TFTP**. This revealed 4 files that had been transferred over TFTP, including one named `plan` — matching the clue from the decoded note. Saved all 4 files locally.

The 4 files were:
- 1 instructions/readme-style file
- 3 image files

### 6. Reading the instructions file
The instructions file explained that the flag had been hidden inside one of the images using **Steghide**, and pointed to "check out the photos."

### 7. Extracting with Steghide
Ran Steghide against each image using the passphrase recovered from the decoded note in step 4:

```bash
steghide extract -sf <image_name> -p "<passphrase from step 4>"
```

Tried this against all three images. Extraction succeeded on the third image, producing `flag.txt`.

### 8. Reading the flag
```bash
cat flag.txt
```

## Flag
```
[paste flag value here]
```

## Key Takeaway
- TFTP is a plaintext, unencrypted protocol — anything sent over it (including hidden clues) can be fully reconstructed from a packet capture via Wireshark's stream-follow and object-export features.
- Steganography (via tools like Steghide) is often layered *on top of* a network-forensics challenge, not instead of it — the network capture is what delivers the passphrase and the carrier files.
- [add your own biggest takeaway here]

## Tools Used
`Wireshark` · `TFTP object export` · `Steghide` · online cipher decoder
