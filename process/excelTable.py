# -*- coding: utf-8 -*-
import pandas
import configtable
import sys
#读取EXCEL表中的员工信息
class EmpTable():
    def __init__(self,dir):
        self.dir = dir#获取员工表的地址
        self.info = self.readTable()
    #获取员工表信息
    def readTable(self):
        info = pandas.read_excel(self.dir)
        return info
    #得到所需要提交的信息
    def detail(self,cfdir):
       cf = configtable.ConfigTable(cfdir)
       dt = self.info
       dt['fee'] = dt.salary.apply(cf.fee)
       return dt
if __name__ == '__main__':
    key = {}
    #接收命令行参数
    key[sys.argv[1]] = sys.argv[2]
    key[sys.argv[3]] = sys.argv[4]
    e = EmpTable(key['-c'])
    e.detail(key['-d'])