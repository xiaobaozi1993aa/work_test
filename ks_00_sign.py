import time
import hashlib

salt = "*2f4961%8*5B588463bee04djDAed27"

def math_sign(**kwargs):
    api_param = dict(sorted(kwargs.items()))
    param_string = ''
    #print(api_param)
    for key, value in api_param.items():
        param_string = param_string+key+'='+str(value)+'&'
    #print(param_string + "secretValue=" + salt)
    return param_string+"secretValue="+salt

def encode_md5(str_para):
    #print(u"加密前的字符串：", str_para)
    m = hashlib.md5()
    m.update(str_para.encode("utf-8"))
    #print(u"加密值为：", m.hexdigest())
    return m.hexdigest()

def get_time():
    request_time = int(time.time())
    return request_time