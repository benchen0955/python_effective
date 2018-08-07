# pip install xlwings

# import xlwings as xw
# wb = xw.Book(r"你的 Excel 檔案的絕對路徑")
# # 讀出 2330 試算表資料，存入 sheet 變數
# sheet = wb.sheets['2330']
# # cells(row, column) 取得試算表底下 row 值為 3, column值為 2 的儲存格
# print(sheet.cells(3, 2).value) # 224.5
# # cells(row, column) 的 column (欄) 也可以用字串表示，非常直覺！
# print(sheet.cells(4, 'B').value) # 233.0

###############################################
# win32api.MessageBox(win32con.NULL, 'Python 你好！', '你好', win32con.MB_OK) 
import xlwings as xw
wb = xw.Book(r"D:\python_effective\\stock_price_data.xlsx")
# 讀出 2330 試算表資料，存入 sheet 變數
sheet = wb.sheets['2330']
# 算出所有的報酬率
for i in range(3, 72):
    returnValue = (sheet.cells(i, "B").value - sheet.cells(i-1, "B").value) / sheet.cells(i-1, "B").value
        # 每迭代一次，就將值印出
    print(returnValue)
        # 再把值寫入同一個 row 的 C 欄内
    sheet.cells(i, "C").value = returnValue

####################################################

# import xlwings as xw
# wb = xw.Book(r"D:\python_effective\stock_price_data.xlsx")
# sheet = wb.sheets['2330']
# for i in range(3, 72):
#     returnValue = (sheet.cells(i, "B").value - sheet.cells(i-1, "B").value) / sheet.cells(i-1, "B").value
#     sheet.cells(i, "C").value = returnValue
#         # 若上漲，顯示紅色，儲存格顔色用 (R, G, B) 三原色强度設定
#     if returnValue > 0:
#         sheet.cells(i, "C").color = (255, 0, 0)
#         # 若下跌，顯示綠色
#     elif returnValue < 0:
#         sheet.cells(i, "C").color = (0, 255, 0)


# import xlwings as xw
# wb = xw.Book(r"D:\python_effective\stock_price_data.xlsx")
# sheet = wb.sheets['2330']
# # 把一個二維陣列放入一個從 F1 開始的儲存格範圍
# sheet.range('F1').value = [
#            ['Foo 1', 'Foo 2', 'Foo 3'], 
#            [10.0, 20.0, 30.0]
#           ]