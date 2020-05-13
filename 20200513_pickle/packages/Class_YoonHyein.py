class first:
    def __init__(self,x=0):
        self.y = x * 2
    def getPredict(self):
        print(self.y)

class second:
    def __init__(self, x1=0, x2=2):
        self.y = x1 + x2
    def getPredict(self):
        print(self.y)

class third:
    def __init__(self, x=0):
        self.y = 2 + (x*0.5)
    def getPredict(self):
        print(self.y)
