class Test1() :
    def __init__(self,x):
        self.x = x        
    def getpredict(self):
        return print("Predict Result : ",self.x * 2)

class Test2() :
    def __init__(self,x):
        self.x = x
    def getpredict(self):
        return print("Predict Result : ",self.x*0.5+2)

class Test3() : 
    def __init__(self,x1,x2):
        self.x1 = x1
        self.x2 = x2
    def getpredict(self):
        return print("predict Result : ",self.x1+self.x2)