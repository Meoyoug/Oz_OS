from multiprocessing import Process, Value, Lock

'''
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
    p1 = Process(target=counter1, args=(shared_number, 5000, lock))
    p1.start()
    p2 = Process(target=counter2, args=(shared_number, 5000, lock))
    p2.start()

    p1.join()
    p2.join()

    print('finally, number is ', shared_number.value)