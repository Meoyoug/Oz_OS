'''
실행전 터미널에서 ps -el | grep python 명령어를 통해 python이라는 이름을 포함한 동작중인 프로세스의 상세내역을 출력해본다.

이후에 파이썬 파일을 실행하고 다시 명령어를 실행해보면 여러개의 프로세스가 추가되어있는 모습을 확인가능하다.

multiprocessing.spwan => 멀티 프로세스에 의해서 돌아가고있음.
multiprocessing-fork => 프로세스 복사시에 fork함수가 사용되었다.

6번째 숫자는 프로세스의 우선순위를 나타내는데 이를 통해 프로세스들의 우선순위가 모두 같은 것을 확인가능하다.

우선순위가 같은 프로세스들을 처리하기 위한 CPU 스케줄링 알고리즘이 존재한다.

'''

from multiprocessing import Process
import os

def func1():
    while True:
        try:
            print("func1 프로세스 아이디: ", os.getpid())
            print("부모 프로세스 아이디: ", os.getppid())
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            break

def func2():
    while True:
        try:
            print("func2 프로세스 아이디: ", os.getpid())
            print("부모 프로세스 아이디: ", os.getppid())
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            break

def func3():
    while True:
        try:
            print("func3 프로세스 아이디: ", os.getpid())
            print("부모 프로세스 아이디: ", os.getppid())
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            break

if __name__ == '__main__':
    print('6.multi_processing3.py 프로세스 아이디: ', os.getpid())
    # 각각 다른 함수를 하위 프로세스로 만든다.
    child1 = Process(target=func1).start() # func1을 하위 프로세스로 만듦
    child2 = Process(target=func2).start() # func2을 하위 프로세스로 만듦
    child3 = Process(target=func3).start() # func3을 하위 프로세스로 만듦

