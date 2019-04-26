#-*- coding:utf8 -*-
# name: 身份证号码生存器0.0.1
# author: Sola
# data:24Jun2016

#!/usr/bin/env python
#-*-coding:utf8-*-
import random
import os
import time
## 2019-4-1 没有测试成功<br>

def id_creator(distinct='341003', birth=time.strftime("%Y%m%d", time.localtime())):
    last42 = random.randint(0,99)
    if last42 < 10:
        last3 = '0' + str(last42)
    else:
        last3 = str(last42)
    gender = input("input your gender(1=male,0=female):")
    last2 = list(filter(lambda i: i % 2 == gender, range(10)))[random.randint(0,4)]
    first_seventeen = distinct + birth + last3 + str(last2)
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    d = 0
    for i in range(len(first_seventeen)):
        d += int(first_seventeen[i]) * weight[i]
    rslt = [1, 0, 'x', 9, 8, 7, 6, 5, 4, 3, 2]
    print ('-' * 20)
    print ("id is: ", first_seventeen + str(rslt[d%11]))
    print ('\n')

def main():
    print ("enter e for changing distinct code")
    print ("enter w for creating id")
    print ("enter r for creating id without birthday")
    print ("enter q for quiting ")
    code = input("please input your command:")
    if code == 'e':
        distinct = input("please input your distinct code:".decode('utf8').encode('gbk'))
        if len(distinct) == 6:
            birth = input("input ur birthday(format:yyyymmdd):".decode('utf8').encode("gbk"))
            try:
                if len(birth) == 0:
                    id_creator(distinct=distinct)
                if time.strptime(birth, '%Y%m%d'):
                    id_creator(distinct=distinct, birth=birth)
            except:
                print ('u input a wrong birthday number \n')
        else:
            print ('u input a wrong distinct number \n')
        main()
    if code == 'w':
        birth = input("input ur birthday(format:yyyymmdd):")
        try:
            if len(birth) == 0:
                id_creator()
            if time.strptime(birth, '%Y%m%d'):
                id_creator(birth=birth)
        except:
            print ("u input a wrong birthday number \n")
        main()
    if code == 'r':
        age = input("please input ur age:")
        age = int(age)
        year = str(int(time.strftime("%Y", time.localtime())) - age)
        month = time.strftime("%m%d", time.localtime())
        birth = year + month
        id_creator(birth=birth)
        main()
    if code == 'q':
        os.system("exit")
    else:
        print ('wrong command')


if __name__ == "__main__":
    main()