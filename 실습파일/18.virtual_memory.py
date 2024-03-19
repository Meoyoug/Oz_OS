foods = ["bugger", "pizza", "salad"]

print(id(foods)) # id는 foods가 참조하는 메모리 주소(가상 주소)를 나타내준다.
print(hex(id(foods))) # id를 16 진수로 확인, 가상 주소는 실행할 때마다 바뀌는 것을 확인가능하다.

mv = memoryview(b"hello") # menoryview는 인자의 참조하는 주소를 가져온다. 인자는 이진데이터로 넣어준다.
print(mv)

# 이진데이터로 들어간 인자를 인덱싱해서 값을 가져올수도있다. 바이트형태로 전달했기 때문에 유니코드로 출력된다.
# 범위를 넘어가면 인덱스 에러를 발생시킨다.
print(mv[0])
print(mv[1])
print(mv[2])