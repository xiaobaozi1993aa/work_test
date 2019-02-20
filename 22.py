from ks_02_open_redpacket_more import *
from ks_07_agent import *
from ks_01_register import *
from ks_03_get_redpacket_uuid import *
from ks_10_add_redpacket import *
from ks_08_recharge import *
from ks_05_open_redpacket_rain import *
from ks_09_select_ksb import  *
from ks_06_traders_password import *

class Liucheng():
    mobile = 14598999999
    password = 136963.
    scope_area_list = [[0,1],[0,3],[0,5],[1,0],[2,0],[3,0],[4,0]]     #公里,区域选择
    uuid = get_uuid(mobile)
    pcode = get_pcode(uuid)
    send_message(uuid,mobile,pcode)
    mcode = get_messafe_code(mobile)
    register(mobile,mcode,password)
    token = login(mobile,password)
    headers = add_token(token)
    sql_update(uuid)
    hash_update(uuid)
    i = 0
    for scope in scope_area_list:
        i = i + 1
        print('第%d次' % i, '发随机红包', scope, add_command_redpacket(host, headers, scope).get('message'))
        i = i + 1
        print('第%d次' % i, '发口令红包', scope, add_random_redpacket(host, headers, scope).get('message'))
        i = i + 1
        print('第%d次' % i, '发幸运红包', scope, add_lucky_redpacket(host, headers, scope).get('message'))
    add_command_redpacket(host,headers,scope)
    add_random_redpacket(host,headers,scope)
    add_lucky_redpacket(host,headers,scope)
    pr_uuid = get_person_redpacket_uuid_list(headers)
    sr_uuid = get_system_redpacket_uuid_list(headers)
    for uuid in pr_uuid:
        r_uuid = uuid.get('uuid')
        ksb = open_redpacket(headers, r_uuid)
        print(ksb)
    for uuid in sr_uuid:
        r_uuid = uuid.get('uuid')
        ksb = open_redpacket(headers, r_uuid)
        print(ksb)
    select_coin(headers)




runner = Liucheng()

