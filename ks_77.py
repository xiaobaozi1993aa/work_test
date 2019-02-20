'''
@1.递归查询上级

'''
import pymysql

db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_user')
cursor = db.cursor()
aaaa = ('0',)
aa = '5a7c09e6320d46f7b51664f016d1110c'
n = -1
def get_upper(uuid,n):
    cursor.execute("select inviter_account_uuid from user_invite where user_account_uuid = '%s'" % uuid)
    upper_uuid = cursor.fetchone()[0]
    n = n+1
    if upper_uuid != '0':
        cursor.execute("select role from user_invite where user_account_uuid = '%s'" % upper_uuid)
        upper_role = cursor.fetchone()[0]
        print("%s 的Upper UUID 是 %s " %(uuid, upper_uuid),upper_role)
        return get_upper(upper_uuid,n)
    else:
        print('end','共%s级' % n)

if __name__ == '__main__':
    get_upper(aa, n)





