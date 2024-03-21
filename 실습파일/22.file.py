# 기본적인 파일 입출력 예제

with open("number_one.txt", "w") as f:
    f.write("one!")

with open("number_two.txt", "w") as f:
    f.write("two!")

with open("number_three.txt", "w") as f:
    f.write("three!")

with open("number_four.txt", "w") as f:
    f.write("four!")

# 파일네임의 패턴을 이용해 한번에 접근하기
import glob

for filename in glob.glob("*.txt", recursive=True):
    print(filename)

import fileinput # 파일의 내용들을 읽어올 수 있음

with fileinput.input(glob.glob('*.txt')) as fi:
    for line in fi:
        print(line)

# 파일 이름이 매치되는 것을 찾아줌
import fnmatch
import os

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '??????_*.txt'):
        print(filename)
