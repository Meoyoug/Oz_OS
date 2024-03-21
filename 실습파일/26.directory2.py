# 경로와 확장자 이용해 파일찾고, 내용읽기
import os

def search_file(dirname, extension):
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            search_file(filepath, extension)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == extension:
                with open(filepath, 'r', encoding='utf-8') as f:
                    print(f.read())