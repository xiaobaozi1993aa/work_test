'''
@1.计算个人红包总额
@2.主要变量为抢红包人数和红包uuid

'''
import requests

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
    #print(data)
    #print(r)
    token = r.get('response','未获取token')
    return token

#请求头
def add_token(token):
    headers = {
        "Accept": "*/*",
        "h-api-token": token,
        "h-admin-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbl91dWlkIiwiaC10ZW5hbnQtY29kZSI6ImdjeWgiLCJsb2dpbklkIjoiYWRtaW5fdXVpZCIsImV4cCI6MTU2MjE1MDI1MCwiaWF0IjoxNTQ0ODcwMjQ2NTMxfQ.kMySAJzhzB-lFkhliSh2S1nYGQMaug2JIPs2ugShZU1wTTcV4n4Edb2pOHgvaRGMSe4Gj6S82BggkVYobu-j1g",
        "h-time": "1565554375874",
        "h-tenant-code": "gcyh",
        "h-nonce": "b9970e650c5147c3a964f9e8f39b7920"
    }
    return headers

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
