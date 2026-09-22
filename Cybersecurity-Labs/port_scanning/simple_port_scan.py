import socket

# creat object and idintfy the type of connection
# AF_INET mean use IPv4 protocol
# socket.SOCK_STREAM mean use TCP connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("welcome to simple port scan ")
port = int(input("enter the number of the port to scan: "))
result = mysock.connect_ex(("45.33.32.156", port))
# if connection seccuss return 0
print(result)
