'''
@1.发红包

'''


from ks_02_open_redpacket_more import *


def add_random_redpacket(host,headers,scope):
    path = 'api/v1/redpacket/person_red_packet/add_random'
    api = ''.join([host, path])
    data = {"userLatitude":22.630182,"userLongitude":113.822965,"redPacketLatitude":22.630182,"redPacketLongitude":113.822965,
            "content":"爱你","areaType":scope[0],"kilometer":scope[1],"money":1.0,"quantity":1,"payType":10001,"channelCode":"android",
            "safetyCode":199308}
    r = requests.post(url=api, data=data,headers=headers).json()
    return r


def add_command_redpacket(host,headers,scope):
    path = 'api/v1/redpacket/person_red_packet/add_password'
    api = ''.join([host, path])
    data = {"userLatitude": 22.630182, "userLongitude": 113.822965, "redPacketLatitude": 22.630182,
            "redPacketLongitude": 113.822965,"password":"1234","isPublicPassword":1,
            "content": "爱你", "areaType": scope[0], "kilometer": scope[1], "money": 1.0, "quantity": 1, "payType": 10001,
            "channelCode": "android",
            "safetyCode": 199308}
    r = requests.post(url=api, data=data, headers=headers).json()
    return r


def add_lucky_redpacket(host,headers,scope):
    path = 'api/v1/redpacket/person_red_packet/add_lucky'
    api = ''.join([host, path])
    data = {"userLatitude": 22.630182, "userLongitude": 113.822965, "redPacketLatitude": 22.630182,
            "redPacketLongitude": 113.822965,"isPublicPassword": 0,
            "content": "爱你", "areaType": scope[0], "kilometer": scope[1], "money": 10.0, "quantity": 100, "payType": 10001,
            "channelCode": "android",
            "safetyCode": 199308}
    r = requests.post(url=api, data=data, headers=headers).json()
    return r


if __name__ == '__main__':
    host = 'https://test_gateway.guochuangyuanhe.com/'
    mobile = 19930808001
    password = 123456
    scope_area_list = [[0,1],[0,3],[0,5],[1,0],[2,0],[3,0],[4,0]]     #公里,区域选择
    token = login(mobile,password)
    headers = add_token(token)
    i = 0
    for scope in scope_area_list:
        i = i + 1
        print('第%d次' % i,'发随机红包',scope,add_command_redpacket(host,headers,scope).get('message'))
        i = i + 1
        print('第%d次' % i,'发口令红包',scope,add_random_redpacket(host,headers,scope).get('message'))
        i = i + 1
        print('第%d次' % i,'发幸运红包',scope,add_lucky_redpacket(host,headers,scope).get('message'))


