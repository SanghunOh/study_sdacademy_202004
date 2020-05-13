#pickle
import pickle

# 1

from package.class_yoojeong import GetPredict1 as gp1
x0=gp1(0)
x0.result1()
x1=gp1(1)
x1.result1()
x2=gp1(2)
x2.result1()
x3=gp1(3)
x3.result1()
print('------------------------------------------------')
x6=gp1(6)
x6.result1()
print('------------------------------------------------')

pickle.dump(x6, open('./x6_class1.pkl', 'wb'))
print('pickle dump')
x6_class01_pkl=pickle.load(open('./x6_class1.pkl', 'rb'))
print('load pickle')
x6_class01_pkl.result1()

print('------------------------------------------------')


# 2
from package.class_yoojeong import GetPredict2 as gp2
a0=gp2(0)
a0.result2()
a1=gp2(1)
a1.result2()
a2=gp2(2)
a2.result2()
a3=gp2(3)
a3.result2()

print('------------------------------------------------')

a5=gp2(5)
a5.result2()

print('------------------------------------------------')
pickle.dump(a5, open('./a5_class2.pkl', 'wb'))
print('pickle dump')
a5_class02_pkl=pickle.load(open('./a5_class2.pkl', 'rb'))
print('load dump')
a5_class02_pkl.result2()
print('------------------------------------------------')

#3
from package.class_yoojeong import GetPredict3 as gp3
a02=gp3(0,2)
a02.result3()
a13=gp3(1,3)
a13.result3()
a24=gp3(2,4)
a24.result3()
a35=gp3(3,5)
a35.result3()
print('------------------------------------------------')
a46=gp3(4,6)
a46.result3()
a58=gp3(5,8)
a58.result3()

print('------------------------------------------------')
pickle.dump(a46, open('./a46_class3.pkl', 'wb'))
print('pickle dump')
a46_class03_pkl=pickle.load(open('./a46_class3.pkl', 'rb'))
a46_class03_pkl.result3()

pickle.dump(a58, open('./a58_class3.pkl', 'wb'))
print('pickle dump')
a58_class03_pkl=pickle.load(open('./a58_class3.pkl', 'rb'))
a58_class03_pkl.result3()


print('------------------------------------------------')

#4
from package.class_yoojeong import GetPredict4 as gp4
g46=gp4(4,6)
g46.result4()  # x1=4 이므로 소수 아님 -> y=x2*3
g57=gp4(5,7)
g57.result4() # x1=5 이므로 소수 -> y=x2*3-0.5

print('------------------------------------------------')
pickle.dump(g46, open('./g46_class4.pkl', 'wb'))
print('pickle dump')
g46_class04_pkl=pickle.load(open('./g46_class4.pkl', 'rb'))
print('load pickle')
g46_class04_pkl.result4()
print('------------------------------------------------')
pickle.dump(g57, open('./g57_class4.pkl', 'wb'))
print('pickle dump')
g57_class04_pkl=pickle.load(open('./g57_class4.pkl', 'rb'))
print('load pickle')
g57_class04_pkl.result4()


