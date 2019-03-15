from loger_test import TestLog
logger = TestLog().get_log()
from ks_02_open_redpacket_more import login
import requests

def get_headers(token):
    headers = {"h-api-token": token,
    "h-time": "1562446689031",
    "h-tenant-code": "gcyh",
    "h-nonce": "4a91903c-bbc6-4b9d-a976-8aabd0501c06",
    "h-system-code": "android",
    "h-version": "2.0.4",
    "h-sign": "d92e51cbd778ce9bd56b717671e760ff"
}
    print(token)
    logger.info(token)
    return headers

def get_location(headers):
    host = 'http://172.18.228.127:7005/api/v1/nest/nest_location/get_spot'
    data = {"latitude":"23.627672508077943","longitude":"113.82137686014175"}
    r = requests.get(url=host, params=data, headers=headers).json()
    logger.info(r.get('response'))
    return r.get('response')

def buy_beehome(headers,number,latitude,longitude):
    host = 'http://172.18.228.127:7005/api/v1/nest/timeInfo/buyNestTime'
    #for i in range(1,21):
    data = {"price": 20, "channelCode": "ios", "nestLocationId": number,
            "payType": "10001","days":5,"startDate":"2019-03-19",
            "safetyCode": "123456", "payLatitude": "113.822985",
            "payLongitude": "22.630174","nestLatitude":latitude,"nestLongitude":longitude}
    r = requests.post(url = host,headers = headers,data = data).json()
    logger.info(data)
    logger.info('接口返回:{} 广告位:{} 经度:{} 纬度:{}'.format(r,data.get("nestLocationId"),
                                                    data.get("nestLatitude"),data.get("nestLongitude")))



if __name__ == '__main__':
    token = login(19930808119,123456)
    headers = get_headers(token)
    r = get_location(headers)
    for i in range(len(r)):
        latitude = r[i].get('latitude')
        longitude = r[i].get('longitude')
        number = r[i].get('nestLocationId')
        buy_beehome(headers,number,latitude,longitude)
    # latitude = 24.81696440254334
    # longitude = 113.60359758138657
    # number = 180708462
    # buy_beehome(headers, number, latitude, longitude)


