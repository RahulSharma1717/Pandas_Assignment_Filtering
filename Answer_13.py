# Show the sales data of electronics of apple that are under process.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[(df['Order_Status'] == 'Processing') & (df['Product_Brand'] == 'Apple')].iloc[:, -12:])


"""Output:
        Total_Purchases      Amount  Total_Amount Product_Category  \
110                   1  171.262658    171.262658      Electronics   
115                   6  141.864984    851.189904      Electronics   
262                   3   43.071098    129.213293      Electronics   
444                   4  389.857402   1559.429610      Electronics   
506                   5   33.537473    167.687367      Electronics   
...                 ...         ...           ...              ...   
293700                7  334.315387   2340.207711      Electronics   
293785                9  416.173835   3745.564520      Electronics   
293804                1   66.471432     66.471432      Electronics   
293886                4   96.046489    384.185954      Electronics   
293907                1  285.137301    285.137301      Electronics   

       Product_Brand Product_Type   Feedback Shipping_Method Payment_Method  \
110            Apple   Smartphone        Bad        Standard         PayPal   
115            Apple       Laptop    Average         Express    Credit Card   
262            Apple   Smartphone    Average        Same-Day     Debit Card   
444            Apple       Laptop       Good        Standard     Debit Card   
506            Apple       Laptop  Excellent         Express           Cash   
...              ...          ...        ...             ...            ...   
293700         Apple       Tablet        Bad        Same-Day           Cash   
293785         Apple       Laptop       Good        Same-Day           Cash   
293804         Apple       Laptop       Good        Same-Day           Cash   
293886         Apple       Laptop    Average        Same-Day           Cash   
293907         Apple       Laptop  Excellent        Same-Day           Cash   

       Order_Status  Ratings            products  
110      Processing        1                LG G  
115      Processing        2         Razer Blade  
262      Processing        2              iPhone  
444      Processing        4             LG Gram  
506      Processing        4        Asus ZenBook  
...             ...      ...                 ...  
293700   Processing        1  Sony Xperia Tablet  
293785   Processing        4        Asus ZenBook  
293804   Processing        3     Lenovo ThinkPad  
293886   Processing        2             MacBook  
293907   Processing        5             LG Gram  

[3502 rows x 12 columns]
"""