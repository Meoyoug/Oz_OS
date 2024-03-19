"""
페이지교체 중 선입 선출 방식을 코드로 구현해보자.
"""

class PageReplacementFIFO :
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []

    def access_page(self, page):
        if page not in self.pages:
            if len(self.pages) >= self.capacity:
                self.pages.pop(0) # 제일 앞의 페이지를 제거
            self.pages.append(page) # 새로들어온 페이지를 추가

    def status(self):
        print("현재 페이지 상태 : ", self.pages)

page_replacement = PageReplacementFIFO(capacity=3)
page_replacement.status()

# 4부터는 선입선출이 적용되어야한다. capacity가 3이기 때문에.
for i in range(1,6):
    page_replacement.access_page(i)
    page_replacement.status()