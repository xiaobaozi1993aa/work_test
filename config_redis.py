import redis
from loger_test import TestLog

logger = TestLog().get_log()

def content_redis():
    try:
        redis_config = {"host": "172.18.228.11",
                        "port": 6379,
                        "password": "2018375tghfsbn8",
                        'db': 10
                        }
        db = redis.Redis(**redis_config)
        logger.info('连接成功: {}'.format(redis_config.get("host")))
        return db
    except Exception as err:
        logger.error('连接错误: {}'.format(err))



if __name__ == '__main__':
    content_redis()