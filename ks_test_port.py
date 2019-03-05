from config_kshb import TestLog
import requests


host = 'http://test_gateway.guochuangyuanhe.com/'

logger = TestLog().getlog()
#登录获取token
def login(mobile, password):
    path = 'api/v1/user/account/login'
    api = ''.join([host, path])
    data = {"username": mobile, "password": password, "systemCode": 1, "loginType": 2}
    r = requests.post(url=api, data=data).json()
    token = r.get('response')
    if token != None:
        #logger.info('账号:{} 接口返回:{}'.format(mobile,r))
        logger.info('账号:%s,%s',mobile,r)
        return token
    else:
        logger.error('账号:{} 密码:{} 错误返回:{}'.format(mobile,password,r.get('message')))

if __name__ == '__main__':

    logger.info('================Start================')
    for mobile in range(19931993000,19931999001):
        login(mobile,123456)