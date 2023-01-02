import pandas as pd

d = pd.read_csv('iris.data')

#	5.1	3.5	1.4	0.2	Iris-setosa
#0	4.9	3.0	1.4	0.2	Iris-setosa
#1	4.7	3.2	1.3	0.2	Iris-setosa
#2	4.6	3.1	1.5	0.2	Iris-setosa
#3	5.0	3.6	1.4	0.2	Iris-setosa
#4	5.4	3.9	1.7	0.4	Iris-setosa

d.dtypes

#5.1            float64
#3.5            float64
#1.4            float64
#0.2            float64
#Iris-setosa     object
#dtype: object

d.shape

#(149, 5)

d.describe()

#	        5.1	        3.5	        1.4     	0.2
#count	149.000000	149.000000	149.000000	149.000000
#mean	5.848322	3.051007	3.774497	1.205369
#std	0.828594	0.433499	1.759651	0.761292
#min	4.300000	2.000000	1.000000	0.100000
#25%	5.100000	2.800000	1.600000	0.300000
#50%	5.800000	3.000000	4.400000	1.300000
#75%	6.400000	3.300000	5.100000	1.800000
#max	7.900000	4.400000	6.900000	2.500000

d.to_json('teste.json')

