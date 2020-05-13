
from package.class_yoojeong import GetPredict1 as gp1


import pickle
# pickle.dump(x0, open('./x0_class1.pkl', 'wb'))
# pickle.dump(x1, open('./x1_class1.pkl', 'wb'))
# pickle.dump(x2, open('./x2_class1.pkl', 'wb'))
# pickle.dump(x3, open('./x3_class1.pkl', 'wb'))
print('pickle dump')
x0_class01_pkl=pickle.load(open('./x0_class1.pkl', 'rb'))
x1_class01_pkl=pickle.load(open('./x1_class1.pkl', 'rb'))
x2_class01_pkl=pickle.load(open('./x2_class1.pkl', 'rb'))
x3_class01_pkl=pickle.load(open('./x3_class1.pkl', 'rb'))
print('load pickle')
x0_class01_pkl.result1()
x1_class01_pkl.result1()
x2_class01_pkl.result1()
x3_class01_pkl.result1()

from use_yoojeong import a0, a1, a2, a3
import pickle 
# pickle.dump(a0,open('./a0_class2.pkl', 'wb'))
# pickle.dump(a1,open('./a1_class2.pkl', 'wb'))
# pickle.dump(a2,open('./a2_class2.pkl', 'wb'))
# pickle.dump(a3,open('./a3_class2.pkl', 'wb'))

print('pickle dump')
a0_class02_pkl=pickle.load(open('./a0_class2.pkl', 'rb'))
a1_class02_pkl=pickle.load(open('./a1_class2.pkl', 'rb'))
a2_class02_pkl=pickle.load(open('./a2_class2.pkl', 'rb'))
a3_class02_pkl=pickle.load(open('./a3_class2.pkl', 'rb'))

print('load pickle')

a0_class02_pkl.result2()
a1_class02_pkl.result2()
a2_class02_pkl.result2()
a3_class02_pkl.result2()


from use_yoojeong import a46
import pickle
pickle.dump(a46, open('./a46_class3.pkl', 'wb'))
print('pickle dump')
a46_class03_pkl=pickle.load(open('./a46_class3.pkl', 'rb'))
print('load pickle')
a46_class03_pkl.result3()


