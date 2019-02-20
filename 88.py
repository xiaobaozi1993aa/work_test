'''
@1.所有代理关系打印写入

'''

import pymysql
from ks_77 import get_upper
import sys

import time
import progressbar          #显示进度条
p = progressbar.ProgressBar()
N = 1000
for i in p(range(N)):
    time.sleep(0.01)

db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_user')
cursor = db.cursor()
output = sys.stdout
type = sys.getfilesystemencoding()   #中文写入调整乱码

def get_all_uuid():
    cursor.execute('select user_account_uuid from agent')
    uuid_list = cursor.fetchall()
    return uuid_list

if __name__ == '__main__':
    uuid_list = get_all_uuid()
    for i in uuid_list:
        get_upper(i,n=-1)
        f = open('agent.txt','a')
        sys.stdout = f