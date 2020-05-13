import classtest01.class_ahntaewoong as cal

cal1 = cal.test1()
cal1.getTest(3)
cal2 = cal.test2()
cal2.getTest(3)
cal3 = cal.test3()
cal3.getTest(3,5)
cal4 = cal.test4()
cal4.getTest(0,2)
import pickle
pickle.dump(cal1, open("./cal1.pkl", "wb"))
cal1_pkl = pickle.load(open("./cal1.pkl", "rb"))
pickle.dump(cal2, open("./cal2.pkl", "wb"))
cal2_pkl = pickle.load(open("./cal2.pkl", "rb"))
pickle.dump(cal3, open("./cal3.pkl", "wb"))
cal3_pkl = pickle.load(open("./cal3.pkl", "rb"))
pickle.dump(cal4, open("./cal4.pkl", "wb"))
cal4_pkl = pickle.load(open("./cal4.pkl", "rb"))

cal1_pkl.getTest(8)
cal2_pkl.getTest(7)
cal3_pkl.getTest(12,7)
cal4_pkl.getTest(10,8)
