import numpy as np
import pandas as pd

df = pd.DataFrame({'col1': ['A', 'A', 'B', np.nan, 'D', 'C'], 'col2': [2,1,9,8,7,4], 'col3': [0,1,9,4,2,3]})

#	col1	col2	  col3
#0	A	      2     	0
#1	A	      1	        1
#2	B	      9         9
#3	NaN       8	        4
#4	D	      7      	2
#5	C	      4     	3

df.sort_values(by=['col3'],ascending=False)

#	col1	col2	col3
#2	B      	9	      9
#3	NaN	    8	      4
#5	C	    4	      3
#4	D     	7	      2
#1	A	    1	      1
#0	A	    2         0

