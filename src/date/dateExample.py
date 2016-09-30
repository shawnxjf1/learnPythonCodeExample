#encoding=UTF-8
import unittest
from datetime import date
from datetime import datetime
from datetime import timedelta
from datetime import time


'''
问题：timedelta没有hours,minutes,_seconds 属性，但是有class里有self._hours,->怎么看一个类有哪些属性.
'''

def dateFunction():
    now = date.today()
    tomorrow = now.replace(day=7)
    delta = tomorrow - now
    print ('now:', now, ' tomorrow:', tomorrow)
    print ('timedelta:', delta)
    print (now + delta)
    print (tomorrow > now)
# # ---- 结果 ----
#程序执行在2016年9月30日
# now: 2016-09-30  tomorrow: 2016-09-07
# timedelta: -23 days, 0:00:00
# 2016-09-07
# False

# class Test(unittest.TestCase):
#     def setUp(self):
#         print('test unitest  setup')
#
#     def tearDown(self):
#         print('test unitest  teardown')
#
#     def testDate(self):
#         dateFunction()


# datetime、date、time都提供了strftime()方法，该方法接收一个格式字符串，输出日期时间的字符串表示
'''
%a 星期的简写。如 星期三为Web
%A 星期的全写。如 星期三为Wednesday
%b 月份的简写。如4月份为Apr
%B月份的全写。如4月份为April
%c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）
%d:  日在这个月中的天数（是这个月的第几天）
%f:  微秒（范围[0,999999]）
%H:  小时（24小时制，[0, 23]）
%I:  小时（12小时制，[0, 11]）
%j:  日在年中的天数 [001,366]（是当年的第几天）
%m:  月份（[01,12]）
%M:  分钟（[00,59]）
%p:  AM或者PM
%S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
%U:  周在当年的周数当年的第几周），星期天作为周的第一天
%w:  今天在这周的天数，范围为[0, 6]，6表示星期天
%W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
%x:  日期字符串（如：04/07/10）
%X:  时间字符串（如：10:43:39）
%y:  2个数字表示的年份
%Y:  4个数字表示的年份
%z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
%Z:  时区名称（如果是本地时间，返回空字符串）
%%:  %% => %
'''

def dateTimeArithmetic():
    now = datetime.now()
    ct = time(20,20,20)
    past = datetime(now.year, now.month, now.day, ct.hour, ct.minute, ct.second, 16)
    pasttime = past.time()
    print('past.time=%s'% (pasttime))


def timedeltaFunction():
    #FIXME
    pass

def strftimeFunction():
    dt = datetime.now()
    print(    '(%Y-%m-%d %H:%M:%S %f): ', dt.strftime('%Y-%m-%d %H:%M:%S %f'))
    print(    '(%Y-%m-%d %H:%M:%S %p): ', dt.strftime('%y-%m-%d %I:%M:%S %p'))
    print(    '%%a: %s ' % dt.strftime('%a'))
    print(    '%%A: %s ' % dt.strftime('%A'))
    print(    '%%b: %s ' % dt.strftime('%b'))
    print(    '%%B: %s ' % dt.strftime('%B'))
    print(    '日期时间%%c: %s ' % dt.strftime('%c'))
    print(    '日期%%x：%s ' % dt.strftime('%x'))
    print(    '时间%%X：%s ' % dt.strftime('%X'))
    print(    '今天是这周的第%s天 ' % dt.strftime('%w'))
    print(    '今天是今年的第%s天 ' % dt.strftime('%j'))
    print(    '今周是今年的第%s周 ' % dt.strftime('%U'))


if __name__ == "__main__":
    dateFunction()
    strftimeFunction()
    dateTimeArithmetic()
    # unittest.main()
