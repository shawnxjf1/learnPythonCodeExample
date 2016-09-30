#encoding=UTF-8
'''2016-09-26
@author: shawn
'''
import openpyxl
import datetime
from  datetime  import  *

#datetime __slot__
#assert name in ("utcoffset", "dst")

##输出：成功

#D:\同步盘\Project\拉卡拉行政\加班报销\(201604-加班交通费及餐费明细表.xlsx
def loadOverWorkExcel(fileName):
    wb = openpyxl.load_workbook(fileName)
    sheet = wb.get_sheet_by_name("0412")
    #sheet = wb.active
    for i in range(4, 8):
        c = sheet.cell(row=i, column=3)
        '''注意 print语句 %s s在%后面'''
        print("c.value.type=%s and c.value=%s"%(type(c.value),c.value)) ##<class 'datetime.time'> and c.value=20:41:00 - (excel当中就是h:mm单元格的格式)
        overWorkCriterion = time(20,00,0)
        ##datetime 可以通过<  > 直接比较大小,如果有问题程序会终止 AssertionError: c.value > overWorkCriterion
        assert c.value > overWorkCriterion, 'c.value > overWorkCriterion'
        now = datetime.now()
        datatimeBaseLine = datetime(now.year,now.month,now.day,20,00,0,0)
        actualWorkTime = c.value
        actualworkDateTime = datetime(now.year,now.month,now.day,actualWorkTime.hour,actualWorkTime.minute,actualWorkTime.second,0)
        '''技术点： unsupported operand type(s) for -: 'datetime.time' and 'datetime.time' '''
        overTimeDelta = actualworkDateTime - datatimeBaseLine  ## unsupported operand type(s) for +: 'datetime.timedelta' and 'int'
        print("overTimeDelta=%s" % (overTimeDelta))

        halfHourNumber = int(convertTimeDeltaTominutes(overTimeDelta)/30)/2 + 2
        c = sheet.cell(row=i, column=12)
        c.value = halfHourNumber
        wb.save("201604.xlsx")

        # if c.value > overWorkCriterion:
        #     assert
def convertTimeDeltaTominutes(overTimeDelta):
    '''
    # 注意这里的秒是转化之后的，比如overTimeDelat=0:41:00,and seconds = 2460
    :param overTimeDelta:
    :return:
    '''
    seconds = overTimeDelta.seconds
    print('overTimeDelat=%s,and seconds = %s' % (overTimeDelta,seconds))
    # hour = overTimeDelta._seconds
    #minute = overTimeDelta._minutes
    totalMinute = seconds//60
    return totalMinute
    # totalMinute = hour * 60 + minute
