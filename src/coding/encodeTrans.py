#encoding=utf-8

#首先要搞清楚，字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
#decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串转换成unicode编码。
#encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串转换成gb2312编码。

'''
python3.4 以后没有unicode？ 待确认->看python核心编程
>>> str2=u"\201"
>>> type(str2)
<class 'str'>
'''

