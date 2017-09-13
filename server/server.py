#!/usr/bin/python
import socket
import json
import re
import sys
import txl_module
import pickle
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
            put_num=pickle.loads(connect.recv(1024))
            if put_num=='4':
                connect.send(pickle.dumps(txl_module.all_info.search_all(l)))
            if put_num=='1':
                name=pickle.loads(connect.recv(1024))
                age=pickle.loads(connect.recv(1024))
                tel=pickle.loads(connect.recv(1024))
                sex=pickle.loads(connect.recv(1024))
                addr=pickle.loads(connect.recv(1024))
                allinfo=[name,age,tel,sex,addr]
                connect.send(pickle.dumps(txl_module.all_info.add_info(l,allinfo)))
            if put_num=='2':
                dell_info=pickle.loads(connect.recv(1024))
                connect.send(pickle.dumps(txl_module.all_info.del_info(l,dell_info)))
            if put_num=='3':
                two_info=pickle.loads(connect.recv(1024))
                connect.send(pickle.dumps(txl_module.all_info.to_search(l,two_info)))
            if put_num=='5':
                change=pickle.loads(connect.recv(1024))
                connect.send(pickle.dumps(txl_module.all_info.xg_info(l,change)))
            if put_num=='6':
                connect.send(pickle.dumps(txl_module.all_info.save_info(l)))
            if put_num=='7':
                m_h=connect.recv(1024).decode()
                connect.send(pickle.dumps(txl_module.all_info.re_ch(l,m_h)))
