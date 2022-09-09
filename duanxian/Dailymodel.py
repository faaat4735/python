import mysql as db


def insertDaily(param):
    sql = "insert into s_daily (stock_id, trade_date, open, high, low, close, pre_close, val_chg, pct_chg, vol, amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
    return db.exec(sql, param)

def hasStock(code):
    sql = "select stock_id from s_stock WHERE ts_code = '%s'" % (code)
    return db.getOne(sql)

def updateStockShow(code):
    sql = "update s_stock set is_show = 1 where ts_code = '%s'" % (code)
    return db.exec(sql, ())

