import tracemalloc # 메모리 할당을 추적할 수 있도록 도와주는 라이브러리

tracemalloc.start()

# 메모리 할당이 진행되는 작업
# 1부터 10000까지 나오는 숫자를 문자열형태로 뿌리는 형태
data = [b'%d' % num for num in range(1, 10001)]
# 중간중간 공백을 넣어줌
joined_data = b' '.join(data)

current, peak = tracemalloc.get_traced_memory() # 현재 메모리사용량과 최대 메모리 사용량을 튜플로 반환해준다.
print(f'현재 메모리 사용량: {current / 10 ** 6} MB')
print(f'최대 메모리 사용량: {peak / 10 ** 6} MB')

tracemalloc.stop()

traced = tracemalloc.get_tracemalloc_memory() # tracemalloc이 사용한 메모리 조회
print(f'{traced / 10 ** 6} MB')