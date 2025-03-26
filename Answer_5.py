# Display the data of clothing product category only.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.iloc[:, 10:22].loc[df['Product_Category'] == 'Clothing'])


"""Output:
        Age  Gender  Income Customer_Segment        Date  Year      Month  \
0        21    Male     Low          Regular   9/18/2023  2023  September   
7        29    Male  Medium          Premium   3/24/2023  2023      March   
14       32  Female    High          Regular  11/18/2023  2023   November   
30       26  Female     Low          Regular  02-06-2024  2024   February   
36       19    Male    High          Regular  12-12-2023  2023   December   
...     ...     ...     ...              ...         ...   ...        ...   
293885   60  Female    High          Premium  11/18/2023  2023   November   
293890   27    Male     Low          Premium   6/16/2023  2023       June   
293897   30  Female    High          Premium  09-09-2023  2023  September   
293905   54    Male    High              New  10/14/2023  2023    October   
293908   41    Male     Low          Premium   2/27/2024  2024   February   

            Time  Total_Purchases      Amount  Total_Amount Product_Category  \
0       22:03:55                3  108.028757    324.086270         Clothing   
7       10:12:56                1   46.588070     46.588070         Clothing   
14      23:41:05                6  297.726039   1786.356235         Clothing   
30      01:59:20                3  159.804193    479.412580         Clothing   
36      17:48:31                5  195.551403    977.757015         Clothing   
...          ...              ...         ...           ...              ...   
293885  17:00:15               10   35.132928    351.329276         Clothing   
293890  14:31:46               10  172.957370   1729.573700         Clothing   
293897  14:15:43                2   51.469204    102.938408         Clothing   
293905  15:06:09                5  472.424060   2362.120301         Clothing   
293908  02:43:49                3   60.701761    182.105285         Clothing   

[53282 rows x 12 columns]
"""