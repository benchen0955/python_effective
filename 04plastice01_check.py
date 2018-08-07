import os

dir = r'D:\python_effective'

# 會回傳你這個 python 程式碼檔案的路徑
print(os.getcwd())

# 會取得你在這個路徑下的所有路徑
listdir = os.listdir(dir)
print("==================")
print(listdir)
print("==================")
# # 用回圈把每一個路徑都檢查一遍
for file in listdir:    
    # print("{}/{}".format(dir,file))
    # 合并檔名和路徑
    filepath = os.path.join(dir, file)    
    print(filepath)
    # 檢查該路徑是否為檔案
    if os.path.isfile(filepath):
        print("{} 是檔案".format(file))
    # 檢查該路徑是否為資料夾
    elif os.path.isdir(filepath):
        print("{} 是資料夾".format(file))
# 創造一個新的絕對路徑
if os.path.isdir('backup_folder'):
    print ('backup_folder existed')
else:
    backup_folder_path = os.path.join(dir, 'backup_folder')
    os.makedirs(backup_folder_path)
    print("make new dir ==> backup_folder ok")

# 查詢該路徑占用的硬碟空間大小
print("total size is %d" % os.path.getsize(dir))