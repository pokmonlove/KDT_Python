#실행: 컨트롤+쉬프트+F10
print("hello pycharm") #ctrl shift f10

#변수
PI=3.141592

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

# 클래스
class Circle:
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return PI * self.radius * self.radius