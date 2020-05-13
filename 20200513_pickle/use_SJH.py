from classTEST import First as fst
fst1 = fst()
from classTEST import Second as Snd
Snd1 = Snd()


import pickle
pickle.dump( fst1, open( "./SJH.pkl", "wb" ) )
print('dump pickle')
fst1_pkl = pickle.load( open( "./SJH.pkl", "rb" ) )
print('load pickle')

import pickle
pickle.dump( Snd1, open( "./SJH.pkl", "wb" ) )
print('dump pickle')
Snd1_pkl = pickle.load( open( "./SJH.pkl", "rb" ) )
print('load pickle')