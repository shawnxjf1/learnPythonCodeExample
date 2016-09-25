'''
目前测试的
>>> str(b)
'-6452.12012'
>>> bstr= str(b)
>>> bstr.index('-')
0
>>> bstr.index('+')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    bstr.index('+')
ValueError: substring not found
>>> bstr.find('-')
0
>>> bstr.find('+')
-1
>>> bstr.index('.')
5
>>> cstr= '123.456.789'
>>> cstr.index('.')
3

'''