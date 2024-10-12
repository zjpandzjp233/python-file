from pymysql import Connection

conn=Connection(
host="localhost",
port=3306,
user="root",
password="Dx!2505185559",
charset='utf8', #防止乱码
autocommit=True # 设置为自动确认就无需手动确认了
)
print(conn.get_server_info())# 查看是否连接
conn.select_db("world") # 创建数据库
cursor=conn.cursor() # 用cursor和数据库交互
# cursor.execute("""    
# create table testTable(
# id int,
# name varchar(10),
# gender varchar(1),
# age int
# )
# """) # 运行代码
#cursor.execute("select * from student;") # 执行指定的代码
cursor.execute("insert into testtable(id,name,gender,age) value(4,'z1jhp','女',2), (5,'zfjdx','男',9), (6,'lj8l','女',2);")
conn.commit()# 只有确认后数据才能成功插入
fetched_tuple=cursor.fetchall() # 抓取上面代码获得的内容，输出元组
print(fetched_tuple) # ((1, 'z1jhp', '女', 1), (2, 'zfjdx', '男', 2), (3, 'lj8l', '女', 3), (4, 'dsf', '女', 4), (5, 'zxj', '男', 5), (6, 'zjp', '女', 6))
conn.close()


# 当上面输入的指令太长，可以用\让字符串换行接着输入
str1="123456"\
"123456"
a=99
b=11
str2=f'a={a}'\
f'b={b}'
print(str1) # 123456123456
print(str2) # a=99b=11