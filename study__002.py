from study_001 import Test_Sql
from config_kshb import TestLog
cursor = Test_Sql().content_db('gcyh_user')
# logger = TestLog().getlog()
from loger_test import TestLog
logger = TestLog().get_log()

def csshi(cursor,sql_ml):
    try:
        cursor.execute(sql_ml)
        a = cursor.fetchone()
        logger.info('查询结果: %s' %a[0])
    except:
        pass

if __name__ == '__main__':
    sql_ml = 'select mobile from user_info where user_account_uuid = "6b46009c77d4436fa835459edb1bbfd9"'
    csshi(cursor,sql_ml)