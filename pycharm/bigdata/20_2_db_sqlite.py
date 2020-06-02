import sqlite3 as sqlite
data = []
datas = []
with sqlite.connect('testdb.sqlite') as conn:
    # sql = """
    #     create table users(
    #         id integer not null primary key autoincrement,
    #         email varchar(255) not null,
    #         pw varchar(255) not null,
    #     );
    # """
    # cursor.execute(sql)
    cursor = conn.cursor()
    sql = "insert into users(email, password) values('hong4@', '1234')"
    cursor.execute(sql)
    sql = 'select * from users where email like ?'
    cursor.execute(sql, ("hong%",))
    rows = cursor.fetchall()
    datas[:] = rows
    print(datas)
    cursor.close()
