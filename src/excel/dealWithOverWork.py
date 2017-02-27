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
def loadOverWorkExcel(fileName,beginIndex,endIndex,destFileName):
    wb = openpyxl.load_workbook(fileName)
    sheet = wb.get_sheet_by_name("0412")
    #sheet = wb.active
    for i in range(beginIndex,endIndex):
        c = sheet.cell(row=i, column=3)
        '''注意 print语句 %s s在%后面'''
        print("c.value.type=%s and c.value=%s"%(type(c.value),c.value)) ##<class 'datetime.time'> and c.value=20:41:00 - (excel当中就是h:mm单元格的格式)
        overWorkCriterion = time(20,00,0)
        ##datetime 可以通过<  > 直接比较大小,如果有问题程序会终止 AssertionError: c.value > overWorkCriterion

        #TypeError: unorderable         types: datetime.datetime() > datetime.time()
        #assert c.value > overWorkCriterion, 'c.value > overWorkCriterion'
        now = datetime.now()
        datatimeBaseLine = datetime(now.year,now.month,now.day,20,00,0,0)

        if c.value == None:
            continue
        actualworkDateTime = patchActualWorkTime(c.value)
        week = getWeekFromTime(actualworkDateTime)
        shordateStr = getShortDateStr(actualworkDateTime)

        '''技术点： unsupported operand type(s) for -: 'datetime.time' and 'datetime.time' '''
        overTimeDelta = actualworkDateTime - datatimeBaseLine  ## unsupported operand type(s) for +: 'datetime.timedelta' and 'int'
        print("overTimeDelta=%s,and index=%s and filename=%s" % (overTimeDelta,i,fileName))

        halfHourNumber = int(convertTimeDeltaTominutes(overTimeDelta)/30)/2 + 2
        cTimeCount = sheet.cell(row=i, column=12)
        cTimeCount.value = halfHourNumber

        cWeek = sheet.cell(row=i, column=13)
        cWeek.value = week

        cShortDate = sheet.cell(row=i, column=14)
        cShortDate.value = shordateStr

        #201604.xlsx
        wb.save(destFileName)

def getWeekFromTime(actualworkDateTime):
    return '星期%s ' % actualworkDateTime.strftime('%w')

def getShortDateStr(actualworkDateTime):
    return '%s月%s日 ' % (actualworkDateTime.strftime('%m'),actualworkDateTime.strftime('%d'))



def patchActualWorkTime(actualWorkTime):

    # excel 中的值为：2016/5/9 20:18:52，则c.value.type=<class 'str'> and c.value=2016/5/4 20:04:49，所以需要改成20:18的格式
    ##判断类型想到了微信读书：python 86个注意点中说到判断的那一章
    now = datetime.now()
    if isinstance(actualWorkTime,datetime):
        actualworkDateTime = datetime(now.year, now.month, now.day, actualWorkTime.hour, actualWorkTime.minute,
                                      actualWorkTime.second, 0)
    elif isinstance(actualWorkTime,str):
        actualWorkTime = convertStrToDateTime(actualWorkTime)
    print("actualworktime=%s" % actualWorkTime)
    return actualWorkTime

#时间格式类似于：2016/5/9 20:18:52,抽出出时分秒
##问题；如果year month 截取出来为空怎么办
def convertStrToDateTime(timeStr):
    try:
        firstColonIndex = timeStr.index(':')
        firstSlashIndex = timeStr.index('/')
        hour = timeStr[firstColonIndex - 2:firstColonIndex]
        minute = timeStr[firstColonIndex + 1:firstColonIndex + 3]
        second = timeStr[firstColonIndex + 4:]

        year = timeStr[:firstSlashIndex]

        secondSlashIndex = timeStr.index('/', firstSlashIndex + 1)
        month = timeStr[firstSlashIndex + 1: secondSlashIndex]

        blankIndex = timeStr.index(' ', secondSlashIndex + 1)
        day = timeStr[secondSlashIndex + 1: blankIndex]

        year = year.strip()
        month = month.strip()
        day = day.strip()
        hour = hour.strip()
        second = second.strip()
    except TypeError:
        print("convertStrToDateTime-typeError,%s" % (timeStr))
    actualworkDateTime = datetime(int(year), int(month), int(day), int(hour), int(minute),int(second), 0)
    return actualworkDateTime;


def convertTimeDeltaTominutes(overTimeDelta):
    '''
    # 注意timeDelta秒是转化之后的，比如overTimeDelat=0:41:00,and seconds = 2460（所有小时分钟折算成的秒）
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
