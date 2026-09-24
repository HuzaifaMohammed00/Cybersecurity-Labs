# TCP Client (`clint.py`)

The client side of a simple TCP client/server experiment. It connects to the server, sends a message, and prints the server's reply.

## Code

```python
import socket

clint_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clint_sock.connect_ex(("127.0.0.1", 65535))
print("connected successfully ... ")

clint_sock.sendall("Hello serever!".encode())
print(clint_sock.recv(1024).decode())
```

## Line by line

| Code | What it does |
|------|--------------|
| `socket.socket(AF_INET, SOCK_STREAM)` | Creates a TCP socket over IPv4, the same kind the server uses. |
| `connect_ex(("127.0.0.1", 65535))` | Tries to connect to the server's IP and port. The OS picks a random source port for the client automatically. |
| `sendall("...".encode())` | Sends the message. `.encode()` converts the string to bytes, and `sendall` keeps sending until every byte is sent. |
| `recv(1024)` | Waits for the server's reply and reads up to 1024 bytes. |
| `.decode()` | Converts the reply from bytes back to a string. |

### `connect` vs `connect_ex`

- `connect()` raises an exception if the connection fails.
- `connect_ex()` does not raise an exception. It returns an error code instead: `0` means success, and any other number means failure (for example `10061` on Windows when the connection is refused).

`connect_ex` is handy for port scanning, because many ports can be checked without a `try/except` for each one.

### `send` vs `sendall`

- `send()` sends what it can and returns the number of bytes actually sent, which can be less than the full message.
- `sendall()` repeats until the whole message is sent, so it is the safer choice.

## What happens behind the scenes

1. `connect_ex()` makes the OS choose a random source port (for example `54321`) and send a `SYN` packet to `127.0.0.1:65535`.
2. The server's OS replies with `SYN-ACK`, and the client's OS answers with `ACK`. This is the **three-way handshake**, and the connection is now `ESTABLISHED`.
3. `sendall()` puts the bytes into the connection, and the server's OS delivers them to the server's buffer.
4. `recv()` waits until the server's reply arrives.
5. When the script ends, the socket closes and both sides exchange `FIN` and `ACK` packets to end the connection.

Because the address is `127.0.0.1` (loopback), the packets never leave the machine.

## How to run

1. Start the server first (see `server.md`).
2. In a second terminal, run:

```
python clint.py
```

Expected output on the client:

```
connected successfully ...
Hello from server!
```

If the server is not running, the connection is refused.

## Limitations and next steps

- `connect_ex` returns a result, but this version never checks it, so **"connected successfully" is printed even if the connection failed**. Check that the return value is `0` before printing, or use `connect()` inside `try/except ConnectionRefusedError`.
- The message is fixed. A next step is to read the message from the user with `input()`.
- Close the socket with `clint_sock.close()` when finished.
- Once the server has a loop, try connecting several times, or from several terminals.
- Capture the traffic with Wireshark on the loopback interface (filter `tcp.port == 65535`) to see `SYN`, `SYN-ACK`, `ACK`, the data, and `FIN`.
