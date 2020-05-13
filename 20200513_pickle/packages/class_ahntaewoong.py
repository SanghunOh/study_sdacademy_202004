class test1:
    def __init__(self, x=None):
        self.x = x
    def getTest(self,x):
        self.x = x
        self.y = x * 2
        print('Result : ', self.y)

class test2:
    def __init__(self, x=None):
        self.x = x
    def getTest(self,x):
        self.x = x
        self.y = x*0.5 + 2
        print('Result : ', self.y)

class test3:
    def __init__(self, x1=None, x2=None):
        self.x1 = x1
        self.x2 = x2
    def getTest(self,x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.y = x1 + x2
        print('Result : ', self.y)

class test4:
    def __init__(self, x1=None, x2=None):
        self.x1 = x1
        self.x2 = x2
    def getTest(self,x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.y = 0*x1 + 3*x2
        if self.y > 10:
            self.y = 0.25*x1 + 2.75*x2
        else:
            self.y
        print('Result : ', self.y)

