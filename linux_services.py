'''
@1.夺宝号
'''

import paramiko
import re

services_list = ['172.18.228.126','172.18.228.127']
port_list = [['7155','activity'],['7140','hbase'],
              ['7130','boss'],
              ['7100','file'],['7005','getway'],
              ['7115','information'],['7145','job'],['7165','nest'],
              ['7125','order'],['7135','redpacket'],['7175','redpacket_consumer'],
              ['7150','redpacket_job'],['7105','sms'],['7180','user_redpacket_consumer'],
              ['7095','user'],['7170','user_consumer'],['7160','user_role']]

for services in services_list:
    for port in port_list:
        host = ''.join(['http://',services,':',port[0]])        #字符串拼接
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('172.18.228.126', 22, username='root', password='qazwwssxedc-!@#$%123453edw', timeout=20)
        stadin,stdout,stderr = client.exec_command('wget %s' % host)
        result = stdout.read().decode()
        err = str(stderr.read())
        client.close()
        d = re.search(r'\b404', err)
        if len(err)>195:
            if d != None:
                print('success')
            else:
                print('%s ,%s , %s ,失败' % (services, port[0], port[1]))
                exit(1)
        else:
            print('%s ,%s , %s ,失败' %(services,port[0],port[1]))
            exit(1)



