import socket
import select

ip_port = ('127.0.0.1', 8888)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)


while True:
    inputs, outputs, errors = select.select([sk], [], [],5)

    for tempSK in inputs:
        conn, address = tempSK.accept()
        print('conn:'+conn)
        data = conn.recv(1024)
        print(data.decode('utf8'))
        conn.sendall("no problem".encode('utf8'))


