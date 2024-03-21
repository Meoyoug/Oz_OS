import concurrent.futures
import time
"""
스레드 풀의 작동원리를 코드 실행을 통해 이해해보자.

0, 1, 2, 3, 4 의 스레드에 순차적으로 작업을 주어지게 하지만

끝나는 작업의 순서는 다름을 볼 수 있다. -> 먼저 끝나는 스레드가 또 다른 작업을 가져갈 수 있다.
"""
def task(name):
    time.sleep(0.5)
    return f"{name}의 작업 완료"

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        future_name = {executor.submit(task, f"Task-{i}") : f"Task-{i}" for i in range(5)}

        # 작업 완료된 순서대로 결과 출력

        for future in concurrent.futures.as_completed(future_name):
            name = future_name[future]
            try:
                result = future.result()
                print(f"{name}의 결과 : {result}")

            except Exception as e:
                print(f"{name}에서 예외 발생 : {e}")