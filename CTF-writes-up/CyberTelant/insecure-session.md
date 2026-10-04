# Insecure Session

## Challenge Info

- **Platform:** CyberTalents
- **Category:** Web Security
- **Challenge Name:** Who Am I?
- **Link:** https://cybertalents.com/challenges/web/who-am-i

## Description

A simple challenge demonstrating a **Broken Access Control / Insecure Session Management** vulnerability, where the server fully trusts data stored in a client-side cookie without performing any real server-side identity verification.

## Steps

### 1. Initial Page Visit
Opened the challenge link and found a regular login page, with no known credentials (no username or password given).

### 2. Inspecting the Source Code
Used browser tools (Inspect / View Page Source) and found a comment in the HTML containing guest credentials:

```
Username: Guest
Password: Guest
```

### 3. Logging In as Guest
Logged in with these credentials and got in as `Guest`, but with limited privileges (access denied when trying to reach admin content).

### 4. Inspecting the Cookie
Opened browser DevTools and checked the Cookies, found a cookie named `Authentication` with a `Base64`-encoded value:

```
bG9naW49R3Vlc3Q%3D
```

### 5. Decoding the Cookie
Decoded the value and got:

```
login=Guest
```

### 6. First Attempt (Failed)
Changed the value directly to `login=admin` without encoding it, and placed it in the cookie.
**Result:** Failed — the server rejected it because it wasn't encoded in the expected format.

### 7. Fixing the Mistake (Success)
Encoded `login=admin` fully in `Base64`, the same way the original value was:

```
login=admin  →  Base64  →  bG9naW49YWRtaW4=
```

### 8. Replacing the Cookie and Reloading
Replaced the old cookie value with the new encoded one, and refreshed the page.
**Result:** Logged in as `admin` and got the flag.

## Root Cause

The server fully trusts the cookie value coming from the user without any validation, signature, or server-side session lookup. This allows any user to escalate their privileges simply by modifying and re-encoding the cookie value.

## Lesson Learned

- Never rely on client-side data (like cookies) to determine user privileges without server-side verification.
- Secure session management should use:
  - Random, unguessable Session IDs tied to server-side state.
  - Signed tokens (e.g. a `JWT` signed with a secret key) instead of storing plain, editable data.
  - Authorization checks performed server-side on every request, not based on what the client sends.
