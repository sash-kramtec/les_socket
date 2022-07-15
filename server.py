import socket

#HOST = "localhost"
PORT = 25290

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() # Получить имя локального хоста
print("server: Start", host, PORT)
server_sock.bind((host, PORT))
print("server: Bind")
server_sock.listen(5)


while True:
    print("server: Listen")
    sock, addr = server_sock.accept()
    print("server: Connect ", addr)

    while True:
        data_bytes = sock.recv(1024)
        if not data_bytes:
            break
        data = data_bytes.decode()  # (bytes to str)    
        print("Received:", data)
        sock.send(data_bytes)
        if data == "0":
            break

    print("server: Disconnect")
    sock.close()

print("server: Stop")

