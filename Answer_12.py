# Show the purchases done by Benjamin Reed

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[df['Name'] == 'Benjamin Reed'])


"""Output:
        Transaction_ID  Customer_ID           Name                 Email  \
46732          4598086        64265  Benjamin Reed     Shawn10@gmail.com   
70256          9498817        10790  Benjamin Reed     Derek77@gmail.com   
284684         6748248        53041  Benjamin Reed  Kimberly98@gmail.com   
293861         6748248        53041  Benjamin Reed  Kimberly98@gmail.com   

             Phone                          Address           City  \
46732   6597818835     69752 Weiss Plains Suite 749     St. John's   
70256   3676064146  77901 Hernandez Burgs Suite 568        Chicago   
284684  4816508706      220 Jordan Shoals Suite 209  San Francisco   
293861  4816508706      220 Jordan Shoals Suite 209  San Francisco   

              State  Zipcode Country  Age  Gender  Income Customer_Segment  \
46732       Ontario    38264  Canada   20  Female     Low          Regular   
70256   Connecticut    36904     USA   20    Male  Medium          Premium   
284684         Iowa    51480     USA   39    Male     Low          Regular   
293861         Iowa    51480     USA   39    Male     Low          Regular   

              Date  Year   Month      Time  Total_Purchases      Amount  \
46732   08-05-2023  2023  August  17:04:08                4  227.246289   
70256   07-12-2023  2023    July  20:22:02                3  115.005248   
284684   6/22/2023  2023    June  21:18:01                7  206.997089   
293861   6/22/2023  2023    June  21:18:01                7  206.997089   

        Total_Amount Product_Category Product_Brand Product_Type Feedback  \
46732     908.985154          Grocery     Coca-Cola   Soft Drink      Bad   
70256     345.015743      Electronics         Apple   Smartphone     Good   
284684   1448.979625      Electronics       Samsung       Tablet  Average   
293861   1448.979625      Electronics       Samsung       Tablet  Average   

       Shipping_Method Payment_Method Order_Status  Ratings         products  
46732          Express           Cash    Delivered        1     Energy drink  
70256         Same-Day         PayPal    Delivered        3             LG G  
284684         Express    Credit Card   Processing        2  Acer Iconia Tab  
293861         Express           Cash   Processing        2             iPad  
"""