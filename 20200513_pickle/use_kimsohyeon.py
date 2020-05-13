from packages.Class_kimsohyeon import Cal1 as C1
from packages.Class_kimsohyeon import Cal2 as C2
from packages.Class_kimsohyeon import Cal3 as C3

val1 = C1(4)
print("Predict Result :",val1.getPredict())

val2 = C2(4)
print("Predict Result :",val2.getPredict())

val3 = C3(4,6)
print("Predict Result :",val3.getPredict())


import pickle
pickle.dump(val1, open("./Pickle_kimsohyeon","wb"))
val1_pkl = pickle.load(open("./Pickle_kimsohyeon","rb"))
val1_pkl.getPredict()