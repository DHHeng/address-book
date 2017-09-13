#!/usr/bin/python
import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.2',9999))
print('welcome')
while True:
    print('请输入您要进行的操作：1：添加 2：删除 3：组合查找 4：查看所有 5：修改 6：转存 7：模糊查找')
    client_put=input('please input choose:')
    sock.send(client_put.encode('utf-8'))
    if client_put=='1':
        put_name=input('please input name:')
        sock.send(put_name.encode('utf-8'))
        put_age=input('please input age:')
        sock.send(put_age.encode('ascii')) 
        put_tel=input('please input tel:')
        sock.send(put_tel.encode('ascii')) 
        put_sex=input('please input sex:')
        sock.send(put_sex.encode('utf-8')) 
        put_add=input('please input add:')
        sock.send(put_add.encode('utf-8')) 
        print(sock.recv(1024).decode())
    if client_put=='2':
        del_info=input('请输入要删除的信息：')
        sock.send(del_info.encode('utf-8'))
        print(sock.recv(1024).decode())
    if client_put=='3':
        to_info=input('请输入组合信息，用空格隔开：')
        sock.send(to_info.encode('utf-8'))
        print(sock.recv(1024).decode('utf-8'))
    if client_put=='4':
        print(sock.recv(1024).decode('utf-8'))
    if client_put=='5':
        xg=input('请输入需要查找的信息（第一个为原始信息，第二个为修改后的信息）')
        sock.send(xg.encode('utf-8'))
        print(sock.recv(1024).decode())
    if client_put=='6':
        print(sock.recv(1024).decode())
    if client_put=='7':
        re_put=input('请输入您需要查找的信息：')
        sock.send(re_put.encode('utf-8'))
        print(sock.recv(1024).decode())
            
