import numpy as np
import pandas as pd

df = pd.DataFrame({'A': ['verdadeiro', 'falso', 'verdadeiro', 'falso',
                          'verdadeiro', 'falso', 'verdadeiro', 'falso'],
                   'B': ['um', 'um', 'dois', 'tres', 
                         'dois', 'dois', 'um', 'tres'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})


#	      A  	B	  C	             D
#0	verdadeiro	um	1.135895	-0.036206
#1	falso	    um	-0.516228	1.347409
#2	verdadeiro	dois -1.120560	0.082770
#3	falso	   tres  0.705163	-1.112318
#4	verdadeiro	dois	-0.540954	0.135520
#5	falso	   dois 	0.817735	0.299011
#6	verdadeiro	um	0.015882	-0.282298
#7	falso	  tres	-1.013585	1.699055


df.groupby(['A']).sum()

	
#A		     C	      D
#falso	-0.006915	2.233157
#verdadeiro	-0.509737	-0.100214

df.groupby(['A']).mean()

#A		     C	      D
#falso	-0.001729	0.558289
#verdadeiro	-0.127434	-0.025053


df.groupby(['A', 'B']).sum()


#A	     B		     c           d
#falso	dois	0.817735	0.299011
#        tres	-0.308422	0.586737
#        um	-0.516228	1.347409
#verdadeiro	dois	-1.661514	0.218290
#           um	1.151777	-0.318504

