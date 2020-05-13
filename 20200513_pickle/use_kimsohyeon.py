from packages.class_kimsohyeon import Cal1 as C1
from packages.class_kimsohyeon import Cal2 as C2
from packages.class_kimsohyeon import Cal3 as C3

val1 = C1(4)
print("Predict Result (x=4) :",val1.getPredict())

val2 = C2(4)
print("Predict Result (x=4):",val2.getPredict())

val3 = C3(4,6)
print("Predict Result (x=4, y=6):",val3.getPredict())


import pickle
pickle.dump(val1, open("./pickle_kimsohyeon.pkl","wb"))
val1_pkl = pickle.load(open("./pickle_kimsohyeon.pkl","rb"))
print("Pickle import value :",val1_pkl.getPredict())