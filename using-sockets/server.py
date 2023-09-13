# Sample server code that accepts connections from clients and some data

import socket

# Bluetooth adapter MAC address
host_addr = '34:E6:AD:A0:6A:58'
port = 4

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind((host_addr, port))
server.listen(1)

client, address = server.accept()

print("Connected to client", address)
data = client.recv(20)
print("Data received:", str(data))

server.close()
client.close()
