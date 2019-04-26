#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2018/8/30'
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

all = [4026, 4022, 4021, 4020, 4018, 4016, 4012, 4010, 3942, 3940, 3941, 3939, 3933, 3926, 3920, 3911, 3910, 3904, 3903, 3890]

order = [3890, 3904, 3910, 3911, 3920, 3926, 3939, 3940, 3941, 3942]

print("all %s" % all)
all_length = len(all)
order_length = len(order)
# print('all lenth %s,order lenth%s' % (all_length,order_length))
# for i in range(all_length):
#     print("序号：%s   值：%s" % (i + 1, all[i]))
#     if (all[i] in order):
#         del all[i]

# for a in all:
#     print("inex:%s compare%s" %(all.index(a) +1 ,a))
#     if (a in order):
#         all.remove(a)

newAll  = filter(lambda x: x not in order, all)  ## 这个是正确的<br>

print("===========================")

for i in newAll:
    print(i)


print(len(newAll))

## 参考:https://www.cnblogs.com/james0/p/7993444.html
