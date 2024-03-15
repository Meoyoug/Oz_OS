# 내 파이썬 프로그램의 이름 알아보기
# psutil을 사용해서 사용중인 프로세스 중에 
# 7. process_homework.py에 해당하는 프로세스를 찾을 경우 프린트로 출력
import os
import psutil

current_pid = os.getpid()

for proc in psutil.process_iter():
    process_id = proc.pid
    if process_id == current_pid:
        print('과제의 프로세스 이름: ', proc.name())
        print('과제의 프로세스 아이디: ', proc.pid)
        print('부모 프로세스 아이디: ', proc.ppid())
        print('부모 프로세스 이름: ', psutil.Process(proc.ppid()).name())
    

