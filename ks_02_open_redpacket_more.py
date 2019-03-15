'''
@1.计算个人红包总额
@2.主要变量为抢红包人数和红包uuid

'''
import requests
from ks_00_sign import *
import random
from loger_test import TestLog
logger = TestLog().get_log()

host = 'http://test_gateway.guochuangyuanhe.com/'
#host = 'https://api.guochuangyuanhe.com/'
#http://test_gateway.guochuangyuanhe.com/
#https://api.guochuangyuanhe.com/

#登录获取token
def login(mobile, password):
    path = 'api/v1/user/account/login'
    api = ''.join([host, path])
    data = {"username": mobile, "password": password, "systemCode": 1, "loginType": 2}
    r = requests.post(url=api, data=data).json()
    token = r.get('response','未获取token')
    logger.info('账号: {} 密码: {}'.format(mobile,password))
    return token

#请求方式
def http_request(api, method, token,**kwargs):
    h_nonce = random.randint(1, 10000) + get_time()
    headers = {
        "h-time": str(get_time() * 1000),
        "h-nonce": str(h_nonce),
        "h-tenant-code": 'gcyh',
        "h-system-code": 'ios'
    }
    params = dict(headers, **kwargs)
    headers["h-sign"] = encode_md5(math_sign(**params))
    headers['h-api-token']=token
    #print(headers)
    if method.lower()=='get':
        response = requests.get(url=api, data=params, headers=headers).json()
        logger.info(params)
        logger.info(headers)

    if method.lower()=='post':
        response = requests.post(url=api, data=params, headers=headers).json()
        logger.info(params)
    return response

#开红包
def open_redpacket(headers,r_uuid):
    path = 'api/v1/redpacket/red_packet_pool/open'
    api = ''.join([host, path])
    data = {"latitude": 22.630186, "longitude": 113.822961, "redPacketUuid":r_uuid ,"password":"0728"}
    #print(data)
    r = requests.post(url=api,data=data,headers=headers).json()
    return r

#483.8997
if __name__ == '__main__':
    r_uuid = "109b8cd7203846078797aaf1d54c320f"
    password = 123456
    #phone = (a for a in range(19930808100,19930808200))
    #phone = ['13066909086']
    phone = (a for a in range(19931996015, 19931996020))
    sum = 0
    for mobile in phone:
        token = login(mobile,password)
        print(token)
        headers = add_token(token)
        KSB = open_redpacket(headers,r_uuid)
        #print(KSB)
        coin = KSB.get('response').get('coin')
        coin = float(coin)
        sum += coin
        print(mobile,'抢了:',coin,'ksb','\n',
              '当前红包总额为:',sum)
