
import pymysql
import re
#链接数据库
db=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='dict',charset='utf8')
#生成游标对象(用于操作数据库数据,获取sql执行结果的对象)
cur=db.cursor()


fr=open('dict.txt')
list_explain=[]
for line in fr:
    tup=re.findall(r"(\S+)\s+(.*)",line)[0]
    list_explain.append(tup)
fr.close()
sql="insert into words (word,mean) values (%s,%s);"
try:
    cur.executemany(sql,list_explain)
    db.commit()
except:
    db.rollback()

db.close()
cur.close()