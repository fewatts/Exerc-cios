import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'Python',
    'G': [2,2,4,4],
    'H': [np.nan,2,4,np.nan]
})
 
#     A	       B	C	D	E    	F	    G	H
#0	1.0	2013-01-02	1.0	3	test	Python	2	NaN
#1	1.0	2013-01-02	1.0	3	train	Python	2	2.0
#2	1.0	2013-01-02	1.0	3	test	Python	4	4.0
#3	1.0	2013-01-02	1.0	3	train	Python	4	NaN

df.nunique(axis=1, dropna=True)

#0    6
#1    6
#2    6
#3    6
#dtype: int64

#	  A	        B	C	D	E	     F	    G	H
#0	1.0	2013-01-02	1.0	3	test	Python	2	NaN
#1	1.0	2013-01-02	1.0	3	train	Python	2	2.0
#2	1.0	2013-01-02	1.0	3	test	Python	4	4.0
#3	1.0	2013-01-02	1.0	3	train	Python	4	NaN

df.drop_duplicates(subset='G', keep=False)

#	A	B	C	D	E	F	G	H

