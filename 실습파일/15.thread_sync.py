import threading
from multiprocessing import Value, Lock
'''
프로세스와 마찬가지로 하위 쓰레드에서도 공유자원 접근에대한 동기화를 적용해 볼 수 있다.
공유 숫자를 두개의 프로세스로 접근하여 하나의 프로세스는 더하기연산을 반복, 하나의 프로세스는 빼기 연산을 반복하여
뮤텍스 락을 적용시켜서 결과를 확인해보자
'''
def counter1(snum, cnt, lock):
    lock.acquire()
    try:
        for i in range(cnt):
            snum.value += 1
    finally:
        lock.release()

def counter2(snum, cnt, lock):
    lock.acquire()
    try:
        for i in range(cnt):
            snum.value -= 1
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()

    shared_number = Value('i', 0)
    t1 = threading.Thread(target=counter1, args=(shared_number, 5000, lock))
    t1.start()
    t2 = threading.Thread(target=counter2, args=(shared_number, 5000, lock))
    t2.start()

    t1.join()
    t2.join()

    print('finally, number is ', shared_number.value)