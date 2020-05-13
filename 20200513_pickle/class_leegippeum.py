# class_1

# # 방법 1
# # list라는 python의 기본 class를 불러와 그 기능을 상속받음
# # ? [0,1,2,3] 이외의 다른 새로운 데이터에 대해 수식이 돌아갈지 모르겠음 ?
# class Class_1_List(list):
#     def __init__(self, x):
#         list.__init__([])
#         self.x = x
# lee = Class_1_List('y = ')
# normelvar = 4
# lee.extend([0,1,2,3])
# for attr in lee:
#     print('y = ', attr * 2)


# 방법 2
# parameter 자리에 x만 넣어주고 y는 str으로 print
# x 라는 변수로 class_1() 을 인스턴스화 시켜줌
# () parameter 자리에 x 에 넣어주고 싶은 값들을 넣어줌
# 학습한 숫자 뿐만 아니라 다른 새로운 값들을 입력해줄때도 서비스 해줄 수 있어야 함


# class Class_1:
#     def __init__(self,x=0):
#         self.x = x
#     def calculate(self):
#         print('y = ', self.x*2) 
# a = Class_1()
# a.calculate()

class Class_1:
    def __init__(self,x=0):
        self.x = x
    def calculate(self):
        return self.x*2 
a = Class_1()
print('y = ', a.calculate())

class Class_2:
    def __init__(self, x=0):
        self.x = x
    def calculate(self):
        return 2+(self.x/2)
b = Class_2()
print('y = ', b.calculate())

class Class_3:
    def __init__(self, x=0):
        self.x = x
    def calculate(self):
        return self.x+(self.x+2)
c = Class_3()
print('y = ', c.calculate())
