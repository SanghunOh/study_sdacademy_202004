class T1() :
    def __init__(self,x):
        self.x = x        
    def getPredict(self):
        return print("Predict Result : ",self.x * 2)

class T2() :
    def __init__(self,x1,x2):
        self.x1 = x1
        self.x2 = x2       
    def getPredict(self):
        return print("Predict Result : ",self.x1 + self.x2)

class T3() :
    z = 2   
    def __init__(self,x):
        self.x =x           
    def getPredict(self):
        return print("Predict Result : ", T3.z + 0.5 * self.x )         


# class T4() :
#     z = 2
#     def __init__(self,x1,x2):
#         self.x1 =x1
#         self.x2 =x2        
#     def getPredict(self):
#         return print("Predict Result : ",z)
    