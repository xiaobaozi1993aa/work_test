'''
@1.夺宝号去重排序统计

'''

from ks_02_open_redpacket_more import *
import requests

host = 'http://172.18.228.126:7005/'


def select_number(token, api):
    data = {"snatchId": "3"}
    r = http_request(api=api, method='post', token=token, **data)
    number = r.get('response')
    a = list(eval(number))              #字符串转列表
    return a

if __name__ == '__main__':
    path = 'api/v1/activity/snatchRecord/querySnatchNums'
    api = ''.join([host, path])
    phone = (a for a in range(19931997000, 19931997050))
    password = 123456
    number_list = []
    for mobile in phone:
        token = login(mobile, password)
        number_list.extend(select_number(token, api))      #列表添加列表
    number_list.sort()                                  #列表排序
    abcd = list(set(number_list))                       #列表去重
    print(len(abcd))                                    #列表统计个数
    print(number_list)


