# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 19:01:44 2018

@author: Administrator
"""

import pandas
#创建一个读取内置文件的类
class ConfigTable():
    def __init__(self,dir):
        self.dir = dir#配置文件地址
        self.info = self.readTable()
    #读取文件信息
    def readTable(self):
        info = {}
        with open(self.dir) as cf:
            while True:
                tmp = cf.readline()
                if not tmp:
                    break
                else:
                    tmp = tmp.replace(' ','')
                    name,rate = tmp.split('=')
                    info[name] = float(rate)
            return info
    #返回所须缴纳的费用
    def fee(self,cash):
        rate = 0
        for tmp in self.info:
            if tmp not in ['JiShuH','JiShuL']:
                rate = rate + self.info[tmp]
        self.rate = rate
        if cash >16446:
            return 16446*rate
        elif cash<2193:
            return 2193*rate
        else:
            return cash*rate