import os

pwd = "/Users/daeyong/Documents"

# 디렉터리 내부 리스트 업
filenames = os.listdir(pwd)
print(filenames)

# 디렉터리인지 아닌지 여부
print(os.path.isdir(pwd+'/파일이름이나 폴더이름'))

# 파일인지 여부
print(os.path.isfile(pwd+'/파일이름이나 폴더이름'))

# 파일이름과 확장자분리
filepath = pwd + '/' + filenames[0]
print(filepath)
name, ext = os.path.splitext(filepath) # 파일이름과 확장자를 튜플로반환
print(name, ext)