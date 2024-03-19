import psutil
import os

print('메모리 사용량 조회하기')

# 시스템 메모리의 사용량을 튜플형태로 반환해주는데 이를 dict로 반환하게끔 만들어준다.
memory_dict = dict(psutil.virtual_memory()._asdict()) 

print(memory_dict)

total = memory_dict['total'] # 사용 가능한 총량
available = memory_dict['available'] # 즉시 제공 가능한 양
percent = memory_dict['percent'] # available을 제외한 비율

print(f'메모리 총량: {total}')
print(f'메모리 즉시 제공 가능량: {available}')
print(f'메모리 사용률: {percent}')

"""
현재 프로세스에서 사용한 메모리 조회해보기
"""
pid = os.getpid()
current_process = psutil.Process(pid)

# memory_info 가 반환한 이터레이터중 첫번째에는 프로세스가 사용한 물리적인 데이터 량이 들어있다.
# 이를 2의 20 승으로 나누면 kb로 출력이 가능하다.
kb = current_process.memory_info()[0] / 2 ** 20
print(f'메모리 사용량: {kb:.2f} kb')