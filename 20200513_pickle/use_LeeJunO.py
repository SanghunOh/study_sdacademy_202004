from packages_LeeJunO.class_LeeJunO import T1
from packages_LeeJunO.class_LeeJunO import T2  
from packages_LeeJunO.class_LeeJunO import T3 

x1 = T1(3)
x1.getPredict()

x2 = T2(1,3)
x2.getPredict()

x3 = T3(1)
x3.getPredict()

import pickle

pickle.dump(x2,open("./20200513_pickle/pickle_LeeJunO.pkl","wb"))
x2_load = pickle.load(open("pickle_LeeJunO.pkl","rb"))

x2_load.getPredict()