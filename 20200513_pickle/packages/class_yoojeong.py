# 첫 번째 클래스
class GetPredict1:
    def __init__(self, x=0):
        self.x = x
    def result1(self):
        print("x=", self.x, ", " , "y=", self.x *2)

# 두 번째 클래스
class GetPredict2:
    def __init__(self, x=0):
        self.x = x
    def result2(self):
        print('x=', self.x, ',', 'y=', self.x*0.5+2)

# 세 번째 클래스
class GetPredict3:
    def __init__(self, x1=0, x2=0):
        self.x1 = x1
        self.x2 = x2
    def result3(self):
        print('x1=',self.x1, ',', 'x2=',self.x2, ',', 'y=', self.x1+self.x2)


