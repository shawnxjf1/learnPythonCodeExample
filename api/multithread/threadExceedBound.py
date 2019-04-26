#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2017/1/1'
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
import threading

threads = []
stepLength = 3
def threadExecTemplate():
    i = 1
    while i <10:
        print("i = " + str(i) + "currentThread=")
        temp_thread = threading.Thread(target=threadRange, args=(i,stepLength))
        threads.append(temp_thread)
        i = i + stepLength

    for t in threads:
        t.setDaemon(True)
        t.start()

    for tj in threads:
        tj.join()

def threadRange(start,length):
    for j in range(start,start + length):
        print('---> thread start = {0} and end = {1}'.format(start,j))



if __name__ == '__main__':
    threadExecTemplate()