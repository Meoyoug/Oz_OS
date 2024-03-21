# 파일 관련 예외는 운영체제와 관련이 있음을 확인해보자

try:
    f = open("none.txt", "r")
    print(f.read())
    f.close()

except FileNotFoundError as e:
    print(e)
    print(issubclass(FileNotFoundError, OSError))