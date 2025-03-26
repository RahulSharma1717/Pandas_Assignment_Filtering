# Show the rows of electronics sold by Samsung only.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[df['Product_Brand'] == 'Samsung', ['Product_Brand', 'Product_Category', 'Product_Type']])


"""Output:
       Product_Brand Product_Category Product_Type
1            Samsung      Electronics       Tablet
6            Samsung      Electronics   Television
26           Samsung      Electronics   Smartphone
33           Samsung      Electronics   Smartphone
52           Samsung      Electronics   Television
...              ...              ...          ...
293823       Samsung      Electronics   Smartphone
293861       Samsung      Electronics       Tablet
293874       Samsung      Electronics   Smartphone
293875       Samsung      Electronics       Tablet
293900       Samsung      Electronics       Tablet

[17866 rows x 3 columns]
"""