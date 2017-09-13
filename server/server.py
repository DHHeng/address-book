#!/usr/bin/python
import socket
import json
import re
import sys
import txl_module
js_info=open('log.json','r')
l=json.loads(js_info.read())
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.2',9999))
sock.listen(5)
print('waiting for connect')
connect,addr=sock.accept()
while True:
    if __name__=='__main__':
        while True:
            put_num=connect.recv(1024).decode()
            if put_num=='4':
                connect.send(txl_module.all_info.search_all(l).encode('utf-8'))
            if put_num=='1':
                name=connect.recv(1024).decode()
                age=connect.recv(1024).decode()
                tel=connect.recv(1024).decode()
                sex=connect.recv(1024).decode()
                addr=connect.recv(1024).decode()
                allinfo=[name,age,tel,sex,addr]
                connect.send(txl_module.all_info.add_info(l,allinfo).encode('utf-8'))
            if put_num=='2':
                dell_info=connect.recv(1024).decode()
                connect.send(txl_module.all_info.del_info(l,dell_info).encode('utf-8'))
            if put_num=='3':
                two_info=connect.recv(1024).decode()
                connect.send(txl_module.all_info.to_search(l,two_info).encode('utf-8'))
            if put_num=='5':
                change=connect.recv(1024).decode()
                connect.send(txl_module.all_info.xg_info(l,change).encode())
            if put_num=='6':
                connect.send(txl_module.all_info.save_info(l).encode('utf-8'))
            if put_num=='7':
                m_h=connect.recv(1024).decode()
                connect.send(txl_module.all_info.re_ch(l,m_h).encode('ascii'))
