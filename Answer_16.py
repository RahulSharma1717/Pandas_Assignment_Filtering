# Display the Sale of Bristol city in UK.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[(df['City'] == 'Bristol') & (df['Country'] == 'UK')])


"""Output:
        Transaction_ID  Customer_ID                 Name  \
4              4983775        27901        Debra Coleman   
17431          9144743        15774     William Williams   
29551          9857115        75659       Lindsay Taylor   
29746          4189323        25082          Mark Monroe   
29887          2882840        29953         Joseph Smith   
...                ...          ...                  ...   
293686         8987705        44352     Jason Mclaughlin   
293784         1124646        94256          Robert Wood   
293834         8489867        94949        Robert Harris   
293870         3676759        68278       Angela Bennett   
293892         3020146        35103  Christina Gutierrez   

                       Email       Phone                       Address  \
4        Charles30@gmail.com  9098267635     5813 Lori Ports Suite 269   
17431    Matthew79@gmail.com  5119343751          77837 Hamilton Light   
29551    Clinton20@gmail.com  9033257256     89997 Gary Isle Suite 908   
29746   Christian9@gmail.com  3902905445   53187 Lynn Corners Apt. 751   
29887     Morgan99@gmail.com  3953179119               300 Tyler Drive   
...                      ...         ...                           ...   
293686     Andre61@gmail.com  6625355901   956 Garcia Squares Apt. 632   
293784   Melinda45@gmail.com  4797094167            59353 Tina Prairie   
293834     Kathy69@gmail.com  3811394013           70255 Trujillo Dale   
293870     Kelly91@gmail.com  8648378905  838 Blake Motorway Suite 020   
293892    Edward62@gmail.com  3378877797    7261 Walters Oval Apt. 778   

           City    State  Zipcode Country  Age  Gender  Income  \
4       Bristol  England    48704      UK   22    Male     Low   
17431   Bristol  England    91291      UK   19    Male  Medium   
29551   Bristol  England    81809      UK   22    Male    High   
29746   Bristol  England    78988      UK   22  Female    High   
29887   Bristol  England    64410      UK   22  Female    High   
...         ...      ...      ...     ...  ...     ...     ...   
293686  Bristol  England    13793      UK   26    Male    High   
293784  Bristol  England    77134      UK   46    Male  Medium   
293834  Bristol  England    57743      UK   47  Female     Low   
293870  Bristol  England    28916      UK   42  Female     Low   
293892  Bristol  England    33441      UK   69    Male  Medium   

       Customer_Segment        Date  Year     Month      Time  \
4               Premium  01-10-2024  2024   January  16:54:07   
17431               New   6/20/2023  2023      June  05:28:35   
29551           Regular  10/23/2023  2023   October  03:24:07   
29746           Regular  04-04-2023  2023     April  21:42:19   
29887           Regular  12/15/2023  2023  December  08:46:27   
...                 ...         ...   ...       ...       ...   
293686          Premium   8/16/2023  2023    August  16:09:14   
293784              New  02-11-2024  2024  February  22:42:38   
293834          Premium   2/13/2024  2024  February  09:42:40   
293870          Premium  02-08-2024  2024  February  19:01:58   
293892              New  08-05-2023  2023    August  22:51:35   

        Total_Purchases      Amount  Total_Amount Product_Category  \
4                     2  124.276524    248.553049          Grocery   
17431                 4  439.192681   1756.770722       Home Decor   
29551                 5  257.214437   1286.072187      Electronics   
29746                10  151.614823   1516.148230            Books   
29887                 7  191.439666   1340.077665            Books   
...                 ...         ...           ...              ...   
293686                4  334.203223   1336.812890          Grocery   
293784                2  125.281015    250.562029       Home Decor   
293834                8  389.720234   3117.761874            Books   
293870                3   87.824931    263.474794          Grocery   
293892                9   80.555426    724.998838          Grocery   

        Product_Brand Product_Type   Feedback Shipping_Method Payment_Method  \
4              Nestle    Chocolate        Bad        Standard           Cash   
17431            IKEA  Decorations       Good         Express         PayPal   
29551            Sony   Headphones        Bad        Same-Day           Cash   
29746    Random House   Literature        Bad        Standard           Cash   
29887   HarperCollins     Thriller        Bad        Same-Day           Cash   
...               ...          ...        ...             ...            ...   
293686      Coca-Cola   Soft Drink       Good         Express           Cash   
293784           IKEA  Decorations        Bad        Same-Day           Cash   
293834  Penguin Books   Children's  Excellent        Standard           Cash   
293870          Pepsi        Juice  Excellent        Same-Day           Cash   
293892      Coca-Cola        Water        Bad        Standard           Cash   

       Order_Status  Ratings             products  
4           Shipped        1    Chocolate cookies  
17431     Delivered        3   Decorative pillows  
29551     Delivered        1  Over-ear headphones  
29746     Delivered        1               Essays  
29887     Delivered        1              Mystery  
...             ...      ...                  ...  
293686      Shipped        3            Root beer  
293784   Processing        1             Wall art  
293834   Processing        5                Games  
293870      Shipped        4         Tomato juice  
293892      Pending        1        Coconut water  

[2137 rows x 30 columns]
"""