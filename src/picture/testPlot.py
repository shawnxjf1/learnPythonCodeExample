#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2017/2/22'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import unittest
import os
from pylab import *
import numpy as numpy
import math
from src.logging.logUtil import info
from src.logging.logUtil import debuger
## from ..logging.logUtil import *   出错:SystemError: Parent module '' not loaded, cannot perform relative import

## x轴最大长度
maxX = 100
xtransfer = 1
yAllTransfer = 2
## 计算出变化的X数组范围
def generateVariationX():

    intensityX = 5
    intensityXa = 4
    intensityXb = 2
    intensityC = 3

    X = numpy.linspace(1,10,50)
    Xa = numpy.linspace(10,30,(30-10)*intensityXa)  ## type(Xa) :numpy.ndarray
    Xb = numpy.linspace(30,60,(60-10)*intensityXb)
    Xc = numpy.linspace(60,maxX,(maxX-60)*intensityC)
    Xall = []
    # Xall.append(X.tolist())
    # Xall.append(Xa.tolist())
    # Xall.append(Xb.tolist())  ## [[x],[xa],[xb]] 会是这样的结果<br>
    Xall = Xall + X.tolist()
    Xall += Xa.tolist()
    Xall += Xb.tolist()
    Xall += Xc.tolist()
    return Xall

## 里面暂时注释,暂时没有想到更好的办法
def getYTransfer(x):
    # if x < 30 and x>0:
    #     return 1 + 1.0/x
    # elif x > 30 and x<60:
    #     return 2
    # else:
    #     return 3
    # return x*x
    return math.log2(x)

def showTransferSinPicture():
    Xall = generateVariationX()
    Y = []
    for i in Xall:
        y = transferSin(i,getYTransfer(i))
        Y.append(y)
    plt.plot(Xall, Y,'k.',linewidth=3)

    Y1 = []
    X1 = []
    x = math.pi/2/xtransfer  ## 极大值
    while x <= maxX :
        Y1.append(transferSin(x,getYTransfer(x)))
        X1.append(x)
        x += math.pi*2/xtransfer

    Y2 = []
    X2 = []
    x = math.pi*(3/2/xtransfer) ## 极小值
    while x <= maxX :
        Y2.append(transferSin(x,getYTransfer(x)))
        X2.append(x)
        x += math.pi*2/xtransfer

    plt.plot(X1, Y1,color='red')
    plt.plot(X2, Y2,color='red')

    ## 给X Y轴打标记
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.show()


def transferSin(x,ytransfer):
    return 1 + (1.0/(10+ytransfer*x))*math.sin(xtransfer*x)

## 变形sin 显示
def showSelfMakeSinPicture():
    x = []
    currentX = 1;
    for i in range(1,101,1):
        currentX += 0.1
        x.append(currentX)

    print(x)

    numeratorY = 0.5
    y = []
    currentY = 0.0
    for j in x:
        currentY += (numeratorY/j)
        y.append(currentY)

    print(y)

    numeratorY1 = 0.5
    y1 = []
    currentY1 = 30.0
    for j in x:
        currentY1 -= (numeratorY1/j)
        y1.append(currentY1)

    print(y1)


    qArr = []
    currentQu = y[0]
    ## 摇摆线分成10段
    for i in range (1,11,1): ## 这里必须是0-9 ,不然后面的
        ## 分成10 段,每一段就是一个上升一个下降曲线
        pointNm = 5 ## 这一段应该描多少点,描点的数量
        ## 注意这里所有的下标访问都 -1 ,因为list第一个位置为从0开始的


        ## 获取最高点 最低点,然后计算出中间会描出多少点,然后根据多少个点 计算出递增的值。
        m1a = 0
        if i == 1:
            m1a = (y1[i*10 - 5 -1 ]-y[0])/pointNm
        else:
            m1a = (y1[i*10 - 5 -1 ]-y[(i-1) *10 -1])/pointNm  ## 升降的曲率

        #info("begin={0},end={1},step={2}=".format(y[0],y1[i*10 - 5 -1 ],m1a)

        ## currentQu += m1a
        for j in range(pointNm):
            currentQu += m1a
            qArr.append(currentQu)

        info("currentQu += m1a, = %q".format(q=currentQu))

        print('y1[i*10 - 5 -1 ]=' + str(y1[i*10 - 5 -1 ]))
        print('currentQu=' + str(currentQu))

        #if i != 10:
        m1d = (y1[i*10 -5 -1] - y[i*10 -1 ])/pointNm
        for j in range(pointNm):
            currentQu -= m1d
            qArr.append(currentQu)


    plt.plot(x,y,color='red')
    plt.plot(x,y1,color='red')
    ## plt.plot(x,qArr,color='black',linestyle='dashed') ## 画虚线
    plt.plot(x,qArr,color='black',linestyle='point') ## 画点
    plt.show()




"""
from plot import showPlot 报红线
"""

# 此测试用例可以执行。
class Test(unittest.TestCase):
    def setUp(self):
        print('test unitest  setup')

    def tearDown(self):
        print('test unitest  teardown')

    def testShowTransferSinPicture(self):
        showTransferSinPicture()
        ## 2017年01月01日 输出  Testing started at 上午11:04 ..., logging/testLog.log文件

    def testShowSelfMakePoint(self):
        showSelfMakeSinPicture()