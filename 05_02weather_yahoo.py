import requests

result = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20item.forecast%2C%20item.condition%2C%20atmosphere%20%20%20from%20weather.forecast%20where%20woeid%20%3D%202306179%20and%20u%3D%22c%22%20limit%201&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")

jsonData = result.json()
# print(jsonData['query']['results']['channel']['item']['forecast'])
forecastData = jsonData['query']['results']['channel']['item']['forecast']
# 最高與最低氣溫
highTemp = forecastData['high']
lowTemp = forecastData['low']

print('最高氣溫： {} 度，最低氣溫： {} 度'.format(highTemp, lowTemp))
content = '最高氣溫： {} 度，最低氣溫： {} 度'.format(highTemp, lowTemp)
# content = "陳文化 測試訊息！"

## Line Notify
lineUrl = "https://notify-api.line.me/api/notify"
token = "token"
headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

payload = {'message': content}
r = requests.post(lineUrl, headers = headers, params = payload)
print(r.status_code)
print('line message ok')