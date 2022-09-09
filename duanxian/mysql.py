import MySQLdb

db = MySQLdb.connect(host='127.0.0.1',port=3307,user='root',passwd='123456',db='my_stock')
cursor = db.cursor() #创建一个游标对象


def getOne(sql):
    cursor.execute(sql)
    return cursor.fetchone()

def getAll(sql):
    cursor.execute(sql)
    return cursor.fetchall()

def getColumn(sql):
    cursor.execute(sql)
    return [record[0] for record in cursor.fetchall()]

def getRow(sql):
    cursor.execute(sql)
    return cursor.fetchmany(1)

def exec(sql, param):
    cursor.execute(sql, param)
    return db.commit()

