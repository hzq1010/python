# coding=utf8
# import mysql.connector
import binascii


# 报文头
def reverseStart_field():
    return "F5F5"


# 返回序列
def reverseNumber_field():
    return "0001"


# 补全字节
def zfill(str1, i):
    str1 = str1.zfill(2 * i)  # 补全 字节
    return str1


# int转16进制
def intChange16(str1, i):
    str1 = hex(int(str1))  # 转16进制
    str1 = str1.replace("0x", "")  # 去掉16进制0x
    str1 = str1.zfill(2 * i)  # 补全 字节
    return str1


# 16进制 去掉0x　补全 字节
def strReplace(str1, i):
    str1 = str1.replace("0x", "")  # 去掉16进制0x
    str1 = str1.zfill(2 * i)  # 补全 字节
    return str1


# int转16进制 倒序
def change16Reverse(str1, i):
    # print("==========调用方法change16Reverse")
    str1 = hex(int(str1))  # 转16进制
    str1 = str1.replace("0x", "")  # 去掉16进制0x
    str1 = str1.zfill(2 * i)  # 补全 字节
    # print("==========倒序之前:",str1)
    i = len(str1)
    str2 = ""
    while (i > 0):
        str2 = str2 + (str1[i - 2:i])
        i = i - 2
        # print("==========倒序之后:",str2)
    return str2


# 时间转16进制
def timeChange16(str1):
    arrTime = []
    arrTime = str1.split('-')
    arrChange = []
    strChange = ""
    i = 0
    while (i < len(arrTime)):
        if (i == 0):
            print("－－－－－－－－－－")
            strChange = change16Reverse(arrTime[i], 2)
        else:
            strTem2 = intChange16(arrTime[i], 1)
            strChange = strChange + strTem2
        i = i + 1
    return strChange + "FF"


# 字符串 转换
def changestr(str2):
    length = len(str2)
    utf8_length = len(str2.encode('utf-8'))  # gbk  8.5    utf-8  9
    length = int((utf8_length - length) / 2 + length)
    str2 = binascii.b2a_hex(str2.encode("gbk"))  # encode("gbk") utf8
    str2 = str(str2)  # 将 byte 类型转换成 str 类型
    str2 = str2.replace("b'", "").replace("'", "")  # 去掉 b'
    str2 = str2.zfill(2 * length)
    return str2


# asc 转换

def changeascii(str1, aa):
    e = 0  # 暂存结果
    for i in str1:
        d = ord(i)  # 单个字符转换成ASCii码
        e = e * 256 + d  # 将单个字符转换成的ASCii码相连
    a = hex(e)
    a = a.replace("0x", "")
    a = a.zfill(2 * aa)
    # print("结果是：%s" % a)
    return a


if __name__ == "__main__":
    message_id = '0x10'
    case_id = "1"