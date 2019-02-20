import pymysql

db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_user')
cursor = db.cursor()
aaaa = ('0',)

def select_user_01(uuid):
    cursor.execute("select inviter_account_uuid from user_invite where user_account_uuid = '%s'"  % uuid)
    a = cursor.fetchone()
    cursor.execute("select role from user_invite where user_account_uuid = '%s'" % a)
    ar = cursor.fetchone()
    ar = int(ar[0])
    if ar != 0:
        ar = str('代理')
    if a != aaaa:
        print(uuid,'我的上级',a[0],ar)
    else:
        print('没有上级')
    return a

def select_user_02(a):
    cursor.execute("select inviter_account_uuid from user_invite where user_account_uuid = '%s'" % a)
    b = cursor.fetchone()
    cursor.execute("select role from user_invite where user_account_uuid = '%s'" % b)
    br = cursor.fetchone()
    br = int(br[0])
    if br != 0:
        br = str('代理')
    if b != aaaa:
        print(a[0],'我的上级',b[0],br)
    else:
        print('没有上级')
    return b

def select_user_03(b):
    cursor.execute("select inviter_account_uuid from user_invite where user_account_uuid = '%s'" % b)
    c = cursor.fetchone()
    cursor.execute("select role from user_invite where user_account_uuid = '%s'" % c)
    cr = cursor.fetchone()
    cr = int(cr[0])
    if cr != 0:
        cr = str('代理')
    if c != aaaa:
        print(b[0], '我的上级', c[0],cr)
    else:
        print('没有上级')
    return c

def select_user_04(c):
    cursor.execute("select inviter_account_uuid from user_invite where user_account_uuid = '%s'" % c)
    d = cursor.fetchone()
    cursor.execute("select role from user_invite where user_account_uuid = '%s'" % d)
    dr = cursor.fetchone()
    dr = int(dr[0])
    if dr != 0:
        dr = str('代理')
    if d != aaaa:
        print(c[0], '我的上级', d[0],dr)
    else:
        print('没有上级')
    return d

def select_user_05(d):
    cursor.execute("select inviter_account_uuid from user_invite where user_account_uuid = '%s'" % d)
    e = cursor.fetchone()
    cursor.execute("select role from user_invite where user_account_uuid = '%s'" % e)
    er = cursor.fetchone()
    er = int(er[0])
    if er != 0:
        er = str('代理')
    if e != aaaa:
        print(d[0], '我的上级', e[0],er)
    else:
        print('没有上级')
    return e

if __name__ == '__main__':
    uuid = '4c8dbbf2585849e3b6cebee196d4476a'
    a = select_user_01(uuid)
    b = select_user_02(a)
    c = select_user_03(b)
    d = select_user_04(c)
    select_user_05(d)
