#!/usr/bin/python
import sys
import json
import re
class all_info(object):
    def __init__(self,name,sex,age,addr,tel):
        self.name=name
        self.age=age
        self.addr=addr
        self.tel=tel
        self.sex=sex
    def search_all(self):
        all_data=json.dumps(self,ensure_ascii=False)
        return all_data
    def add_info(self,c_put):
        self.append(c_put)
        finally_reason='添加成功'
        return finally_reason
    def del_info(self,re_info):
        for info in self:
            if re_info in info.values():
                self.remove(info)
                finally_reason='删除成功'
                return finally_reason
    def to_search(self,info):
        count=0
        com_info=info.split(' ')
        for info in self:
            for s in com_info:
                if s in info.values():
                    count=count+1
            if count==len(com_info):
                finally_reason=json.dumps(info)
                return finally_reason
            else:
                finally_reason='没有此人'
                return finally_reason
    def xg_info(self,xg):
        change=xg.split(' ')
        for info in self:
            count=0
            for key in info:
                if info[key]==change[0]:
                    info[key]=change[1]
                    count=count+1
            if count==1:
                return json.dumps(info)
        if count==0:
            finally_reason='没有找到相应数据'
            return finally_reason
    def re_ch(self,re_date):
        count=0
        s=r'.*'+re_date
        for info in self:
            for val in info.values():
                su = re.match(s,val)
                if su:
                    return json.dumps(info)
                    count +=1
        if count==0:
            finally_reason='没有此人'
            return finally_reason
    def save_info(self):
        s_j=json.dumps(self,ensure_ascii=False)
        fileobject=open('log.json','w')
        fileobject.write(s_j)
        fileobject.close() 
        finally_reason='转存成功'
        return finally_reason

