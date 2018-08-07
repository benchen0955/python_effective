# import bs4
# import requests

# res = requests.get('https://tw.stock.yahoo.com/q/q?s=2330')
# # 用 html 格式解碼 爬下來的檔案
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(soup)

# pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests

stock_id = 2330

doc = requests.get('https://tw.stock.yahoo.com/q/q?s={}'.format(stock_id))
html = BeautifulSoup(doc.text, 'html.parser')
table = html.findAll(text='個股資料')[0].parent.parent.parent #
data_row = table.select('tr')[1].select('td')
closing_price = data_row[7].text
print("台積電今日收盤價：${}".format(closing_price))
content = "台積電今日收盤價：${}".format(closing_price)
# content = "測試訊息！"

## Line Notify
lineUrl = "https://notify-api.line.me/api/notify"
token = "plEwlD7JExtUtAFHTi9P36B7T68pEag4KBlDBo6ayq1"
headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

payload = {'message': content}
r = requests.post(lineUrl, headers = headers, params = payload)
print(r.status_code)
print('line message ok')