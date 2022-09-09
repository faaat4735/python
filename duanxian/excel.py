import datetime
import openpyxl

wb = openpyxl.load_workbook('duanxian.xlsx')
#获取工作表名
# sheet = wb.sheetnames
sheet = wb.active
sheet.insert_cols(idx=2)
wb.save('duanxian.xlsx') # 名称重复会覆盖
# stock.sort(key=sort_stock)
#print(stock)
