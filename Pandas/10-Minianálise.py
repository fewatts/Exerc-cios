import pandas as pd
df = pd.read_excel('Prova+Excel.xlsx')
print(df)

#       Produto   Venda      Unnamed: 2   1  \
#0    H7456916    290         NaN NaN   
#1    H9375185    400         NaN NaN   
#2    H6678964    420         NaN NaN   
#3    H2192354    380         NaN NaN   
#4    H9356582    430         NaN NaN   
#..        ...    ...         ...  ..   
#294  H6151130    260         NaN NaN   
#295  H6934826    320         NaN NaN   
#296  H7081867    430         NaN NaN   
#297  H7560040    250         NaN NaN   
#298  H1909982    240         NaN NaN   

#                                             Calcule:  
#0    Quantidade de vendas, soma do valor vendido e ...  
#1                                                  NaN  
#2                                                  NaN  
#3                                                  NaN  
#4                                                  NaN  
#..                                                 ...  
#294                                                NaN  
#295                                                NaN  
#296                                                NaN  
#297                                                NaN  
#298                                                NaN  

#[299 rows x 5 columns]

soma = df['Venda'].sum()
print(soma)

#119450

med = df['Venda'].mean()

#399.4983277591973

ouro = df[df.Venda > 350]
prata = df[df.Venda <= 350]

#ouro

print(prata)

#	Produto	   Venda	Unnamed: 2	1	Calcule:
#0	H7456916	290	NaN	NaN	Quantidade de vendas, soma do valor vendido e ...
#6	H6584776	200	NaN	NaN	NaN
#8	H5119127	350	NaN	NaN	NaN
#10	H3968958	200	NaN	NaN	NaN
#11	H1561973	260	NaN	NaN	NaN
#...	...	...	...	...	...
#290	H9357444	240	NaN	NaN	NaN
#294	H6151130	260	NaN	NaN	NaN
#295	H6934826	320	NaN	NaN	NaN
#297	H7560040	250	NaN	NaN	NaN
#298	H1909982	240	NaN	NaN	NaN
