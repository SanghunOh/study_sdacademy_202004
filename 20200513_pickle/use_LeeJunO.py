from packages.class_LeeJunO import T1
from packages.class_LeeJunO import T2  
from packages.class_LeeJunO import T3 
from packages.class_LeeJunO import T4 

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
print("T4")
# T4 기존값
x4 = T4(0,2)
x5 = T4(1,3)
x6 = T4(2,4)
x7 = T4(3,6)

x4.getPredict()
x5.getPredict()
x6.getPredict()
x7.getPredict()
print("--------------------------")
print("T4에 임의값")
# T4 임의값

x8 = T4(4,6)
x9 = T4(5,7)
x10 = T4(1,4)

x8.getPredict()
x9.getPredict()
x10.getPredict()
print("--------------------------")
#import pickle & pickle.load

import pickle

pickle.dump(x7,open("C:/Users/sundooedu/study_sdacademy_202004/20200513_pickle/pickle_LeeJunO.pkl","wb"))
x7_load = pickle.load(open("C:/Users/sundooedu/study_sdacademy_202004/20200513_pickle/pickle_LeeJunO.pkl","rb"))
print("pickle로 불러온 값")
x7_load.getPredict()
print("--------------------------")