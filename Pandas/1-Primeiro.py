import pandas as pd
import numpy as np

series = pd.Series([7, 4, 2, np.nan, 6, 9 ]) 

#Output:
#0    7.0
#1    4.0
#2    2.0
#3    NaN
#4    6.0
#5    9.0
#dtype: float64

type(series)

#Output: pandas.core.series.Series 

datas = pd.date_range('20190101', periods = 6, freq='D')

#Output: DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
#              '2019-01-05', '2019-01-06'],
#             dtype='datetime64[ns]', freq='D')

type(datas)

#Output: pandas.core.indexes.datetimes.DatetimeIndex

df = pd.DataFrame(np.random.randn(6,4), index = datas, columns = list('ABCD'))

np.random.randn(6,4)

#Output: array([[ 0.9074969 , -0.46746885, -1.16953991,  0.32219979],
#      [ 2.37172559, -1.35292015, -0.67086469,  0.73430025],
#      [ 0.98769182,  0.22471215, -0.11683735,  0.16073209],
#      [-1.42209804,  0.74975222,  0.77429943, -0.90773978],
#      [-1.35019293,  0.05216846,  0.27276518, -0.29304372],
#      [-1.23589524, -0.97351768,  1.41776575, -1.60738676]])

df = pd.DataFrame(np.random.randn(6,4), index = datas, columns = ['Teste', 'Pessoas', 'IA', 'Yeah'])

#OutPut: 	Teste	Pessoas	IA	Yeah
#2019-01-01	1.536758	-0.175004	0.418668	0.603794
#2019-01-02	1.190349	0.471640	-1.465663	-0.119803
#2019-01-03	-0.422298	1.069849	-0.798789	-1.786624
#2019-01-04	0.797185	-0.605738	-1.149086	1.566036
#2019-01-05	0.598063	0.496288	-1.358519	-0.449006
#2019-01-06	-0.321895	1.325904	-1.503625	-0.950643

type(df)

#Output: pandas.core.frame.DataFrame

from pandas.core.arrays import categorical
df2 = pd.DataFrame({'a':7,
                    'b': pd.Timestamp('20190101'),
                    'c': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'd': np.array([3] * 4, dtype='int32'),
                    'e': pd.Categorical(['test', 'train', 'test', 'train']),
                    'f': 'python'})
#Output: 
#a	b	c	d	e	f
#0	7	2019-01-01	1.0	3	test	python
#1	7	2019-01-01	1.0	3	train	python
#2	7	2019-01-01	1.0	3	test	python
#3	7	2019-01-01	1.0	3	train	python

df2.dtypes

#Output: a             int64
#b    datetime64[ns]
#c           float32
#d             int32
#e          category
#f            object
#dtype: object 
