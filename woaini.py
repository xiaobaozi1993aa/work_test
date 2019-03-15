from ks_02_open_redpacket_more import login,http_request
from loger_test import TestLog
logger = TestLog().get_log()


def get_location(token):
    host = 'http://172.18.228.127:7005/api/v1/nest/nest_location/get_spot'
    data = {"latitude":"22.630396","longitude":"113.823172"}
    r = http_request(api=host, method='get', token=token, **data)
    #print(r)
    logger.info(r.get('response'))
    return r.get('response')


def buy_beehome(number,latitude,longitude,token):
    host = 'http://172.18.228.127:7005/api/v1/nest/timeInfo/buyNestTime'
    data = {"price": 20, "channelCode": "ios", "nestLocationId": number,
            "payType": "10001","days":5,"startDate":"2019-03-15",
            "safetyCode": "123456", "payLatitude": "113.822985",
            "payLongitude": "22.630174","nestLatitude":latitude,"nestLongitude":longitude}
    r = http_request(api=host, method='post', token=token, **data)
    logger.info(data)
    logger.info('接口返回:{} 广告位:{} 经度:{} 纬度:{}'.format(r,data.get("nestLocationId"),
                                                    data.get("nestLatitude"),data.get("nestLongitude")))

if __name__ == '__main__':
    token = login(19930808119, 123456)
    r = get_location(token)
    for i in range(len(r)):
        latitude = r[i].get('latitude')
        longitude = r[i].get('longitude')
        number = r[i].get('nestLocationId')
        buy_beehome(number, latitude, longitude,token)