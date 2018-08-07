# 引用 pillow 套件是 PIL, 而非 pillow
from PIL import Image
# 開啓影像檔
lenna = Image.open(r'D:\python_effective\lenna_sharp.jpg')
# 取得影像檔案大小 (以像素計算)
# width, height = lenna.size

# print("{} {}".format(width, height))
# # 輸入你想要的寬與高(以象素計算，記得放入整數)
# # 我們希望把圖縮小成原圖 1/2 的比例
# halfLenna = lenna.resize((int(width), int(height)))
# # #最後別忘了將檔案存成一個圖檔
# # halfLenna.save(r'D:\python_effective\lenna_sharp.jpg')

# # .rotate(n) 是指把圖檔以逆時鐘方向轉 n 度
# halfLenna.rotate(45).save(r'D:\python_effective\lenna_sharp.jpg')

box = (106, 51, 406, 512)
cropLenna = lenna.crop(box)
cropLenna.save(r'D:\python_effective\lenna_sharp_1.jpg')