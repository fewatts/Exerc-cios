import pandas as pd

arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]

v = pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))

#Out: 
#MultiIndex([(1,  'red'),
#            (1, 'blue'),
#            (2,  'red'),
#           (2, 'blue')],
#           names=['number', 'color'])

