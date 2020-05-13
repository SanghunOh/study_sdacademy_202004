import class_jay as cal

ex1 = cal.xy1(2)
ex1.getPredict()

ex2 = cal.xy2(3)
ex2.getPredict()

ex3 = cal.xxy1(4,6)

import pickle
pickle.dump(ex3, open("./pickle_jay.pkl","wb"))
ex_pkl = pickle.load(open("./pickle_jay.pkl","rb"))
ex_pkl.getPredict()

