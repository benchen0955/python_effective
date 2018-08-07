import os
import shutil

dir = r'D:\python_effective'
dest = r'D:\python_effective\backup_folder'

listdir = os.listdir(dir)


# 每一個在原始資料夾内的檔案
for file in listdir:
    # 拼凑出絕對路徑
    fullName = os.path.join(dir, file)
        # 偵測該檔案的副檔名是否為 'jpg'
    if fullName.endswith('jpg') or fullName.endswith('png'):
        print(fullName)
                # 如果是，就拼凑出目地資料夾的路徑，複製該圖檔至目地資料夾
        destPath = os.path.join(dest,file)
        print(destPath)
        shutil.copy(fullName, destPath)