#encoding=UTF-8
'''
Created on 2016年9月4日

@author: shawn
'''

#coding=utf-8  
import threading   
from time import sleep, ctime   
   
loops = ['a','b']                      #睡眠时间  
   
def loop(nloop, nsec):  
    print('Start loop', nloop, 'at:', ctime() ) 
    sleep(nsec)   
    print ('Loop', nloop, 'done at:', ctime())  
      
   
def main():  
    print ('Starting at:', ctime())  
    threads = []  
    nloops = range(len(loops))     #列表[0,1]  
          
    #创建线程  
    for i in nloops:  
        t = threading.Thread(target=loop,args=(i,loops[i]))  
        threads.append(t)  
  
    #开始线程  
    for i in nloops:  
        threads[i].start()  
  
    #等待所有结束线程  
    for i in nloops:  
        threads[i].join()  
  
    print ('All end:', ctime())   
  
if __name__ == '__main__':   
    main()  