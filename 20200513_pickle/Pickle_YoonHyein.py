from Use_YoonHyein import s1
import pickle
pickle.dump(s1, open("./Pickle_Hyein.pkl","wb"))
yhiS1_pkl = pickle.load(open("./Pickle_Hyein.pkl","rb"))
yhiS1_pkl.getPredict()