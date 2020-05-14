from packages.class_LeeJunO import T1
from packages.class_LeeJunO import T2  
from packages.class_LeeJunO import T3 
import packages.class_LeeJunO as packclass 

#T1 기존값
print("------------------------")
print("T1")
x1 = T1(8)
x1.getPredict()
print("--------------------------")
print("T2")
#T2 기존값
x2 = T2(5,7)
x2.getPredict()
print("--------------------------")
print("T3")
#T3 기존값
x3 = T3(6)
x3.getPredict()
print("--------------------------")
print("T4에 임의값")
# T4 임의값


x8 =packclass.T4() 
x9 = packclass.T4()
x10 = packclass.T4()


emp1 =x8.getPredict(4,6)
emp2 = x9.getPredict(5,7)
emp3 = x10.getPredict(1,4)
print("--------------------------")
#import pickle & pickle.load

import pickle

pickle.dump(x10,open("C:/Users/sundooedu/study_sdacademy_202004/20200513_pickle/pickle_LeeJunO.pkl","wb"))
x10_load = pickle.load(open("C:/Users/sundooedu/study_sdacademy_202004/20200513_pickle/pickle_LeeJunO.pkl","rb"))
print("pickle로 불러온 값")
x10_load.getPredict(7,10)
print("--------------------------")