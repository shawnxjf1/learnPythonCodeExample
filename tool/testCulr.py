# -*- coding: utf-8 -*-


import os
def testCurl():
    for i in range(1,10):
        tmpres = os.popen('curl %s' % "localhost:8001/hello").readlines();
        print(tmpres)


##
def testGatewayRateLimit():
    gatewayTestUlr =  "http://localhost:9999/admin/aliauth/web/mocktest"
    adminUlrl = "http://localhost:6001/aliauth/web/mocktest"
    for i in range(1,10):
        tmpres = os.popen('curl %s' % gatewayTestUlr).readlines();
        print(tmpres)

if __name__ == "__main__":
    testGatewayRateLimit()