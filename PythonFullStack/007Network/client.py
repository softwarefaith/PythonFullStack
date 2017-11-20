
import socket


ip_port = ('127.0.0.1', 8888)

sk = socket.socket()
data = sk.connect(ip_port)
#sk.settimeout(5)

while True:
    data = sk.recv(1024)
    print('receive:', data.decode('utf8'))
    inp = input('please input:')
    print('----'+inp)
    if not len(inp):
       inp = input('re-input:')
       print('----' + inp)
    sk.sendall(inp.encode('utf8'))
    if inp == 'exit':
        break

sk.close()