import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))
server.listen(1)

conn, addr = server.accept()
print("Conectado:", addr)

data = conn.recv(1024)
print(data.decode())

conn.sendall(b"HTTP/1.1 200 OK\r\n\r\nHello World")

conn.close()
server.close()
