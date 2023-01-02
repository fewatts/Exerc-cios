import pandas as pd

data = {
    "localização": ['cidadeA', 'cidadeB'],
    "Temperatura": ["prevista", "atual"],
    'out-2022': [30, 22],
    'set-2022':[45, 43],
    'nov-2022': [24, 22]
}
print(data)

#{'localização': ['cidadeA', 'cidadeB'], 'Temperatura': ['prevista', 'atual'], 'out-2022': [30, 22], 'set-2022': [45, 43], 'nov-2022': [24, 22]}

#Display: {'localização': ['cidadeA', 'cidadeB'],
# 'Temperatura': ['prevista', 'atual'],
# 'out-2022': [30, 22],
# 'set-2022': [45, 43],
# 'nov-2022': [24, 22]}

df = pd.DataFrame(data, columns=['localização', 'Temperatura', 'set-2022', 'out-2022', 'nov-2022'])

#    localização	Temperatura	set-2022	out-2022	nov-2022
#0	cidadeA	prevista	45	30	24
#1	cidadeB	atual	43	22	22

df2 = pd.melt(df, id_vars=['localização', 'Temperatura'], var_name='Date', value_name='Value')

#	localização	Temperatura	Date	Value
#0	cidadeA	prevista	set-2022	45
#1	cidadeB	atual	set-2022	43
#2	cidadeA	prevista	out-2022	30
#3	cidadeB	atual	out-2022	22
#4	cidadeA	prevista	nov-2022	24
#5	cidadeB	atual	nov-2022	22

