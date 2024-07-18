import pymysql


conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='fjd2023dnui',
    database='test0704',
    charset='utf8'
)

# 创建游标, 查询数据默认为元组类型
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS student")
# 创建student表
cursor.execute("""CREATE TABLE student (
            ID CHAR(10) NOT NULL,
            Name CHAR(8),
            Grade INT )""")

sql = """INSERT INTO student
         VALUES ('001', 'CZQ', 70),
                ('002', 'LHQ', 80),
                ('003', 'MQ', 90),
                ('004', 'WH', 80),
                ('005', 'HP', 70),
                ('006', 'YF', 66),
                ('007', 'TEST', 100)"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()
except pymysql.Error as e:
    # Rollback in case there is any error
    print(e)
    print('插入数据失败!')
    conn.rollback()

try:
    cursor.execute("SELECT * FROM student")
    results = cursor.fetchall()
    print(cursor.rowcount)
    for row in results:
        ID = row[0]
        Name = row[1]
        Grade = row[2]
        print(ID, Name, Grade)
except pymysql.Error as e:
    print("Error: unable to fetch data")

try:
    cursor.execute("DELETE FROM student WHERE Grade = 100")
    conn.commit()
except pymysql.Error as e:
    print('删除数据失败!')
    conn.rollback()

cursor.close()
conn.close()