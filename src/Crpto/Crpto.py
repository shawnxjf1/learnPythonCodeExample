#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2018/8/26'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64


# 伪随机数生成器
random_generator = Random.new().read

# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

# master的秘钥对的生成
private_pem = rsa.exportKey()

#--------------------------------------------生成公私钥对文件-----------------------------------------------------------
# with open('master-private.pem', 'wb') as f:
#     f.write(private_pem)
#
# public_pem = rsa.publickey().exportKey()
# with open('master-public.pem', 'wb') as f:
#     f.write(public_pem)


with open('ghost-private.pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('ghost-public.pem', 'wb') as f:
    f.write(public_pem)



message = 'hello ghost, this is a plian text'

with open('master-public.pem',"r") as f:
     key = f.read()
     rsakey = RSA.importKey(key)  # 导入读取到的公钥
     cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
     cipher_text = base64.b64encode(cipher.encrypt(message.encode(encoding="utf-8")))  # 通过生成的对象加密message明文，注意，在python3中加密的数据必须是bytes类型的数据，不能是str类型的数据
     ## type(base64.b64decode('RgDZH/fOD4yob41IZYr5krlz')) <class 'bytes'>编码过后的都是 bytes
     print(cipher_text)

with open('master-private.pem') as f:
    print('#########################')
    key = f.read()
    rsakey = RSA.importKey(key)  # 导入读取到的私钥
    cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    cipher_text = "b'RgDZH/fOD4yob41IZYr5krlzWqcQrrH1FkKZUVcQ1ESnl9nT6kl7JHSSYO6lzEc+wgvkqKPMofTf9bOI86k7fAEWsaPivo9LKOWGJPnrznLs2BO98ZlNT/G30aWjXibma1WoC7lChOtyT1jPNYFLjHpb1WOauYyTX8DoecOkcxo='"
    text = cipher.decrypt(base64.b64decode(cipher_text), "ERROR")  # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str
    print(text)
    print(text.decode())
    ## b'hello ghost, this is a plian text'
    ## hello ghost, this is a plian text
print("#######################")







