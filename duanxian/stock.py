import tushare as ts

#filename = 'stock_base.txt'
#f = open(filename, 'wt', encoding= 'utf-8')
#print(type(f))
ts.set_token('78d48a37ff275165030d8aa5e0d8e6eca7eb2fed1b83ec92ff6dfafe')
pro = ts.pro_api()

# 获取股票基本信息
def getStockInfo(stockName):
#     return pro.stock_company(exchange='SSE')
    return pro.stock_basic(name=stockName,fields='ts_code,symbol,name,area,industry,market,exchange,is_hs,list_date')
# 获取股票当日信息
def getStockDaily(code, start_date, end_date):
    return pro.daily(ts_code=code, start_date=start_date, end_date=end_date)

if __name__ == '__main__':
    data = pro.query('stock_basic', exchange='', list_status='L', name='立新能源', fields='ts_code,symbol,name,area,industry,market,exchange,is_hs,list_date')
    print(data)
