import socket

clint_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clint_sock.connect_ex(("127.0.0.1", 65535))
print("connected successfully ... ")

clint_sock.sendall("Hello serever!".encode())
print(clint_sock.recv(1024).decode())
