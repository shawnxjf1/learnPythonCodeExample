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

master_private = env_dist['CVS_PRIVATE']

def searchRecord(domain,cipher):
    with open(fileName,'r') as myFile:
        lines=csv.reader(myFile)
        existFlag = False
        for line in lines:
            if line[0]==domain:
                ## pwd = line[2].decode(encoding='UTF-8')
                line[2] = cipher.decrypt(base64.b64decode(line[2]), "ERROR")  # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str
                line[2] = line[2].decode() ## cipher.decrypt后是byte类型 如 b'123456'
                print("line=%s" % line)
                existFlag = True
                break
        if (not existFlag):
            print("domain not exist")


## python3版本执行: python3 WriteToCsv.py
if __name__ == "__main__":
    with open(master_private, "r") as f:
            key = f.read()
            rsakey = RSA.importKey(key)  # 导入读取到的公钥
            cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
            searchRecord(sys.argv[1],cipher)
