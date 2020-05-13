import pickle;
from single_xy import c_xy4;

test = c_xy4()
print(test.getPredict4(3,5))
print(test.getPredict4(5,10))

with open('XY4.pickle', 'rb') as ttp:
    testp = pickle.load(ttp)

print(testp.getPredict4(2,4))
print(testp.getPredict4(4,6))

