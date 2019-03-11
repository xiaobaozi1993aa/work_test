import pymysql
from loger_test import TestLog
logger = TestLog().get_log()

class Test_Sql(object):

    def __init__(self):
        self.host = '172.18.228.112'
        self.name = 'root'
        self.pass_wd = '2nOI8ca76%$#1Gm4EH'

    def content_db(self,lib_name):
        try:
            self.db = pymysql.connect(self.host, self.name, self.pass_wd, lib_name)
            self.cursor = self.db.cursor()
            logger.info('%s :连接成功' % lib_name)
            return self.cursor
        except Exception as e:
            logger.error('连接错误: %s' % e)

    # def select_sql(self,sql_ml):
    #     try:
    #         self.cursor.execute(sql_ml)
    #         logger.info('查询成功')
    #         return self.cursor.fetchone()
    #     except:
    #         logger.error()
