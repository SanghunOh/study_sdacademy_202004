from classTEST import First as fst
fst1 = fst()
from classTEST import Second as Snd
Snd1 = Snd()
from classTEST import Third as Trd
Trd1 = Trd()
from classTEST import Third2 as Trdw
Trdw1 = Trdw()


import pickle
pickle.dump( fst1, open( "./SJH.pkl", "wb" ) )
print('dump pickle')
fst1_pkl = pickle.load( open( "./SJH.pkl", "rb" ) )
print('load pickle')

import pickle
pickle.dump( Snd1, open( "./SJH2.pkl", "wb" ) )
print('dump pickle')
Snd1_pkl = pickle.load( open( "./SJH2.pkl", "rb" ) )
print('load pickle')

import pickle
pickle.dump( Trd1, open( "./SJH3.pkl", "wb" ) )
print('dump pickle')
Trd1_pkl = pickle.load( open( "./SJH3.pkl", "rb" ) )
print('load pickle')

import pickle
pickle.dump( Trdw1, open( "./SJHw3.pkl", "wb" ) )
print('dump pickle')
Trdw1_pkl = pickle.load( open( "./SJHw3.pkl", "rb" ) )
print('load pickle')