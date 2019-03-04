'''
@1.数据库查询获取用户uuid
@2.绑定代理关系
@3.升级代理

'''

from ks_02_open_redpacket_more import *
import pymysql

host = 'http://test_gateway.guochuangyuanhe.com/'
#host = 'https://api.guochuangyuanhe.com/'
#获取用户uuid
def get_user_uuid(mobile):
    db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_user')
    cursor = db.cursor()
    cursor.execute('select user_account_uuid from user_info where mobile = %s' % mobile)
    uuid = cursor.fetchone()
    return uuid

#绑定代理关系
def binding_relationship(uuid,headers):
    path = 'api/v1/user/admin/invite/add_inviter'
    data = {'userAccountUuid':uuid,'inviteCode':19931993013}
    api = ''.join([host, path])
    r = requests.post(url=api, data=data,headers=headers).json()
    print(data)
    return r

#升级代理
def upgrade(headers):
    path = '/api/v1/user/agent/upgrade_agent'
    data = {'channelCode': 'ios', 'payType': '10001', 'originalMoney': 499,'safetyCode':199308}
    api = ''.join([host, path])
    r = requests.post(url=api, data=data, headers=headers).json()
    print(r)
    return r

if __name__ == '__main__':
    password = 123456
    phone = (a for a in range(19911998000,19911998005))
    #phone = ['13066909086']
    for aa in phone:
        mobile = str(aa)
        token = login(mobile, password)
        headers = add_token(token)
        uuid = get_user_uuid(mobile)
        print('绑定关系',mobile,binding_relationship(uuid,headers))
        print('升级代理',mobile,upgrade(headers))

