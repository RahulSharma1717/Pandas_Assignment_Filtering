# Show the data where payment method is cash and total amount is greater than 300.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[(df['Payment_Method'] == 'Cash') & (df['Total_Amount'] > 300), ['Payment_Method', 'Total_Amount']])


"""Output:
       Payment_Method  Total_Amount
6                Cash    630.115295
8                Cash   2630.714413
9                Cash   3976.112295
14               Cash   1786.356235
17               Cash    419.360565
...               ...           ...
293903           Cash   2659.976987
293904           Cash   2384.717299
293905           Cash   2362.120301
293906           Cash    973.962984
293910           Cash   2382.233417

[60109 rows x 2 columns]
"""