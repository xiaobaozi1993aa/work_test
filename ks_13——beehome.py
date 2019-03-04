from ks_02_open_redpacket_more import *
from ks_09_select_ksb import select_coin
import requests

host = 'http://test_gateway.guochuangyuanhe.com'

def buy_bee(number, token, api):
        data = {"price":number,"channelCode":"ios","nestTimeInfoId":"9","payType":"10001",
                "safetyCode":"123456","longitude":"113.021121","latitude":"25.776524"}
        r = http_request(api=api,method='post',token = token, **data)
        print(r,mobile,number)


if __name__ == '__main__':
    path = 'api/v1/nest/timeInfo/buyNestTime'
    api = ''.join([host, path])
    #phone = (a for a in range(19931997001, 19931997021))
    #number1 = (b for b in range(1,6))
    #dict = [[19931997001,1],[19931997002,2],[19931997003,3],[19931997004,4]]
    phone = ['19931993000']
    number = 19
    for mobile in phone:
        while number < 20:
            number = number + 1
            password = 123456
            token = login(mobile, password)
            buy_bee(number,token,api)
            #coin = select_coin(headers)
            #print(headers)
