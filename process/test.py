# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:12:38 2018

@author: Administrator
"""

from multiprocessing import Process,Queue
import os
from configtable import ConfigTable
from excelTable import EmpTable
from multiprocessing import Pool,Pipe
import pandas

con1,con2 = Pipe()
con3,con3 = Pipe()
#得到员工信息
def read_emp():
    emp_info  = EmpTable('F:\python程序\process\emp.xlsx')
    con1.send(emp_info)
    print('read {}'.format(os.getpid()))
#计算员工信息
def cal():
    print('cal head {}')
    emp = con2.recv()
    print('call {}'.format(os.getpid()))
    print(emp)
    dt = emp.detail('F:\python程序\process\config.txt')
    print(dt)
    que.put(dt)
#写入信息
def write_data():
    dt = que.get()
    print('write {}'.format(os.getpid()))
    print(dt)
    
def main():
    p1 = Process(target = read_emp)
    p2 = Process(target = cal)
    p3 = Process(target = write_data)
    p1.start()
    p2.start()
    
if __name__ == '__main__':
    print('this main {}'.format(os.getpid()))
    main()
    
    