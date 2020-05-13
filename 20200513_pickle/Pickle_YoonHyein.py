from Use_YoonHyein import s1
import pickle
pickle.dump(s1, open("./yhiS1.pkl","wb"))
yhiS1_pkl = pickle.load(open("./yhiS1.pkl","rb"))
yhiS1_pkl.getPredict()