# Check the product brand and rating where home decor is purchased by paying via PayPal.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[(df['Payment_Method'] == 'PayPal') & (df['Product_Category'] == 'Home Decor'), ['Product_Category', 'Product_Brand', 'Payment_Method', 'Ratings']])


"""Output:
       Product_Category      Product_Brand Payment_Method  Ratings
3            Home Decor         Home Depot         PayPal        4
23           Home Decor  Bed Bath & Beyond         PayPal        3
35           Home Decor               IKEA         PayPal        4
43           Home Decor               IKEA         PayPal        5
50           Home Decor         Home Depot         PayPal        1
...                 ...                ...            ...      ...
267741       Home Decor               IKEA         PayPal        1
267803       Home Decor  Bed Bath & Beyond         PayPal        2
267901       Home Decor  Bed Bath & Beyond         PayPal        1
292518       Home Decor  Bed Bath & Beyond         PayPal        2
292527       Home Decor         Home Depot         PayPal        2

[10938 rows x 4 columns]
"""