import socket

HOST = "192.168.1.103"
PORT = 25290

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock)

sock.connect((HOST, PORT))
print(sock)

while True:  
    
    data = input("Type the message to send:")
    if data == "0":
        break
    data_bytes = data.encode()  # (str to bytes)    
    sock.sendall(data_bytes)  # Send    
    data_bytes = sock.recv(1024)  # Receive    
    data = data_bytes.decode()  # (bytes to str)    
    print("Received:", data)

print("client: Stop")
sock.close()
