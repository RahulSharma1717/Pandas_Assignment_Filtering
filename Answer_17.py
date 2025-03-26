# Display the data where ratings is either above 4 or below 2.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[(df['Ratings'] > 4) | (df['Ratings'] < 2)])


"""Output:
        Transaction_ID  Customer_ID                 Name  \
0              8691788        37249  Michelle Harrington   
4              4983775        27901        Debra Coleman   
6              5434096        97285           Erin Lewis   
7              2344675        26603        Angela Fields   
8              4155845        80175          Diane Clark   
...                ...          ...                  ...   
293901         9862022        99656         Amber Fields   
293902         5561211        35974          Jordan Hall   
293903         8961631        79479          Jason Welch   
293906         4246475        12104         Meagan Ellis   
293907         1197603        69772          Mathew Beck   

                       Email       Phone                         Address  \
0          Ebony39@gmail.com  1414786801               3959 Amanda Burgs   
4        Charles30@gmail.com  9098267635       5813 Lori Ports Suite 269   
6         Arthur76@gmail.com  1578355423     600 Brian Prairie Suite 497   
7          Tanya94@gmail.com  3668096144                 237 Young Curve   
8         Martin39@gmail.com  6219779557    8823 Mariah Heights Apt. 263   
...                      ...         ...                             ...   
293901    Donald38@gmail.com  6472396785  50022 Antonio Valley Suite 498   
293902     Holly86@gmail.com  2062575013                  806 Alan Flats   
293903     Jason36@gmail.com  6279294104                 764 Garcia Flat   
293906  Courtney60@gmail.com  7466353743          389 Todd Path Apt. 159   
293907  Jennifer71@gmail.com  5754304957               52809 Mark Forges   

              City            State  Zipcode    Country  Age  Gender  Income  \
0         Dortmund           Berlin    77985    Germany   21    Male     Low   
4          Bristol          England    48704         UK   22    Male     Low   
6        Kitchener          Ontario    47545     Canada   29  Female     Low   
7           Munich           Berlin    86862    Germany   29    Male  Medium   
8       Wollongong  New South Wales    39820  Australia   46    Male  Medium   
...            ...              ...      ...        ...  ...     ...     ...   
293901    Plymouth          England    92925         UK   43    Male  Medium   
293902    Ballarat  New South Wales    99633  Australia   61    Male  Medium   
293903    Hamilton          Ontario    61218     Canada   63    Male     Low   
293906  Townsville  New South Wales     4567  Australia   31    Male  Medium   
293907     Hanover           Berlin    16852    Germany   35  Female     Low   

       Customer_Segment        Date  Year      Month      Time  \
0               Regular   9/18/2023  2023  September  22:03:55   
4               Premium  01-10-2024  2024    January  16:54:07   
6                   New   6/26/2023  2023       June  13:35:51   
7               Premium   3/24/2023  2023      March  10:12:56   
8                   New  01-06-2024  2024    January  14:38:26   
...                 ...         ...   ...        ...       ...   
293901              New  03-05-2023  2023      March  14:47:57   
293902          Premium   2/14/2024  2024   February  00:13:52   
293903              New  09-06-2023  2023  September  17:37:41   
293906          Regular   1/20/2024  2024    January  23:40:29   
293907              New  12/28/2023  2023   December  02:55:45   

        Total_Purchases      Amount  Total_Amount Product_Category  \
0                     3  108.028757    324.086270         Clothing   
4                     2  124.276524    248.553049          Grocery   
6                     2  315.057648    630.115295      Electronics   
7                     1   46.588070     46.588070         Clothing   
8                     8  328.839302   2630.714413          Grocery   
...                 ...         ...           ...              ...   
293901                7   21.686500    151.805498          Grocery   
293902                7  343.066709   2401.466964       Home Decor   
293903                6  443.329498   2659.976987       Home Decor   
293906                5  194.792597    973.962984            Books   
293907                1  285.137301    285.137301      Electronics   

            Product_Brand Product_Type   Feedback Shipping_Method  \
0                    Nike       Shorts  Excellent        Same-Day   
4                  Nestle    Chocolate        Bad        Standard   
6                 Samsung   Television        Bad        Standard   
7                    Zara        Shirt        Bad        Same-Day   
8                  Nestle    Chocolate        Bad        Same-Day   
...                   ...          ...        ...             ...   
293901             Nestle    Chocolate        Bad         Express   
293902  Bed Bath & Beyond     Bathroom        Bad        Same-Day   
293903         Home Depot        Tools  Excellent         Express   
293906      Penguin Books      Fiction        Bad        Same-Day   
293907              Apple       Laptop  Excellent        Same-Day   

       Payment_Method Order_Status  Ratings            products  
0          Debit Card      Shipped        5      Cycling shorts  
4                Cash      Shipped        1   Chocolate cookies  
6                Cash   Processing        1             QLED TV  
7                Cash   Processing        1         Dress shirt  
8                Cash    Delivered        1      Dark chocolate  
...               ...          ...      ...                 ...  
293901           Cash      Pending        1    Chocolate mousse  
293902           Cash   Processing        1      Soap dispenser  
293903           Cash      Pending        5               Level  
293906           Cash   Processing        1  Historical fiction  
293907           Cash   Processing        5             LG Gram  

[90991 rows x 30 columns]
"""