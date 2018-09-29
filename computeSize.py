#!/usr/bin/env python
# coding=utf-8
import os

PATH='/home/wyj/公共的/未修改/李工资2.jpg'

def getMbSize(path):#获取以MB为单位的源文件容量
    try:
        size=os.path.getsize(path)
    except Exception as err:
        print(err)
    mb=float(size)/1024/1024
    return mb

if __name__=='__main__':
    print(getMbSize(PATH))
