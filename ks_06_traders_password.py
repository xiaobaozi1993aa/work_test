'''
@1.批量绑定交易密码
@2.主要变量为注册的号码

'''

import requests
import redis
import pymysql
from ks_01_register import *
from ks_02_open_redpacket_more import *

url = 'http://test_gateway.guochuangyuanhe.com/'

#获取uuid
def get_uuid(mobile,headers):
    path = 'api/v1/file/captcha/reset_safe_code'
    data = {"mobile": "%s" % mobile}
    api = ''.join([url, path])
    r = requests.post(url=api, data=data,headers=headers).json()
    uuid = (r.get('response')).get('uuid')
    #print(uuid)
    return uuid

#获取图形验证码
def get_pcode(uuid):
    value = "file:CaptchaServiceImpl:mobileCaptcha[%s]" % uuid  #
    pool = redis.ConnectionPool(host='172.18.228.112', port=6379, password='2018375tghfsbn8',db=10)
    r = redis.Redis(connection_pool=pool)
    p_code = r.get(value).decode('utf8')
    return p_code

#发送短信验证码
def send_message(uuid, mobile, pcode,headers):
    path = 'api/v1/user/sms/reset_safety_code'
    api = ''.join([url, path])
    data = {"mobile": mobile, "captcha": pcode, "uuid": uuid}
    message_code = requests.post(url=api, data=data,headers=headers)
    return message_code

#获取手机验证码
def get_messafe_code(mobile):
    db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_sms')
    cursor = db.cursor()
    cursor.execute('select content from send where mobile = "%s" order by id desc limit 1' % mobile)
    data = cursor.fetchone()
    mcode = str(data)[22:28]
    print(mcode)
    return mcode

#绑定交易密码
def traders_password(mobile,headers,mcode):
    path = '/api/v1/user/safe/reset'
    data = {'captcha': mcode, 'safetyCode': 199308}
    api = ''.join([url, path])
    r = requests.post(url=api, data=data,headers=headers).json()
    #print(data)
    #print(headers)
    print(mobile,'绑定交易密码',r)

if __name__ == '__main__':
    password = 123456
    phone = (a for a in range(19911998000,19911998005))
    #phone = ['19931996020']
    for mobile in phone:
        token = login(mobile, password)
        #print(token)
        headers = add_token(token)
        uuid = get_uuid(mobile,headers)
        pcode = get_pcode(uuid)
        send_message(uuid,mobile,pcode,headers)
        mcode = get_messafe_code(mobile)
        #print(mcode)
        traders_password(mobile,headers,mcode)
