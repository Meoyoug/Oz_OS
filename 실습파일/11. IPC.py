from multiprocessing import Process, Pipe
import os

def send(conn):
    print(f'{os.getpid()}가 {os.getppid()}에게 데이터를 보낸다')
    conn.send('Hello parent')
    conn.close()

if __name__ == '__main__':
    parent, child = Pipe() # Pipe는 두개의 값을 반환하는 튜플 생성자이다.
    p = Process(target=send, args=(child,)) # child가 parent에 보낼것임으로 args에 child를 입력
    p.start() # 프로세스실행
    print('기존 프로세스 아이디: ', os.getpid()) 
    print(parent.recv()) # 부모가 받은것을 보여줌
    p.join() # 프로세스를 기다림