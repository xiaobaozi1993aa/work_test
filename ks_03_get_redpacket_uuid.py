'''
@1.获取个人红包uuid
@2.获取系统红包uuid

'''

from  ks_02_open_redpacket_more import login,add_token
import requests
host = 'http://test_gateway.guochuangyuanhe.com/'
#http://test_gateway.guochuangyuanhe.com/
#https://api.guochuangyuanhe.com/
#获取个人红包uuid
def get_person_redpacket_uuid_list(headers):
    path = 'api/v1/redpacket/red_packet_pool/get_location'
    data = {"latitude":22.630398,"longitude":113.823169}
    api = ''.join([host,path])
    r = requests.get(url=api,params=data,headers=headers).json()
    uuid = r.get('response')
    return uuid

#获取系统红包uuid
def get_system_redpacket_uuid_list(headers):
    path = 'api/v1/redpacket/red_packet_pool/get'
    data = {"latitude":22.630398,"longitude":113.823169}
    api = ''.join([host,path])
    r = requests.get(url=api,params=data,headers=headers).json()
    uuid = r.get('response')
    return uuid

if __name__ == '__main__':
    mobile = 13066909086
    password = 123456
    token = login(mobile,password)
    headers = add_token(token)
    get_person_redpacket_uuid_list(headers)
    a=get_system_redpacket_uuid_list(headers)
    for i in a:
        print(i)