from ks_07_agent import *
from ks_02_open_redpacket_more import *

phone = (a for a in range(19931997000,19931997100))

for aa in phone:
    password = 123456
    mobile = str(aa)
    token = login(mobile, password)
    headers = add_token(token)
    uuid = get_user_uuid(mobile)
    print('绑定关系', mobile, binding_relationship(uuid,headers))
