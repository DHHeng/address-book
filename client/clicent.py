#!/usr/bin/python
import socket
import pickle
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.2',9999))
print('welcome')
while True:
    print('请输入您要进行的操作：1：添加 2：删除 3：组合查找 4：查看所有 5：修改 6：转存 7：模糊查找')
    client_put=input('please input choose:')
    sock.send(pickle.dumps(client_put))
    if client_put=='1':
        all_info={}
        put_name=input('please input name:')
        put_age=input('please input age:') 
        put_tel=input('please input tel:')
        put_sex=input('please input sex:')
        put_add=input('please input add:')
        all_info={'name':put_name,'age':put_age,'tel':put_tel,'sex':put_sex,'add':put_add}
        pickle_info=pickle.dumps(all_info)
        sock.send(pickle_info) 
        print(pickle.loads(sock.recv(1024)))
    if client_put=='2':
        del_info=input('请输入要删除的信息：')
        sock.send(pickle.dumps(del_info))
        print(pickle.loads(sock.recv(1024)))
    if client_put=='3':
        to_info=input('请输入组合信息，用空格隔开：')
        sock.send(pickle.dumps(to_info))
        print(pickle.loads(sock.recv(1024)))
    if client_put=='4':
        print(pickle.loads(sock.recv(10241024)))
    if client_put=='5':
        xg=input('请输入需要查找的信息（第一个为原始信息，第二个为修改后的信息）')
        sock.send(pickle.dumps(xg))
        print(pickle.loads(sock.recv(1024)))
    if client_put=='6':
        print(pickle.loads(sock.recv(1024)))
    if client_put=='7':
        re_put=input('请输入您需要查找的信息：')
        sock.send(pickle.dumps(re_put))
        print(pickle.dumps(sock.recv(1024)))
            
