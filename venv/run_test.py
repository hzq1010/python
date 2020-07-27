# coding=utf-8
import datetime
import logging
import threading
from socket import *
from time import sleep
import manholecover_state

# import logging.handlers

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='test.log',
                    filemode='w')
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
socks = []


def singlesend(case, soc2):
    global lock
    lock.acquire()
    # case_id = 1
    # while case_id<=2:   #循环次数
    print("报文发送时间：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-----------------------井盖监控点编码", case)  # , "上报次数:", case_id)
    send_manholecover_state = manholecover_state.parseadd(case)
    #print("----------------------", send_manholecover_state + '\n')

    soc2.send(bytes().fromhex(send_manholecover_state))

    # case_id = case_id + 1
    # print("报文发送时间：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # sleep(1) #可修改的上报时间间隔
    lock.release()


def message():
    global lock
    lock.acquire()
    t_code = 201820190601
    threads = []
    # while (t_code <= 201820190667):
    for case in range(1, 68):
        t_singlesend = threading.Thread(target=singlesend, args=(str(case), socks[case-1]))
        threads.append(t_singlesend)
        # t_singlesend.setDaemon(True)
        # t_singlesend.start()
        # sleep(1)
        t_code += 1

    for i in threads:
        i.setDaemon(True)
        i.start()
    lock.release()


if __name__ == '__main__':
    lock = threading.Lock()

    end = datetime.datetime.now() + datetime.timedelta(days=2)  # 获取结束时间
    print("报文发送一周结束时间" + end.strftime("%Y-%m-%d %H:%M:%S") + '\n')
    for case in range(1, 68):
        soc = socket(AF_INET, SOCK_STREAM)
        soc.settimeout(300)  # 设置超时时间
        soc.connect(('192.168.0.156', 8845))
        socks.append(soc)

    while True:
        message()
        now = datetime.datetime.now()
        sleep(1)
        if now >= end:
            break

'''
threads = []
threads.append(t_singlesend)
for t in threads:
    t.start()
for t in threads:
    t.join(）
    logging.info("全部执行完成~：%s" % ctime())
 '''