# 인터럽트 예제

import time
import signal # 신호 처리 라이브러리, 비동기 인터럽트에 대한 핸들러

# signum : 인터럽트의 유형 번호
# frame : 메모리영역 중 스택 영역의 정보
# 아래함수는 인터럽트 서비스 루틴, 인터럽트 핸들러의 역할

def signal_handler(signum, frame):
    print("키보드 인터럽트 감지")
    print('신호 번호 : ', signum)
    print('스택 프레임 : ', frame)
    exit() # 무한루프를 돌리다가 인터럽트 발생시 강제종료

# signal.SIGINT 키보드 인터럽트 상수
signal.signal(signal.SIGINT, signal_handler)

while True:
    print('5초 간격으로 출력중...')
    time.sleep(5)