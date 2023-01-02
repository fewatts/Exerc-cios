import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.available

plt.style.use('classic')

plt.rcParams['figure.figsize'] = (20,7)
d = pd.read_csv('train.csv')

#	PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
#0	1	0	3	Braund, Mr. Owen Harris	male	22.0	1	0	A/5 21171	7.2500	NaN	S
#1	2	1	1	Cumings, Mrs. John Bradley (Florence Briggs Th...	female	38.0	1	0	PC 17599	71.2833	C85	C
#2	3	1	3	Heikkinen, Miss. Laina	female	26.0	0	0	STON/O2. 3101282	7.9250	NaN	S
#3	4	1	1	Futrelle, Mrs. Jacques Heath (Lily May Peel)	female	35.0	1	0	113803	53.1000	C123	S
#4	5	0	3	Allen, Mr. William Henry	male	35.0	0	0	373450	8.0500	NaN	S

plt.plot(d.Age, '*-')
plt.title('Info de passageiros titanic')
plt.xlabel('Passageiro', size=14)
plt.ylabel('Idade', size=17)
plt.show()

d.Age.plot()
plt.xlabel('Passageiro')
plt.ylabel('Idade')
plt.show()

#Todos os dados no mesmo gráfico
d.plot()
plt.show()

plt.scatter(d.PassengerId, d.Age, color='b', marker='>')
plt.show()

d.Age.hist()
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.savefig('nome_fig.png', transparent=True)
plt.show()

d.Fare.hist()

d.Survived.hist()
plt.title('Survivors in titanic')
plt.ylabel('Number of survivors')
plt.xlabel('0: died/1: survived')
plt.show()

