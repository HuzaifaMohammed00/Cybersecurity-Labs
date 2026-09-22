import socket

# creat object and idintfy the type of connection
# AF_INET mean use IPv4 protocol
# socket.SOCK_STREAM mean use TCP connection


def get_info_about_the_scan():
    print("welcome to port scanning ")
    ip = input("enter the IP number for the scanning: ")
    port = int(input("enter the number of the port to scan: "))
    return ip, port


def port_scan():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip, port = get_info_about_the_scan()
    result = mysock.connect_ex((ip, port))
    if result == 0:
        return "its open"
    else:
        return "its not open"


if __name__ == "__main__":
    result = port_scan()
    print(result)
