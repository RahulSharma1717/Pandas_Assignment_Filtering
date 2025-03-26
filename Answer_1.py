# Display only customer ID, name, email, phone, and address columns of top 3 rows.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

df_new = df[['Customer_ID', 'Name', 'Email', 'Phone', 'Address']]
print(df_new.head(3))


"""Output:
   Customer_ID                 Name              Email       Phone  \
0        37249  Michelle Harrington  Ebony39@gmail.com  1414786801   
1        69749          Kelsey Hill   Mark36@gmail.com  6852899987   
2        30192         Scott Jensen  Shane85@gmail.com  8362160449   

              Address  
0   3959 Amanda Burgs  
1  82072 Dawn Centers  
2   4133 Young Canyon  
"""