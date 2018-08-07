from PIL import Image
# 若要把 Lenna 的臉部模糊, 可用 pillow 的濾鏡功能
from PIL import ImageFilter

import os

file_name='lenna_sharp.jpg'
file_name_c='lenna_sharp_2.jpg'
file_path = "D:/python_effective/"
os.chdir(file_path)
lenna = Image.open(file_name)
a=120
b=60
c=420
d=500
box = (a,b,c,d)
cute = [a,b,c,d]
cropLenna = lenna.crop(cute)
# 將截取的部分用濾鏡模糊
lennaBlurred = cropLenna.filter(ImageFilter.BLUR)
# lennaBlurred.save(file_name)

# 若模糊的效果不夠，可用 for loop 把同樣的濾鏡套用很多次
for i in range(10):
    lennaBlurred = lennaBlurred.filter(ImageFilter.BLUR)

box = (a,b,c,d)
cute = [a,b,c,d]
# 用 .paste() 將模糊後的部分貼囘原本的影像（用 box tuple 指定原圖要被貼上的位置）
lenna.paste(lennaBlurred, cute)
lenna.save(file_name_c)