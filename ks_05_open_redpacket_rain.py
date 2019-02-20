from ks_02_open_redpacket_more import *

host = 'http://test_gateway.guochuangyuanhe.com/'
#获取红包雨列表
def get_rain_list(headers):
    path = 'api/v1/redpacket/red_packet_rain/get_list'
    api = ''.join([host,path])
    data = {"currentPage":1,"pageSize":10}
    r = requests.get(url=api, params=data, headers=headers).json()
    return r.get('response')

#打开红包雨
def open_red_rain(headers,rain_uuid,number):
    path = 'api/v1/redpacket/red_packet_rain/draw'
    api = ''.join([host, path])
    data = {"redPacketRainUuid": rain_uuid, "quantity": number}
    print(data)
    r = requests.post(url=api, data=data,headers=headers).json()
    print(r)

if __name__ == '__main__':
    mobile = 13066909086
    password = 123456
    number = 490
    token = login(mobile, password)
    print(token)
    headers = add_token(token)
    rlist = get_rain_list(headers).get('dataList')
    for i in rlist:
        rain_uuid = i.get('redPacketRainUuid')
        open_red_rain(headers,rain_uuid,number)