'''
@1.注册，登录一条龙
@2.主要变量为注册的号码

'''
import requests
import redis
import pymysql
url = 'http://test_gateway.guochuangyuanhe.com/'

#获取uuid
def get_uuid(mobile):
    path = 'api/v1/file/captcha/register'
    data = {"mobile": "%s" % mobile}
    api = ''.join([url, path])
    r = requests.post(url=api, data=data).json()
    uuid = (r.get('response')).get('uuid')
    return uuid

#获取图形验证码
def get_pcode(uuid):
    value = "file:CaptchaServiceImpl:mobileCaptcha[%s]" % uuid  #
    pool = redis.ConnectionPool(host='172.18.228.112', port=6379, password='2018375tghfsbn8',db=10)
    r = redis.Redis(connection_pool=pool)
    p_code = r.get(value).decode('utf8')
    return p_code

#发送短信验证码
def send_message(uuid, mobile, pcode):
    path = 'api/v1/user/sms/register'
    api = ''.join([url, path])
    data = {"mobile": mobile, "captcha": pcode, "uuid": uuid}
    message_code = requests.post(url=api, data=data)
    return message_code

#获取手机验证码
def get_messafe_code(mobile):
    db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_sms')
    cursor = db.cursor()
    cursor.execute('select content from send where mobile = "%s" order by id desc limit 1' % mobile)
    data = cursor.fetchone()
    mcode = str(data)[18:24]
    return mcode

#注册
def register(mobile, mcode, password):
    path = 'api/v1/user/register/mobile'
    api = ''.join([url, path])
    data = {"tenantCode": "gcyh", "mobile": mobile, "captcha": mcode, "password": password,
             "registerSource": "1"}
    r = requests.post(url=api, data=data).json()
    return r

#登录
def login(mobile, password):
    path = 'api/v1/user/account/login'
    api = ''.join([url, path])
    data = {"username": mobile, "password": password, "systemCode": 1, "loginType": 1}
    r = requests.post(url=api, data=data).json()
    #print(r)
    return r.get('response')


if __name__ == '__main__':
    password = 123456
    phone = (a for a in range(19931998000,19931998100))
    #phone= ['18823303216']
    for mobile in phone:
        get_uuid(mobile)
        uuid = get_uuid(mobile)
        get_pcode(uuid)
        pcode = get_pcode(uuid)
        send_message(uuid,mobile,pcode)
        mcode = get_messafe_code(mobile)
        register(mobile,mcode,password)
        a = login(mobile,password)
        print(a)