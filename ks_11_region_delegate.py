'''
@1.抢城主

'''

from ks_02_open_redpacket_more import *
import requests

host = 'http://test_gateway.guochuangyuanhe.com/'

def add_region_delegate(headers,rid,safe_pd):
    path = 'api/v1/user/region_delegate/add'
    api = ''.join([host,path])
    data = {"channelCode":"ios","money":4000.00,"payType":10001,"regionId":rid,"safetyCode":safe_pd}
    r = requests.post(url=api,data=data,headers=headers).json()
    print(r)

if __name__ == '__main__':
    #phone = ['19931996000', '19931995090', '19931995091', '19931993002']
    phone = ['19931993000']
    for mobile in phone:
        password = 123456
        rid = 2115
        safe_pd = 199308
        token = login(mobile, password)
        headers = add_token(token)
        for i in range(4):
            add_region_delegate(headers,rid,safe_pd)