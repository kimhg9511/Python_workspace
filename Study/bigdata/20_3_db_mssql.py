import pymssql as mssql
conn = mssql.connect(
    server='localhost',
    user='sa',
    password='1234',
    database='python'
)
email = 'hong6@naver.com'
with conn.cursor() as cursor:
    # insert
    sql = 'INSERT INTO users(email, pw) VALUES(%s, %s)'
    cursor.execute('BEGIN TRANSACTION')
    cursor.execute(sql, (email, '1111'))
    # selectOne
    sql = 'SELECT id, email, pw FROM users ORDER BY id DESC'
    cursor.execute(sql)
    row = cursor.fetchone()
    print(row)
    # rollback insert fault
    if row[1] == 'hong5@naver.com':
        conn.rollback()
    else:
        conn.commit()

with conn.cursor() as cursor:
    # selectAll
    sql = 'SELECT id, email, pw FROM users ORDER BY id DESC'
    cursor.execute(sql)
    rows = cursor.fetchall()
    if rows is None:
        print('empty')
    else:
        print('next : ')
        for row in rows:
            print(row)
