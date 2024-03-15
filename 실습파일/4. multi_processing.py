# 같은 작업을 하는 하나의 하위 프로세스 생성
from multiprocessing import Process
import os

def func():
    print('실험용으로 만들어 본 함수')
    print('나의 프로세스 아이디: ', os.getpid())
    print('나의 부모 프로세스 아이디: ', os.getppid()) # ppid는 부모 프로세스의 아이디

if __name__ == '__main__':
    print('4.multi_processing.py 프로세스 아이디: ', os.getpid())
    child = Process(target=func).start() # target을 하위 프로세스로 만듦