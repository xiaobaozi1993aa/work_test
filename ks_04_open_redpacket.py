'''
@1.快速领取个人红包，清空红包界面
@2.主要变量为手机号

'''


from ks_03_get_redpacket_uuid import *
from ks_02_open_redpacket_more import *


#开红包
mobile = 19931993002
password = 199308
token = login(mobile,password)
headers = add_token(token)
sr_uuid = get_system_redpacket_uuid_list(headers)
pr_uuid = get_person_redpacket_uuid_list(headers)
print(pr_uuid)
print(sr_uuid)
for uuid in pr_uuid:
    r_uuid = uuid.get('uuid')
    ksb = open_redpacket(headers,r_uuid)
    print(ksb)
for uuid in sr_uuid:
    r_uuid = uuid.get('uuid')
    ksb = open_redpacket(headers, r_uuid)
    print(ksb)