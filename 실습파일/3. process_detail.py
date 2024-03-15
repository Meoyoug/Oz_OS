import psutil

for proc in psutil.process_iter() :
    process_name = proc.name()
    if "chrome" in process_name:
        # 해당 프로세스의 자식을 가져옴
        child = proc.children()
        # 프로세스이름, 상태, 부모 프로세스 모두 프린트
        print(process_name, proc.status(), proc.parent())

        # 자식프로세스가 존재하면 프린트.
        if child :
            print(f'{process_name}의 자식 프로세스 : ', child)