
import socket


ip_port = ('127.0.0.1',9999)

sk = socket.socket()
data = sk.connect(ip_port)
print('>>>>>')
inStr = input()
sk.sendall(inStr.encode())

server_reply = sk.recv(1024)



sk.close()