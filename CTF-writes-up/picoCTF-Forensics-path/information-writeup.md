# Information — Forensics (Easy) — picoCTF 2021

## Challenge Description
> Files can always be changed in a secret way. Can you find the flag?

**Hints:**
1. Look closely at the image's details.
2. The flag format is `picoCTF{...}`.

**Provided file:** `cat.jpg`

## Walkthrough

### 1. Downloading the file
Downloaded the provided image locally.

### 2. Examining metadata with ExifTool
Since the hint pointed at the image's "details," the natural first move in an image-forensics challenge is to check its metadata rather than the pixels themselves:

```bash
exiftool cat.jpg
```

Buried in the metadata output was an unusual encoded string that clearly didn't belong there.

### 3. Decoding the string
Copied the encoded string into **CyberChef** and ran it through a decoding recipe. It resolved cleanly and directly into the flag — no extra steps needed.

## Flag
```
picoCTF{...}
```
*(Value intentionally redacted — this writeup documents the method, not the answer, for readers who haven't solved it yet.)*

## Key Takeaway
- EXIF/metadata fields are one of the first places to check in any image-forensics challenge — data hidden there survives even when the image itself looks completely normal.
- CyberChef is a fast way to identify and decode an unknown encoded string without having to guess the cipher by hand.
- [add your own biggest takeaway here]

## Tools Used
`ExifTool` · `CyberChef`
