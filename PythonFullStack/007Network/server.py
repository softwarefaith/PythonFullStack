#!/usr/bin/env python
# coding:utf-8


import socket


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1', 9999)
sk.bind(address)
sk.listen(10)


while True:
    print ('server waiting...')
    connection, address = sk.accept()
    print(connection)
    print(address)
    client_data =  connection.recv(1024)
    print(client_data)
    connection.send('Hello Word'.encode('utf-8'))
    connection.close()

def main():
    pass

if __name__ == '__main__':
    main()