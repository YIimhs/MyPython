"""

"""
import pymysql
#链接数据库
db=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='stu',charset='utf8')
#生成游标对象(用于操作数据库数据,获取sql执行结果的对象)
cur=db.cursor()



#对数据库执行写操作
try:
    # #insert插入
    # sql="update cls1 set sex='m' where name='Emma';"
    # cur.execute(sql)
    # #delete 删除
    # sql="delete from cls1 where sex is null;"
    # cur.execute(sql)
    exe=[]
    for i in range(3):
        name=input("请输入姓名:")
        age=input("请输入年龄:")
        score=input("请输入分数:")
        exe.append((name,age,score))
    sql="insert into cls1 (name,age,score) values (%s,%s,%s)"
    cur.execute(exe)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()