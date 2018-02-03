# -*- coding: utf-8 -*-
"""
from multiprocessing import Process,Queue
import os
from configtable import ConfigTable
from excelTable import EmpTable
from multiprocessing import Pool,Pipe
import pandas
c1,c2 = Pipe()
def a():
    c1.send('asdas')
def v():
    d = c2.recv()
    print(d)
def main():
    p1 = Process(target = a)
    p2 = Process(target = v)
    p1.start()
    p2.start()
if __name__ == '__main__':
    main()
"""
from multiprocessing import Process, Pipe

conn1, conn2 = Pipe()

def f1():
    conn1.send('Hello shiyanlou')

def f2():
    data = conn2.recv()
    print(data)

def main():
    Process(target=f1).start()
    Process(target=f2).start()

if __name__ == '__main__':
    main()