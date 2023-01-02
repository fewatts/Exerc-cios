import pandas as pd
import numpy as np

datas = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=['var_A', 'var_B', 'var_C', 'var_D'])

df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'Python'
})

#              var_A	    var_B	    var_C	    var_D
#2020-01-01	0.314735	-0.016460	-0.726002	1.506078
#2020-01-02	1.116529	-1.678398	-0.715860	-0.305115
#2020-01-03	0.697863	-0.097429	0.303913	1.235793
#2020-01-04	-0.090675	-0.068427	-1.582859	0.808750
#2020-01-05	-0.065928	1.749190	1.445060	1.487379
#2020-01-06	1.413743	0.402841	-0.792987	-1.208566

#    A	    B      	C	D	E	        F
#0	1.0	2013-01-02	1.0	3	test	Python
#1	1.0	2013-01-02	1.0	3	train	Python
#2	1.0	2013-01-02	1.0	3	test	Python
#3	1.0	2013-01-02	1.0	3	train	Python

df1 = df.reindex(index=datas[0:4], columns=list(df.columns) + ['var_E'])

df1.loc[datas[0]:datas[1], 'var_E'] = 1

#	        var_A	        var_B   	var_C   	var_D	var_E
#2020-01-01	0.314735	-0.016460	-0.726002	1.506078	1.0
#2020-01-02	1.116529	-1.678398	-0.715860	-0.305115	1.0
#2020-01-03	0.697863	-0.097429	0.303913	1.235793	NaN
#2020-01-04	-0.090675	-0.068427	-1.582859	0.808750	NaN

df1.dtypes
df1.describe()

#var_A    float64
#var_B    float64
#var_C    float64
#var_D    float64
#var_E    float64
#dtype: object

#       	 var_A	    var_B	    var_C   	var_D	var_E
#count	4.000000	4.000000	4.000000	4.000000	2.0
#mean	0.509613	-0.465178	-0.680202	0.811376	1.0
#std	0.517078	0.809506	0.771717	0.797767	0.0
#min	-0.090675	-1.678398	-1.582859	-0.305115	1.0
#25%	0.213383	-0.492671	-0.940216	0.530284	1.0
#50%	0.506299	-0.082928	-0.720931	1.022271	1.0
#75%	0.802529	-0.055435	-0.460917	1.303364	1.0
#max	1.116529	-0.016460	0.303913	1.506078	1.0

