# Show the sales data where the rating is more than 2.5.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[(df['Ratings'] > 2.5)].iloc[:, -12:])


"""Output:
        Total_Purchases      Amount  Total_Amount Product_Category  \
0                     3  108.028757    324.086270         Clothing   
1                     2  403.353907    806.707815      Electronics   
3                     7  352.407717   2466.854021       Home Decor   
5                     4  296.291806   1185.167224      Electronics   
9                    10  397.611229   3976.112295       Home Decor   
...                 ...         ...           ...              ...   
293900                8   51.716857    413.734856      Electronics   
293903                6  443.329498   2659.976987       Home Decor   
293905                5  472.424060   2362.120301         Clothing   
293907                1  285.137301    285.137301      Electronics   
293909                1  120.834784    120.834784       Home Decor   

       Product_Brand Product_Type   Feedback Shipping_Method Payment_Method  \
0               Nike       Shorts  Excellent        Same-Day     Debit Card   
1            Samsung       Tablet  Excellent        Standard    Credit Card   
3         Home Depot        Tools  Excellent        Standard         PayPal   
5              Apple       Tablet       Good         Express         PayPal   
9         Home Depot  Decorations  Excellent        Standard           Cash   
...              ...          ...        ...             ...            ...   
293900       Samsung       Tablet  Excellent        Same-Day           Cash   
293903    Home Depot        Tools  Excellent         Express           Cash   
293905          Nike       Shorts  Excellent        Standard           Cash   
293907         Apple       Laptop  Excellent        Same-Day           Cash   
293909          IKEA    Furniture       Good        Standard           Cash   

       Order_Status  Ratings        products  
0           Shipped        5  Cycling shorts  
1        Processing        4      Lenovo Tab  
3        Processing        4   Utility knife  
5           Pending        4      Lenovo Tab  
9         Delivered        4         Candles  
...             ...      ...             ...  
293900      Shipped        5            iPad  
293903      Pending        5           Level  
293905    Delivered        4    Chino shorts  
293907   Processing        5         LG Gram  
293909      Shipped        4        TV stand  

[190712 rows x 12 columns]
"""
