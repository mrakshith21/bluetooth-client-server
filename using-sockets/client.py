# Sample client code that connects to a server and sends some data

import socket

# MAC address of the server
bt_addr = '34:E6:AD:A0:6A:58'
port = 4
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect((bt_addr, port))
print("Connected to server", (bt_addr, port))

data = "Hello World!"
client.send(data.encode())

client.close()
