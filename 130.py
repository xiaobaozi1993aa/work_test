from ks_02_open_redpacket_more import login,http_request
import pymysql
time_api = 'https://test_gateway.guochuangyuanhe.com/api/v1/nest/timeInfo/queryNestTimeInfo'
db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_nest')
cursor = db.cursor()
cursor.execute('select id,longitude,latitude from nest_location where id between 249001 and 249003')
location_id = cursor.fetchall()

def get_frist_time(token):
    for i in location_id:
        data = {"nestLocationId":i[0],"locationLatitude":str(i[1]),"locationLongitude":str(i[2])}
        print(data)
        r = http_request(api=time_api, method='post', token=token, **data)
        print(r)
        aa = r.get('response').get('current').get('nestTimeInfoId')
        print(aa)
        return aa


if __name__ == '__main__':
    phone = (a for a in range(19931997001, 19931997003))
    pass_word = 123456
    for mobie in phone:
        token = login(mobie, pass_word)
        get_frist_time(token)