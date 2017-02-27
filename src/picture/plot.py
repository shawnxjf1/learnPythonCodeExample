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
from pylab import *

def showSin():
    n = 256
    X = np.linspace(-np.pi,np.pi,n,endpoint=True)
    Y = np.sin(2*X)

    plot (X, Y+1, color='blue', alpha=1.00)
    plot (X, Y-1, color='blue', alpha=1.00)
    show()
    """
    处理
    """

def showPlot():
    n = 256
    x = range(1,10,0.26)
    y = range(1,10,0.26)
    plot (x,y, color='blue', alpha=1.00)
    show()


