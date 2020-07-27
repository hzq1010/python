# -*-coding:utf-8-*-

# coding=utf8
import mysql.connector
import common
import logging
import datetime
import pymysql


def parseadd(case):
    config = {
        'host': '127.0.0.1',  # 连接的IP地址
        'user': 'root',
        'password': '123456',
        'port': 3306,
        'database': 'monitor',
        'charset': 'utf8',  # 编码格式,防止查出来的数据中文乱码
    }
    #db1_cursor = mysql.connector.Connect(**config)  # 连接数据库
    db1_cursor = pymysql.Connect(**config)

    cur = db1_cursor.cursor()  # 执行命令，接收结果
    t_str = "select * from monitor.test_manholecover_state_copy where case_id="
    try:
        cur.execute(t_str + str(case))
        t_result = cur.fetchone()
        print(t_result)
        db1_cursor.close()
        print("-----------------------井盖监控点编码", t_result[5])
        strElement0 = common.reverseStart_field()  # 头
        strElement1 = common.reverseNumber_field()  # 序列
        strElement2 = common.intChange16(t_result[4], 1)  # 应答标志
        # strElement3=common.changeascii(t_result[5],12)#设备编码
        strElement3 = common.changeascii(t_result[5], 12)  # 设备编码
        logging.info("报文发送时间：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " 编码：" + t_result[5])
        strElement4 = common.intChange16(t_result[6], 1)  # 井盖状态
        strElement5 = common.intChange16(t_result[7], 1)  # 正在操作方式
        strElement6 = common.intChange16(t_result[8], 3)  # 告警状态
        strElement6_1 = common.intChange16(t_result[9], 3) # 告警状态
        strElement7 = common.intChange16(t_result[10], 1)  # 控制授权
        strElement8 = common.intChange16(t_result[11], 1)  # 角度状态
        strElement9 = common.zfill(t_result[12], 4)  # 结束标记

        # 拼接字符串
        strElement = [strElement0, strElement1, strElement2, strElement3, strElement4, strElement5, strElement6,
                      strElement6_1, strElement7, strElement8, strElement9]
        strResult = ''.join(strElement)

        # print("=====================")
        print("拼接报文:", strResult)
        return strResult

    except Exception as e:
        print("Error: %s" % e)


if __name__ == "__main__":

    for id in range(1, 68):
        print(parseadd(1))

        # db1_cursor = mysql.connector.connect(host='127.0.0.1', port='3306', user='root', password='123456', database='monitor', charset='utf8')
        # cur = db1_cursor.cursor()
        # case_id='1'
        # #parseadd(case_id)
        # db1_cursor.close()