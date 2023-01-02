import pandas as pd

carros = [7, 4, 3, 2, 8]

dias = pd.date_range('20220101', '20220101', periods=5)

vendedor = ['george', 'vagner', 'pedro', 'vagner', 'george']

df = pd.DataFrame({'vendas':carros, 'data':dias, 'vendedor':vendedor})

# vendas	    data	vendedor
#0	7	2022-01-01	george
#1	4	2022-01-01	vagner
#2	3	2022-01-01	pedro
#3	2	2022-01-01	vagner
#4	8	2022-01-01	george

pd.pivot_table(df, index='data', columns='vendedor', values='vendas', aggfunc='sum')

#vendedor	george	pedro	vagner
#data			
#2022-01-01	   15	   3	  6

