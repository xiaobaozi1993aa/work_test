import requests
from config_kshb import TestLog

class Ks_Login():
    def __init__(self):
        self.host = 'http://test_gateway.guochuangyuanhe.com/'
        self.logger = TestLog().getlog()
    def login(self,mobile, password):
        path = 'api/v1/user/account/login'
        api = ''.join([self.host, path])
        data = {"username": mobile, "password": password, "systemCode": 1, "loginType": 2}
        r = requests.post(url=api, data=data).json()
        token = r.get('response')
        if token != None:
            # logger.info('账号:{} 接口返回:{}'.format(mobile,r))
            self.logger.info('账号:%s,%s', mobile, r)
            return token
        else:
            self.logger.error('账号:{} 密码:{} 错误返回:{}'.format(mobile, password, r.get('message')))

a = Ks_Login()

for i in range(10):
    a.login(19931999000,123456)
