import socket

PORT = 25290
host = "localhost"

#host = socket.gethostname() # Получить имя локального хоста

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        if "quit" in data:
            break        
        data = "server responce: " + data
        data_bytes = data.encode()
        sock.send(data_bytes)


    print("server: Disconnect")
    sock.close()

print("server: Stop")

