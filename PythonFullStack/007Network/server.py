#!/usr/bin/env python
# coding:utf-8


import socket

WELCOME = '欢迎致电 10086，请输入1xxx,0转人工服务.'

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1', 8888)
sk.bind(address)
sk.listen(10)


while True:
    print ('server waiting...')
    connection, address = sk.accept()
    print(connection, address)
    connection.sendall(bytes(WELCOME, 'utf8'))

    flag = True
    while flag:
        client_data = connection.recv(1024)
        print(client_data)
        if not len(client_data):
            print('空...')
            connection.sendall(bytes("请重新输入", 'utf8'))
            continue
        if client_data == b"exit":
            Flag = False
        elif client_data == b'0':
            connection.sendall(bytes("您的通话可能被录音", 'utf8'))
        else:
            connection.sendall(client_data)

    connection.close()

sk.close()

def main():
    pass

if __name__ == '__main__':
    main()