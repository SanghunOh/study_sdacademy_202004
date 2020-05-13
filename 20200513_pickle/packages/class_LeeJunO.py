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


class T4() :
    
    def __init__(self,x1,x2):
        self.x1 =x1
        self.x2 =x2        
    def getPredict(self):
        if(self.x1==0 or self.x1==1):
            return print("Predict Result : ",self.x2*3)
        elif(self.x1==2):
            return print("Predict Result : ",self.x2*3-0.5)
        else:
            for i in range(2,self.x1):      
                if(self.x1%i==0.0):
                    return print("Predict Result : ",self.x2*3)                    
                else:
                    return print("Predict Result : ",self.x2*3-0.5)            
       


 

        
            
    