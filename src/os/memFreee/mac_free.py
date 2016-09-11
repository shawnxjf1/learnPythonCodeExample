#!/usr/bin/python
#encoding=utf-8
'''
Created on 2016年2月14日

@author: shawn
'''

#######################################执行出的结果如下############################################
#1.该程序输出程序正在运行的进程 和 内存信息。

#  2016-09-11 11:31:18,823 - DEBUG - Start of program，ps=   RSS COMM
# 519972 eclipse
# 444020 Google Chrome Helper
# 404420 YoudaoNote
# 216468 Google Chrome Helper
# 216316 QQ
# 208588 Google Chrome
# 
#    724 -bash
#    632 mdflagwriter
#    608 pboard
#    352 periodic-wrapper
# 
# Wired Memory:        1845 MB
# Active Memory:        3130 MB
# Inactive Memory:    1454 MB
# Free Memory:        356 MB
# Real Mem Total (ps):    6519.406 MB
#################################################################################################


import subprocess
import re

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#打印日志到文件
#logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#要做的打印日志进行调试。

#注意：在shell脚本中直接调，没有写成函数也可以。

def print_mac_free():
# Get process info
    ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0]
    
    logging.debug('Start of program，ps=' + ps)
    
    vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0]
    
    # Iterate processes
    processLines = ps.split('\n')
    sep = re.compile('[\s]+')
    rssTotal = 0 # kB
    for row in range(1,len(processLines)):
        rowText = processLines[row].strip()
        rowElements = sep.split(rowText)
        try:
            rss = float(rowElements[0]) * 1024
        except:
            rss = 0 # ignore...
        rssTotal += rss
    
    # Process vm_stat
    vmLines = vm.split('\n')
    sep = re.compile(':[\s]+')
    vmStats = {}
    for row in range(1,len(vmLines)-2):
        rowText = vmLines[row].strip()
        rowElements = sep.split(rowText)
        vmStats[(rowElements[0])] = int(rowElements[1].strip('\.')) * 4096
    
    print 'Wired Memory:\t\t%d MB' % ( vmStats["Pages wired down"]/1024/1024 )
    print 'Active Memory:\t\t%d MB' % ( vmStats["Pages active"]/1024/1024 )
    print 'Inactive Memory:\t%d MB' % ( vmStats["Pages inactive"]/1024/1024 )
    print 'Free Memory:\t\t%d MB' % ( vmStats["Pages free"]/1024/1024 )
    print 'Real Mem Total (ps):\t%.3f MB' % ( rssTotal/1024/1024 )

if __name__ == '__main__':
    print_mac_free()