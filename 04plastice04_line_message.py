# https://notify-bot.line.me/my/
#   
#   
# lenna_sharp.jpg
import requests

content = "測試訊息！"

## Line Notify
lineUrl = "https://notify-api.line.me/api/notify"
token = "token"
headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
picURI="light.jpg"
files = {'imageFile': open(picURI, 'rb')}
stickerPackageId = 2
stickerId = 38
payload = {"message": content, "stickerPackageId": stickerPackageId, 'stickerId': stickerId}
# payload = {"message": content}
# payload = {'message': content}
# r = requests.post(lineUrl, headers = headers, params = payload,files = files)
r = requests.post(lineUrl, headers = headers, params = payload)

print(r.status_code)
# print('line message ok')