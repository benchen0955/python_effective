# import PyPDF2
# import os
# os.chdir(r'c:\pyyrhon_proj')
# pdfFile = open('ror.pdf', 'rb')
# reader = PyPDF2.PdfFileReader(pdfFile)
# # 可以把 writer 想象成是被寫入内容的暫存區
# writer = PyPDF2.PdfFileWriter()
# # 取得 ror.pdf 檔案的第一頁
# page1 = reader.getPage(0)
# # 取出該頁的文字
# pageText = page1.extractText()
# # 限制：如果你的 PDF 是中文，PyPDF2 讀取出的文字會產生亂碼
# print(pageText)

################################################################

# import PyPDF2
# import os
# os.chdir(r'c:\pyyrhon_proj')
# pdfFile = open('ror.pdf', 'rb')
# # 讀取出 PDF 黨的資料，寫入 reader 變數
# reader = PyPDF2.PdfFileReader(pdfFile)
# # 可以把 writer 想象成是被寫入内容的暫存區
# writer = PyPDF2.PdfFileWriter()
# # 取得 ror.pdf 檔案的第一頁
# page1 = reader.getPage(0)
# # 注意 addPage 只能把一頁 pdf 放到新 pdf 檔的最後面
# writer.addPage(page1)
# # 開啓一個名為 ror1.pdf 的新 pdf 檔案
# outputPdf = open('ror1.pdf', 'wb')
# # 將目前 writer 物件的内容寫入新的 pdf 檔内
# writer.write(outputPdf)
# # 這個很重要！
# outputPdf.close()

##############################################################

# import PyPDF2
# import os
# os.chdir(r'c:\pyyrhon_proj')
# pdfFile = open('ror.pdf', 'rb')
# # 讀取出 PDF 黨的資料，寫入 reader 變數
# reader = PyPDF2.PdfFileReader(pdfFile)
# # 可以把 writer 想象成是被寫入内容的暫存區
# writer = PyPDF2.PdfFileWriter()
# # 將 ror.pdf 每一頁的内容加入 writer
# for pageNum in range(reader.numPages):
#     pdfPage = reader.getPage(pageNum)
#     writer.addPage(pdfPage)
# # 將同樣的 ror.pdf 每一頁的内容加入 writer
# for pageNum in range(reader.numPages):
#     pdfPage = reader.getPage(pageNum)
#     writer.addPage(pdfPage)
# outputPdf = open('ror_copy.pdf', 'wb')
# writer.write(outputPdf)
# outputPdf.close()

#################################################

# import PyPDF2
# import os
# os.chdir(r'c:\pyyrhon_proj')
# pdfFile = open('ror.pdf', 'rb')
# reader = PyPDF2.PdfFileReader(pdfFile)
# writer = PyPDF2.PdfFileWriter()
# watermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
# # 取得 ror.pdf 第一頁
# firstPage = reader.getPage(0)
# # 取得浮水印
# watermark = watermarkReader.getPage(0)
# # 將浮水印以圖層的方式與 ror.pdf 第一頁結合
# firstPage.mergePage(watermark)
# # 把結合后的結果存入 writer 暫存區
# writer.addPage(firstPage)
# # 最後再將 writer 的内容寫入新的 pdf 檔
# outputPdf = open('watermark_ror.pdf', 'wb')
# writer.write(outputPdf)
# outputPdf.close()

#########################################

import PyPDF2
import os
os.chdir(r'D:\python_effective')
pdfFile = open('ror.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)

writer = PyPDF2.PdfFileWriter()
watermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
# watermark = watermarkReader.getPage(0)
watermark = watermarkReader.getPage(0)
for pageNum in range(reader.numPages):
    page = reader.getPage(pageNum)
    page.mergePage(watermark)
    
    writer.addPage(page)
outputPdf = open('all_watermark_ror.pdf', 'wb')
writer.write(outputPdf)
outputPdf.close()