from multiprocessing import Process
import os
import time

# 파일을 통한 통신 예제

def wrirer():
    print(f'{os.getpid()}가 파일에 쓴다')
    with open('IPS.txt', 'w') as f:
        f.write(f'Hello')

def reader():
    with open('IPS.txt', 'r') as f:
        print(f.read())

if __name__ == '__main__':
    p1 = Process(target=wrirer)
    p1.start()

    time.sleep(2) # 파일을 쓰는동안 읽지않도록 딜레이를 준다.

    p2 = Process(target=reader)
    p2.start()

    p1.join()
    p2.join()