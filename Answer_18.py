# Display the sales of products of nike and adidas only.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[(df['Product_Brand'] == 'Nike') | (df['Product_Brand'] == 'Adidas')].iloc[:, -8:])


"""Output:
       Product_Brand Product_Type   Feedback Shipping_Method Payment_Method  \
0               Nike       Shorts  Excellent        Same-Day     Debit Card   
14            Adidas      T-shirt        Bad        Same-Day           Cash   
30            Adidas        Shoes       Good        Same-Day     Debit Card   
39            Adidas        Shoes  Excellent        Same-Day    Credit Card   
49            Adidas       Jacket    Average        Standard    Credit Card   
...              ...          ...        ...             ...            ...   
293879          Nike       Shorts        Bad         Express           Cash   
293885          Nike      T-shirt        Bad        Same-Day           Cash   
293897        Adidas      T-shirt  Excellent        Standard           Cash   
293905          Nike       Shorts  Excellent        Standard           Cash   
293908        Adidas       Jacket    Average         Express           Cash   

       Order_Status  Ratings        products  
0           Shipped        5  Cycling shorts  
14          Shipped        1      V-neck tee  
30          Pending        3   Running shoes  
39          Pending        4   Running shoes  
49          Pending        2         Peacoat  
...             ...      ...             ...  
293879      Pending        1    Chino shorts  
293885    Delivered        1       Plain tee  
293897   Processing        4  Scoop neck tee  
293905    Delivered        4    Chino shorts  
293908      Shipped        2           Parka  

[35406 rows x 8 columns]
"""