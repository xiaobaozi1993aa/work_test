import pymysql


def sql_update():
    db = pymysql.Connect('172.18.228.112', 'root', '2nOI8ca76%$#1Gm4EH', 'gcyh_user')
    cursor = db.cursor()
    db.commit()
    return cursor

def csshi(cursor,sql_ml):
    cursor.execute(sql_ml)
    a = cursor.fetchone()
    print(a)

if __name__ == '__main__':
    cursor = sql_update()
    sql_ml = 'select mobile from user_info where user_account_uuid = "6b46009c77d4436fa835459edb1bbfd9"'
    csshi(cursor,sql_ml)