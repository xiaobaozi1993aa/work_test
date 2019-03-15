from ks_02_open_redpacket_more import login,http_request
from loger_test import TestLog
logger = TestLog().get_log()
import threading
import time
def buy_beehome(token):
    host = 'http://172.18.228.127:7005/api/v1/nest/timeInfo/buyNestTime'
    data = {"price": 20, "channelCode": "ios", "nestLocationId": 320259875,
            "payType": "10001","days":5,"startDate":"2019-03-15",
            "safetyCode": "123456", "payLatitude": "113.822985",
            "payLongitude": "22.630174","nestLatitude":"109.68674629926681519","nestLongitude":"20.66255135294448309"}
    for i in range(3):
        r = http_request(api=host, method='post', token=token, **data)
        logger.info(r)


if __name__ == '__main__':      #单个接口多线程压测
    try:
        token = login(19930808119, 123456)
        i = 0
        tasks_number = 1
        logger.info('=========Test Start=========')
        time1 = time.clock()
        while i < tasks_number:
            t = threading.Thread(target=buy_beehome(token))
            t.start()
            i += 1
        time2 = time.clock()
        times = time2 - time1
        logger.info('=========Test End=========')
        logger.info('共耗时: {}'.format(times))
        logger.info('平均耗时: {}'.format(times / tasks_number))
    except Exception as e:
        logger.error(e)
