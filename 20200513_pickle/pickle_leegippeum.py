# class_1

from class_1 import Class_1

c1 = Class_1()
c1.calculate()
print(c1.calculate())

import pickle

pickle.dump(c1, open("./c1.pkl", "wb"))
print('dump pickle')
c1_pkl = pickle.load(open("./c1.pkl", "rb"))
print('load pickle')
c1_pkl.calculate()
print(c1_pkl.calculate())


# class_2

from class_2 import Class_2

c2 = Class_2()
c2.calculate()
print(c2.calculate())

import pickle

pickle.dump(c2, open("./c2.pkl", "wb"))
print('dump pickle')
c2_pkl = pickle.load(open("./c2.pkl", "rb"))
print('load pickle')
c2_pkl.calculate()
print(c2_pkl.calculate())


# class_3

from class_3 import Class_3

c3 = Class_3()
c3.calculate()
print(c3.calculate())

import pickle

pickle.dump(c3, open("./c3.pkl", "wb"))
print('dump pickle')
c3_pkl = pickle.load(open("./c3.pkl", "rb"))
print('load pickle')
c3_pkl.calculate()
print(c3_pkl.calculate())
