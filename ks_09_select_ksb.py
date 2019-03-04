'''
@1.查询金额

'''



from ks_02_open_redpacket_more import *

host = 'http://test_gateway.guochuangyuanhe.com/'
#查询KSB余额
def select_coin(headers):
    path = 'api/v1/user/wallet/coin'
    api = ''.join([host,path])
    r = requests.get(url=api, headers=headers).json()
    return r



if __name__ == '__main__':
    phone = ['17620340622']
    #phone = (a for a in range(19931993000))
    password = 123456
    for mobile in phone:
        token = login(mobile,password)
        print(token)
        headers = add_token(token)
        coin = select_coin(headers)
        if mobile == '19931993002':
            print('总监',mobile,'ksb:',coin.get('response'))
        elif mobile == '19931993006':
            print('总监',mobile,'ksb:',coin.get('response'))
        elif mobile == '19931993048':
            print('经理',mobile,'ksb:',coin.get('response'))
        elif mobile == '19931993062':
            print('总监',mobile,'ksb:',coin.get('response'))
        elif mobile == '19931993068':
            print('经理',mobile,'ksb:',coin.get('response'))
        else:print('代理',mobile,'ksb:',coin.get('response'))