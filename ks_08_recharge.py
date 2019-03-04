'''
@1.更改用户mysql金额
@2.更改用户redis金额

'''

from ks_07_agent import get_user_uuid
import redis
import pymysql

#更改mysql
def sql_update(uuid):
    db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_user')
    cursor = db.cursor()
    cursor.execute("update user_wallet set coin = 10000 where user_account_uuid = '%s'"% uuid)
    db.commit()
    cursor.close()

#更改Redis
def hash_update(uuid):
    pool = redis.ConnectionPool(host='172.18.228.112', port=6379, password='2018375tghfsbn8',db=10)
    r = redis.Redis(connection_pool=pool)
    b = r.hset(name='user:UserWalletServiceImpl:userCoin',key='%s' %uuid,value=1000000000)
    print(b)
    a = r.hset(name = 'user-consumer:TenantWalletServiceImpl:accountInfo',key = 'market_Out',value=0)
    print(a)    #公司出
    c = r.hset(name = 'user-consumer:TenantWalletServiceImpl:accountInfo',key = 'bonus_In',value=0)
    print(c)    #增值池
    d = r.hset(name = 'user-consumer:TenantWalletServiceImpl:accountInfo',key = 'market_In',value=0)
    print(d)    #公司出
if __name__ == '__main__':
    phone = (a for a in range(19931992020,19931992099))
    #phone = ['17620340622']
    #phone = ['19931996000', '19931995090', '19931995091', '19931993002','19931993013']

    for mobile in phone:
        uuid = get_user_uuid(mobile)
        sql_update(uuid)
        hash_update(uuid)
