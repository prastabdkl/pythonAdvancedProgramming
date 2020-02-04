import pymysql
connection = pymysql.connect(host = 'localhost',user = 'root',passwd ='',database ='ap_db')
cursor = connection.cursor()

connection.commit()
connection.close()