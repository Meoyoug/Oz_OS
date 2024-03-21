# 파일 복사 또는 이동
import os
import shutil

pwd = '폴더나 파일경로'
extension = '.확장자명'
keyword = '파일이름 중 일부'
new_dir = 'pwd 아래의 새로운 폴더'
filenames = os.listdir(pwd)

for filename in filenames:
    if keyword in filename:
        origin = os.path.join(pwd, filename)
        print(origin)
        shutil.copy(origin, os.path.join(pwd, 'copy' + extension)) # 복사
        shutil.move(origin, os.path.join(pwd, new_dir)) # new_dir로 파일 이동