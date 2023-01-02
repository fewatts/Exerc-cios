import pandas as pd
import numpy as np

dias = pd.date_range(start='20190101', periods=12)

#DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
#               '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08',
#               '2019-01-09', '2019-01-10', '2019-01-11', '2019-01-12'],
#              dtype='datetime64[ns]', freq='D')

pessoa = ['george', 'vitor', 'lucas']

np.random.choice(pessoa)

nome = []
gasto = []
for i in range(12):
  nome.append(np.random.choice(pessoa))
  gasto.append(np.round(np.random.rand() * 100,2))

#['vitor','george','george','vitor','vitor','vitor','george','lucas','george','lucas','george','lucas']
#[76.1,65.85,66.93,65.14,47.66,48.69,15.06,79.1,16.62,31.59,63.3,52.06]

df = pd.DataFrame({'dia':dias, 'nome':nome, 'gasto':gasto})

#	      dia	nome	gasto
#0	2019-01-01	vitor	76.10
#1	2019-01-02	george	65.85
#2	2019-01-03	george	66.93
#3	2019-01-04	vitor	65.14
#4	2019-01-05	vitor	47.66
#5	2019-01-06	vitor	48.69
#6	2019-01-07	george	15.06
#7	2019-01-08	lucas	79.10
#8	2019-01-09	george	16.62
#9	2019-01-10	lucas	31.59
#10	2019-01-11	george	63.30
#11	2019-01-12	lucas	52.06


df.pivot(index='dia', columns='nome', values='gasto')

#nome	george	lucas	vitor
#dia			
#2019-01-01	NaN	NaN	76.10
#2019-01-02	65.85	NaN	NaN
#2019-01-03	66.93	NaN	NaN
#2019-01-04	NaN	NaN	65.14
#2019-01-05	NaN	NaN	47.66
#2019-01-06	NaN	NaN	48.69
#2019-01-07	15.06	NaN	NaN
#2019-01-08	NaN	79.10	NaN
#2019-01-09	16.62	NaN	NaN
#2019-01-10	NaN	31.59	NaN
#2019-01-11	63.30	NaN	NaN
#2019-01-12	NaN	52.06	NaN


