#!/usr/bin/env python
# coding=utf-8
from computeSize import getMbSize
import os,math,cv2

DSTPATH='/home/wyj/公共的/已修改'
SRCPATH='/home/wyj/公共的/未修改'
DSTSIZE=1.0#目标文件大小，单位MB

#获取文件名列表
def getPathList(path):#path为源文件存储路径
    pathList=os.listdir(path)
    return pathList

#获取压缩率
#size为源文件大小，单位MB
#dstSize为目标文件大小，单位MB
def resizeRate(size,dstSize):
    rate = math.ceil((size / dstSize) * 10) / 10 + 0.1
    rate = math.sqrt(rate)
    rate = 1.0 / rate
    return rate

#压缩文件
#rate压缩率
#srcPath源文件路径
#dstPath目标文件路径
def compressImage(rate,srcPath,dstPath):
    image=cv2.imread(srcPath)
    imResized=cv2.resize(image,None,fx=rate,fy=rate)
    cv2.imwrite(dstPath,imResized)

if __name__=='__main__':
    pathList=getPathList(SRCPATH)
    for p in pathList:
        size=getMbSize(os.path.join(SRCPATH,p))
        if size<DSTSIZE:
            os.system('cp '+os.path.join(SRCPATH,p)+' '+os.path.join(DSTPATH,p))
        else:
            rate=resizeRate(size,DSTSIZE)
            compressImage(rate,os.path.join(SRCPATH,p),os.path.join(DSTPATH,p))
            while getMbSize(os.path.join(DSTPATH,p))>DSTSIZE:
                size=getMbSize(os.path.join(DSTPATH,p))
                rate=resizeRate(size,DSTSIZE)
                compressImage(rate,os.path.join(DSTPATH,p),os.path.join(DSTPATH,p))
