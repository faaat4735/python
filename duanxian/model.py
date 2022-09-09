import mysql as db

def getAllStock():
    return db.getAll('select stock_id, ts_code from s_stock')

def insertStock(param):
    sql = "insert into s_stock (ts_code, symbol, name, area, industry, market, exchange, is_hs, list_date, add_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
    return db.exec(sql, param)

def hasStock(code):
    sql = "select stock_id from s_stock WHERE ts_code = '%s'" % (code)
    return db.getOne(sql)

def updateStockShow(code):
    sql = "update s_stock set is_show = 1 where ts_code = '%s'" % (code)
    return db.exec(sql, ())

