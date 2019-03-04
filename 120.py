import pymysql


db = pymysql.Connect('172.18.228.112', 'root', '3nOI9ca45%$#8Gm7EH', 'gcyh_nest')
cursor = db.cursor()
cursor.execute('select id,longitude,latitude from nest_location where id between 249001 and 249003')
location_id = cursor.fetchall()
for i in location_id:
    print(i[0])


