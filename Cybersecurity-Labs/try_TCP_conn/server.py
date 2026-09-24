import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind(("127.0.0.1", 65535))
server_sock.listen()
print("server is listing on the port 65535....")
conn,add = server_sock.accept()
data = conn.recv(1024)
print (data.decode())
conn.sendall(b"Hello from server!")