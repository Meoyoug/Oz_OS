# 파이썬 프로그램도 프로세스가 될 수 있다.
# 파이썬 코드 동작시 할당되는 프로세스의 아이디를 확인하는 코드
import os

# os.getpid() -> 프로세스 아이디를 가져옴
print('파이썬 코드 실행중.. 실행중인 프로세스 아이디는 : ', os.getpid())


# 내 컴퓨터에서 돌아가는 크롬에 해당하는 프로세스 조회하기
import psutil

# 프로세스들에 반복적으로 접근하여 개별 프로세스의 이름을 가져옴
for proc in psutil.process_iter():
    process_name = proc.name()
    # 프로세스의 이름에 크롬이 포함되어있으면 프린트.
    if "chrome" in process_name:
        print(process_name, proc.pid)