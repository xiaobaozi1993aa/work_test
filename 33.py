from ks_02_open_redpacket_more import *
from ks_09_select_ksb import select_coin
import redis

pool = redis.ConnectionPool(host='172.18.228.112', port=6379, password='2018375tghfsbn8', db=10)
r = redis.Redis(connection_pool=pool)
b = r.hget(name = 'user-consumer:TenantWalletServiceImpl:accountInfo',key = 'market_Out')
print('公司出:',int(b))
b = r.hget(name = 'user-consumer:TenantWalletServiceImpl:accountInfo',key = 'market_In')
print('公司进:',b)
b = r.hget(name = 'user-consumer:TenantWalletServiceImpl:accountInfo',key = 'bonus_In')
print('增值池:',b)
phone = ['19931996000','19931995090','19931995091','19931993002','19931993013']
password = 123456
for mobile in phone:
    token = login(mobile,password)
    #print(token)
    headers = add_token(token)
    coin = select_coin(headers)
    if mobile == '19931996000':
        print('省代', mobile, 'ksb:', coin.get('response'))
    elif mobile == '19931995091':
        print('城主', mobile, 'ksb:', coin.get('response'))
    elif mobile == '19931995090':
        print('市代', mobile, 'ksb:', coin.get('response'))
    elif mobile == '19931993002':
        print('上级', mobile, 'ksb:', coin.get('response'))
    else:print('乌拉', mobile, 'ksb:', coin.get('response'))

#19931993013