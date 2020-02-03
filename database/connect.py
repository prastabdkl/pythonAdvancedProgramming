# https://www.journaldev.com/15539/python-mysql-example-tutorial

import PyMySQL as pymysql
#database connection, conntect take sfour arguments, hostname and others
connection = pymysql.connect(host = 'localhost',user = 'root',passwd ='',database ='testdb_ap')
cursor = connection.cursor()
#some other statements with the help of cursor
# table_from_code = """CREATE TABLE employee1(
#     ID INT(20) PRIMARY KEY AUTO_INCREMENT,
#     NAME VARCHAR(20) NOT NULL, SURNAME VARCHAR(20) NOT NULL, DEPARTMENT VARCHAR(20) NOT NULL
#     )"""

# cursor.execute(table_from_code)
print('table successfully created')

# insert1 = "INSERT INTO employee1(NAME,SURNAME,DEPARTMENT) VALUES ('ram','sharma','sales')"
# cursor.execute(insert1)

#select the data
# queries for retrievint all rows
retrive = "Select * from employee1;"

#executing the quires
cursor.execute(retrive)
rows = cursor.fetchall()
for row in rows:
   print(row)

#update the data
updateSql = "UPDATE  employee1 SET NAME= 'shyam'  WHERE ID = '2' ;"
cursor.execute(updateSql)

# queries for retrievint all rows
retrive = "Select * from employee1;"

#executing the queries
cursor.execute(retrive)
rows = cursor.fetchall()
for row in rows:
   print(row)

#delete the data entity
deleteSql = "DELETE FROM employee1 WHERE ID = '2'; "
cursor.execute(deleteSql )

#drop table
dropSql = "DROP TABLE IF EXISTS employee;"
cursor.execute(dropSql)

#commit the connection after inserting into database
connection.commit()
connection.close()  