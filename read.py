
import pymysql
import re
#链接数据库
db=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='stu',charset='utf8')
#生成游标对象(用于操作数据库数据,获取sql执行结果的对象)
cur=db.cursor()


sql="select name,age from cls1;"
cur.execute(sql)#执行语句,没有返回值
#cur 可迭代对象,通过迭代获取select结果
##or i in cur:
#   print(i)
print("=========================================================")
#获取一个结果
#print(cur.fetchone())

#获取多个查询结果
#print(cur.fetchmany(3))

#获取所有查询结果
print(cur.fetchall())

db.close()
cur.close()