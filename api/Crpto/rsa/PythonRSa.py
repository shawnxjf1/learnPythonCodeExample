#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2018/8/19'
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
import rsa
import base64

def generateKey():
    (pubkey, privkey) = rsa.newkeys(169)
    print('pubkey:  %s,\n privkey:  %s' % (pubkey, privkey))
    pub = pubkey.save_pkcs1('PEM').decode()  ## public.pem','w+' ,decode后不能用wb
    with open('public.pem', 'w+') as myfile:
        myfile.write(pub)
        myfile.close()
    pri = privkey.save_pkcs1('PEM').decode()
    with open('private.pem', 'w+') as myfile:
        myfile.write(pri)
        myfile.close()
    message = 'helloworld-python'

    with open('public.pem', 'r') as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read())
        print('pubkey%s'%pubkey)

    with open('private.pem', 'r') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read())
        print('privkey%s'%privkey)

    ## OverflowError: 17 bytes needed for message, but there is only space for 10
    crypto = base64.b64encode(rsa.encrypt(message.encode(encoding="UTF-8"), pubkey))  # 私钥解密
    message = rsa.decrypt(base64.b64dncode(crypto), privkey)
    print(message)

    # 导入密钥


if __name__ == "__main__":
    generateKey()
