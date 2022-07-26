import socket

PORT = 25290
#host = "localhost"
host = ""
#host = socket.gethostname() # Получить имя локального хоста


if __name__ == '__main__':

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        print("server: Start", host, PORT)
        server_sock.bind((host, PORT))
        print("server: Bind")
        server_sock.listen(5)
        while True:
            print("server: Listen")
            sock, addr = server_sock.accept()
            print("server: Connect ", addr)
            with sock:
                print("Connected by ...", addr)
                while True:
                    #Receive
                    try:
                        data_bytes = sock.recv(1024)
                    except ConnectionError:
                        print(f"Client suddenly closed while receiving")
                        break
                    data = data_bytes.decode()  # (bytes to str)
                    print("Received:", data)
                    if "quit" in data:
                        break        
                    data = "server responce: " + data
                    data_bytes = data.encode()
                    try:
                        sock.sendall(data_bytes)
                    except:
                        print(f"Client suddenly closed, can't send")
                        break
                print("Disconnected by ", addr)
                #sock.close()

        print("server: Stop")

