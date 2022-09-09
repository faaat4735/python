import stock
import model
import Dailymodel as dModel


# 添加股票
def addStock(nameList, addDate):
    for name in nameList:
        stockInfo = stock.getStockInfo(name)
        stockInfo = stockInfo.iloc[0]
        #判断是否在列表中，是则修改is_show为1 否则插入
        if model.hasStock(stockInfo['ts_code']) == None:
            model.insertStock((stockInfo['ts_code'], stockInfo['symbol'], stockInfo['name'], stockInfo['area'], stockInfo['industry'], stockInfo['market'], stockInfo['exchange'], stockInfo['is_hs'], stockInfo['list_date'], addDate))
        else :
            model.updateStockShow(stockInfo['ts_code'])

addDate = '2022-09-08'
addDate1 = addDate.replace('-', '')
addStock(['上海港湾', '上海电力', '金奥博', '冀凯股份', '博深股份', '佳电股份', '安凯客车'], addDate)

# 查询历史股票的记录，并记录
allStock = model.getAllStock()
for code in allStock:
    dailyInfo = stock.getStockDaily(code[1], addDate1, addDate1)
    dailyInfo = dailyInfo.iloc[0]
    dModel.insertDaily((code[0], addDate, dailyInfo['open'], dailyInfo['high'], dailyInfo['low'], dailyInfo['close'], dailyInfo['pre_close'], dailyInfo['change'], dailyInfo['pct_chg'], dailyInfo['vol'], dailyInfo['amount']))
#生成excel todo






