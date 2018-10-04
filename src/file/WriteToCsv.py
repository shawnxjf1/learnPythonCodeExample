#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2018/8/19'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import csv
import sys
import os
import rsa
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

env_dist = os.environ

fileName = env_dist['CVS_FILE']

master_public = env_dist['CVS_PUBLIC']


def searchRecord(domain):
    with open(fileName,'r',encoding='utf8') as myFile:
        lines=csv.reader(myFile)
        for line in lines:
            if line[0]==domain:
                print("line=%s" % line)
                return 1
        return 0

def writeRecoreToFile(domain,userName,pwd,cipher):
    with open(fileName,"a") as f:
        f = csv.writer(f)
        cipher_text = base64.b64encode(cipher.encrypt(pwd.encode(encoding="utf-8")))  # 通过生成的对象加密message明文，注意，在python3中加密的数据必须是bytes类型的数据，不能是str类型的数据
        f.writerow([domain,userName,cipher_text.decode(encoding='utf-8')])

# def writeToFile():
#     with open(publicfile, "r") as f:
#         key = f.read()
#         rsakey = RSA.importKey(key)  # 导入读取到的公钥
#         cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
#         writeRecoreToFile('www.baidu.com', 'shawnxjf', '123456', cipher)
#         ## writeRecoreToFile(sys.argv[1],sys.argv[2],sys.argv[3],cipher)
#     print("write success")

## python3版本执行: python3 WriteToCsv.py
if __name__ == "__main__":
    print(os.path.abspath(os.curdir))
    # print(sys.version_info)
    #writeToFile();

    if searchRecord(sys.argv[1]) == 1:
        print("domain exist")
    else:
        with open(master_public, "r") as f:
            key = f.read()
            rsakey = RSA.importKey(key)  # 导入读取到的公钥
            cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
            #writeRecoreToFile('www.baidu.com','shawnxjf','123456',cipher)
            writeRecoreToFile(sys.argv[1],sys.argv[2],sys.argv[3],cipher)
        print("write success")

    # input = input("Please input method:")
    # if input == 1:
    #     writeRecoreToFile(sys.argv[1],sys.argv[2],sys.argv[3])
    # elif input == 2:
    #     searchRecord(sys.argv[1])
