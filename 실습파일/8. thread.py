import threading
import os

def func():
    print('실험용으로 만들어 본 함수')
    print('나의 프로세스 아이디: ', os.getpid())
    print('쓰레드 아이디 : ', threading.get_native_id())

if __name__ == '__main__':
    print('기존 프로세스 아이디 : ', os.getpid())
    thread1 = threading.Thread(target=func) # target에 대한 쓰레드를 생성
    thread1.start()
