# TCP Server (`server.py`)

The server side of a simple TCP client/server experiment. It listens on a local port, waits for **one** client to connect, reads the message the client sends, prints it, and sends a reply.

## Code

```python
import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind(("127.0.0.1", 65535))
server_sock.listen()
print("server is listing on the port 65535....")
conn, add = server_sock.accept()
data = conn.recv(1024)
print(data.decode())
conn.sendall(b"Hello from server!")
```

## Line by line

| Code | What it does |
|------|--------------|
| `import socket` | Loads Python's standard networking module. It is a thin wrapper around the operating system's networking functions. |
| `socket.socket(AF_INET, SOCK_STREAM)` | Creates a socket. `AF_INET` means IPv4, and `SOCK_STREAM` means TCP (a reliable, ordered stream of bytes). |
| `bind(("127.0.0.1", 65535))` | Reserves an IP address and a port for this program. `127.0.0.1` is localhost (loopback), so only this machine can connect. The IP must belong to the machine, otherwise `bind` fails. |
| `listen()` | Switches the socket to the `LISTEN` state. From here the operating system itself accepts incoming connection requests and queues the completed ones. |
| `accept()` | Blocks (waits) until a client connects, then returns two values: `conn`, a **new socket** dedicated to that client, and the client's address `(IP, port)`. |
| `conn.recv(1024)` | Reads up to 1024 bytes from the client. It blocks until data arrives. An empty result (`b""`) means the client closed the connection. |
| `data.decode()` | Converts the received bytes into a string. |
| `conn.sendall(b"...")` | Sends the whole reply to the client. The `b` prefix means the text is bytes, because the network carries bytes, not strings. |

**Why two sockets?** `server_sock` is like the door of a shop: its only job is to receive new visitors. `accept()` gives each visitor a private line, `conn`, so the door stays free to listen. The second value returned by `accept()` (`add` in the code) is the client's address. It is not used yet, but it is useful for logging or blocking specific IPs.

## What happens behind the scenes

1. `socket()` asks the OS for a new socket. Nothing is sent on the network yet.
2. `bind()` reserves `127.0.0.1:65535` for this program.
3. `listen()` puts the socket in `LISTEN` state. The OS now answers connection requests on this port without running any Python code.
4. When a client connects, the **three-way handshake** (`SYN`, `SYN-ACK`, `ACK`) is completed by the two operating systems.
5. `accept()` takes the ready connection from the queue and returns `conn` and the client's address.
6. `recv()` reads the client's data from a buffer in the OS, and `sendall()` writes the reply back.

## How to run

Start the server first, in its own terminal:

```
python server.py
```

It prints the listening message and then waits. That waiting is `accept()`, and it is normal. Then run the client (see `client.md`) in a second terminal.

Expected output on the server after the client connects:

```
server is listing on the port 65535....
Hello serever!
```

## Limitations and next steps

- This first version handles **one client and then exits**, because there is no loop.
- Add a `while True:` loop around `accept()` so the server keeps running and serves client after client.
- Close the connection with `conn.close()` when finished with a client.
- Handle several clients at the same time (for example with threads).
- Use the client's address (`add`) for logging.
- Choose a port in the application range (for example `5000` or `8080`) instead of `65535`, which is in the range the OS uses for random client ports.
