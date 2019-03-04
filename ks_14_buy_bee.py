import pymysql
from ks_02_open_redpacket_more import login,http_request

db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_nest')
cursor = db.cursor()

time_api = 'https://test_gateway.guochuangyuanhe.com/api/v1/nest/timeInfo/queryNestTimeInfo'
buy_api = 'http://test_gateway.guochuangyuanhe.com/api/v1/nest/timeInfo/buyNestTime'



#获取初期ID
def get_frist_time(token,i):
    data = {"nestLocationId":i[0],"locationLatitude":str(i[1]),"locationLongitude":str(i[2])}
    r = http_request(api=time_api, method='post', token=token, **data)
    print(data)
    aa = r.get('response').get('current').get('nestTimeInfoId')
    return aa

#循环购买
def buy_bee(token,info_id):
    data = {"price": 1, "channelCode": "ios", "nestTimeInfoId": info_id, "payType": "10001",
            "safetyCode": "123456", "longitude": "113.021121", "latitude": "25.776524"}
    r = http_request(api=buy_api, method='post', token=token, **data)
    return r

if __name__ == '__main__':
    phone = (a for a in range(19931997001, 19931997100))
    pass_word = 123456
    cursor.execute('select id,longitude,latitude from nest_location where id between 249001 and 250000')
    location_id = cursor.fetchall()
    for mobie in phone:
        token = login(mobie, pass_word)
        for i in location_id:
            info_id = get_frist_time(token,i)
            response = buy_bee(token,info_id)
            print(response)
