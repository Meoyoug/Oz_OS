# 다른 작업을 하는 여러 개의 하위 프로세스 생성
from multiprocessing import Process
import os
import time

def func1():
    print("func1 프로세스 아이디: ", os.getpid())
    print("부모 프로세스 아이디: ", os.getppid())

def func2():
    print("func2 프로세스 아이디: ", os.getpid())
    print("부모 프로세스 아이디: ", os.getppid())

def func3():
    print("func3 프로세스 아이디: ", os.getpid())
    print("부모 프로세스 아이디: ", os.getppid())

if __name__ == '__main__':
    print('6.multi_processing3.py 프로세스 아이디: ', os.getpid())
    # 각각 다른 함수를 하위 프로세스로 만든다.
    child1 = Process(target=func1).start() # func1을 하위 프로세스로 만듦
    child2 = Process(target=func2).start() # func2을 하위 프로세스로 만듦
    child3 = Process(target=func3).start() # func3을 하위 프로세스로 만듦