import threading
import os
import time

# 문자열 데이터를 받아 무한히 출력하는 함수
# 3초마다 문자열을 출력
def something(word):
    while True:
        print(word)
        time.sleep(3)

'''

파이썬을 실행하면 기본적으로 메인 쓰레드가 하나 생기는데, 하위 쓰레드를 만들어 별도의 쓰레드에서 something이라는 함수를 실행시킨다.

하나의 프로세스 안에서 두개의 쓰레드 (메인, 하위(데몬))을 실행시키는 구조이다.

파이썬 파일을 실행해보면 메인쓰레드의 프린터문은 1초간격으로 실행되고, 별도의 쓰레드에서 3초간격으로 다른 프린터문이 실행되는 모습을 확인할 수 있다.

'''
if __name__ == "__main__":
    print('something의 프로세스 아이디: ', os.getpid())
    thread1 = threading.Thread(target=something, args=("hello",))
    thread1.daemon = True # 데몬 쓰레드 : 메인 쓰레드가 종료되면 같이 종료되는 쓰레드 -> 활성화
    thread1.start()
    print('메인 쓰레드에서 반복문을 시작')
    while True:
        try:
            print('main thread....')
            time.sleep(1)
        except KeyboardInterrupt:
            print('메인 쓰레드 종료')
            break