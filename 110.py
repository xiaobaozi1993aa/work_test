






from ks_02_open_redpacket_more import *
import requests
host = 'http://test_gateway.guochuangyuanhe.com/'

def buy_bee(headers,number):
        path = 'api/v1/nest/timeInfo/buyNestTime'
        data = {"price":number,"channelCode":"ios","nestTimeInfoId":"7","payType":"10001",
                "safetyCode":"123456","longitude":"113.8180160522","latitude":"22.6241917710"}
        api = ''.join([host,path])
        r = requests.post(url = api,data = data,headers = headers).json()
        print(data)
        print(r,key,number)

if __name__ == '__main__':
    phone = (a for a in range(19931997000, 19931997005))
    number1 = (b for b in range(1, 6))
    dict2 = []
    dict1 = []
    for i in phone:
        dict2.append(i)
    for ii in number1:
        dict1.append(ii)
    a = dict(zip(dict2, dict1))
    password = 123456
    for key, values in a.items():
        token = login(key, password)
        headers = add_token(token)
        buy_bee(headers,values)