import pandas as pd

df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})

#	A	B	C
#0	a	1	2
#1	b	3	4
#2	c	5	6

dfm = pd.melt(df, id_vars=['A'], value_vars=['B'])

#	A	variable	value
#0	a	B	1
#1	b	B	3
#2	c	B	5

pd.melt(df, id_vars=['A'], value_vars=['B', 'C'])

#	A	variable	value
#0	a	B	1
#1	b	B	3
#2	c	B	5
#3	a	C	2
#4	b	C	4
#5	c	C	6

pd.melt(df, id_vars=['A'], value_vars=['B', 'C'], var_name='Points', value_name='frequence')

#	A	Points	frequence
#0	a	B	1
#1	b	B	3
#2	c	B	5
#3	a	C	2
#4	b	C	4
#5	c	C	6

