import pandas as pd

cadastro_a = {'ID': ['AA2930', 'BB4563', 'CC2139', 'DE2521', 'GT3462', 'HH1158'],
              'Nome': ['Victor', 'Amanda', 'Bruna', 'Carlos', 'Ricardo', 'Marla'],
              'Idade': [20, 35, 40, 54, 30, 27],
              'Cep': ['9384-293', '2948-394', '0294-349', '0984-984', '9428-827', '9285-928']
              }
cadastro_a = pd.DataFrame(cadastro_a, columns = ['ID', 'Nome', 'Idade', 'Cep'])

#Out:
#       ID	 Nome  Idade	Cep
#0	AA2930	Victor	20	9384-293
#1	BB4563	Amanda	35	2948-394
#2	CC2139	Bruna	40	0294-349
#3	DE2521	Carlos	54	0984-984
#4	GT3462	Ricardo	30	9428-827
#5	HH1158	Marla	27	9285-928

cadastro_b = {'ID': ['CC9999', 'EF4488', 'DD9999', 'GT3462', 'HH1158'],
              'Nome': ['Marcos', 'Patrícia', 'Erika', 'Ricardo', 'Marla'],
              'Idade': [19, 30, 22, 30, 27],
              'Cep': ['7842-789', '9845-098', '0294-826', '0967-593', '0985-829']
              }
cadastro_b = pd.DataFrame(cadastro_b, columns = ['ID', 'Nome', 'Idade', 'Cep'])
cadastro_b


compras = {'Id': ['AA2930', 'EF4488', 'CC2139', 'EF448', 'CC9999', 'AA2930', 'HH1158', 'HH1158'],
           'Data': ['2022-01-01', '2022-03-04', '2022-10-04', '2022-07-05', '2022-03-18', '2022-05-22', '2021-12-31', '2022-10-30'],
           'Valor': ['300', '1498', '5000', '12599', '1856', '876253', '945493', '6837483']
          }
compras = pd.DataFrame(compras, columns = ['Id', 'Data', 'Valor'])
compras

#Out(compras):
#       Id	   Data	    Valor
#0	AA2930	2022-01-01	300
#1	EF4488	2022-03-04	1498
#2	CC2139	2022-10-04	5000
#3	EF448	2022-07-05	12599
#4	CC9999	2022-03-18	1856
#5	AA2930	2022-05-22	876253
#6	HH1158	2021-12-31	945493
#7	HH1158	2022-10-30	6837483


#pd.merge(Tabela_da_esqueda, Tabela_da_direita, on='coluna_coincidente', how='Left/Right/Inner/Outer')

#inner joins == interseção #Full == tudo em tudo, quase um append
#left join == interseção com lado esquerdo completo,
#right join == interseção com o lado direito completo

inner = pd.merge(cadastro_a, cadastro_b, how='inner', on='ID', suffixes=('__a', '__b'))
inner

#ID	Nome__a	Idade__a	Cep__a	Nome__b	Idade__b	Cep__b
#0	GT3462	Ricardo	30	9428-827	Ricardo	30	0967-593
#1	HH1158	Marla	27	9285-928	Marla	27	0985-829

pd.merge(cadastro_a, cadastro_b[['ID', 'Idade', 'Cep']], on=['ID'], how='inner', suffixes=('__a', '__b'))

#     ID    Nome  Idade__a	Cep__a	Idade__b	Cep__b
#0	GT3462	Ricardo	30	9428-827	30	0967-593
#1	HH1158	Marla	27	9285-928	27	0985-829

lojas = pd.concat([cadastro_a, cadastro_b], ignore_index=True)
lojas


#     ID	Nome	Idade	Cep
#0	AA2930	Victor	20	9384-293
#1	BB4563	Amanda	35	2948-394
#2	CC2139	Bruna	40	0294-349
#3	DE2521	Carlos	54	0984-984
#4	GT3462	Ricardo	30	9428-827
#5	HH1158	Marla	27	9285-928
#6	CC9999	Marcos	19	7842-789
#7	EF4488	Patrícia	9845-098
#8	DD9999	Erika	22	0294-826
#9	GT3462	Ricardo	30	0967-593
#10	HH1158	Marla	27	0985-829

lojas.drop_duplicates(subset='ID')

#ID	Nome	Idade	Cep
#0	AA2930	Victor	20	9384-293
#1	BB4563	Amanda	35	2948-394
#2	CC2139	Bruna	40	0294-349
#3	DE2521	Carlos	54	0984-984
#4	GT3462	Ricardo	30	9428-827
#5	HH1158	Marla	27	9285-928
#6	CC9999	Marcos	19	7842-789
#7	EF4488	Patrícia	9845-098
#8	DD9999	Erika	22	0294-826

esquerda = pd.merge(cadastro_a, compras, how='left', on=['ID'])

esquerda.groupby(['ID', 'Nome'])['Valor'].sum()

pd.merge(cadastro_a, cadastro_b, how='outer', on='ID', indicator='true')

#     ID	Nome_x	Idade_x	Cep_x	Nome_y	Idade_y	Cep_y	true
#0	AA2930	Victor	20.0	9384-293	NaN	NaN	NaN	left_only
#1	BB4563	Amanda	35.0	2948-394	NaN	NaN	NaN	left_only
#2	CC2139	Bruna	40.0	0294-349	NaN	NaN	NaN	left_only
#3	DE2521	Carlos	54.0	0984-984	NaN	NaN	NaN	left_only
#4	GT3462	Ricardo	30.0	9428-827	Ricardo	30.0	0967-593	both
#5	HH1158	Marla	27.0	9285-928	Marla	27.0	0985-829	both
#6	CC9999	NaN	NaN	NaN	Marcos	19.0	7842-789	right_only
#7	EF4488	NaN	NaN	NaN	Patrícia	30.0	9845-098	right_only
#8	DD9999	NaN	NaN	NaN	Erika	22.0	0294-826	right_only

