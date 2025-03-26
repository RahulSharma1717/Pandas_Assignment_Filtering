# Display the sales data of Nike only.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[df['Product_Brand'] == 'Nike'].iloc[:, -12:-6])


"""Output:
        Total_Purchases      Amount  Total_Amount Product_Category  \
0                     3  108.028757    324.086270         Clothing   
54                    4  129.756972    519.027890         Clothing   
62                    3   85.156932    255.470797         Clothing   
94                    3  427.594784   1282.784351         Clothing   
163                   9  457.292346   4115.631109         Clothing   
...                 ...         ...           ...              ...   
293853               10  256.627850   2566.278499         Clothing   
293865                5  132.897860    664.489301         Clothing   
293879               10  320.783426   3207.834257         Clothing   
293885               10   35.132928    351.329276         Clothing   
293905                5  472.424060   2362.120301         Clothing   

       Product_Brand Product_Type  
0               Nike       Shorts  
54              Nike        Shoes  
62              Nike        Shoes  
94              Nike       Shorts  
163             Nike       Shorts  
...              ...          ...  
293853          Nike        Shoes  
293865          Nike       Shorts  
293879          Nike       Shorts  
293885          Nike      T-shirt  
293905          Nike       Shorts  

[17646 rows x 6 columns]
"""