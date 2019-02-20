import requests
from ks_02_open_redpacket_more import *

class Ceshi:
    def __init__(self):
        self.host = 'http://test_gateway.guochuangyuanhe.com/'
        self.path = 'api/v1/user/wallet/coin'
        self.api = ''.join([self.host,self.path])
        self.headers = add_token(login(19931993002,199308))
        self.data = {}
        self.post = requests.post(url=self.api,data=self.data,headers=self.headers).json()
        self.get = requests.get(url=self.api,params=self.data,headers=self.headers).json()
    def ks1(self):
        print(self.get)


a = Ceshi()
a.ks1()