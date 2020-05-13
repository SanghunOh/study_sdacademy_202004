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


# 네번째 클래스
class GetPredict4:
    def __init__(self, x1=0, x2=0):
        self.x1 = x1
        self.x2 = x2
    def result4(self):
        if(self.x1==0 or self.x1==0):
            return print('x1=', self.x1, ',' 'x2=', self.x2, ',', 'y=', self.x2*3)
        elif(self.x1==2):
            return print('x1=', self.x1,',' 'x2=', self.x2, ',', 'y=', self.x2*3-0.5)
        else:
            for i in range(2, self.x1):
                if(self.x1 % i ==0):
                   return print('x1=', self.x1, ',' 'x2=', self.x2, ',', 'y=', self.x2*3)
                else:
                    return print('x1=', self.x1,',' 'x2=', self.x2, ',', 'y=', self.x2*3-0.5)


  




