import pymysql as mysql
# connect(host, id, pw, db)
conn = mysql.connect(host="localhost", user="root", password="1234", db="bigdata")
# cursor()
try:
    # insert
    with conn.cursor() as cursor:
        sql = 'INSERT INTO users(email, pw) VALUES(%s, %s)'
        cursor.execute(sql, ('hong4@naver.com', '1111'))
        conn.commit()
    # read
    with conn.cursor() as cursor:
        # sql = 'SELECT id, pw FROM users WHERE id = %s'
        sql = 'SELECT id, pw FROM users'
# execute()
        # cursor.execute(sql, (1,))  # resultSet stored in cursor
        cursor.execute(sql)
# fetchall(), fetchone()
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    # insert
# rollback()
finally:
    conn.close()
