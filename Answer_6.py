# Display the names and phone numbers of the customers from UK

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df[['Name', 'Phone', 'Country']].loc[df['Country'] == 'UK'])


"""Output:
                       Name       Phone Country
1               Kelsey Hill  6852899987      UK
4             Debra Coleman  9098267635      UK
10           Jonathan Eaton  2996714102      UK
11          Brianna Oconnor  9398168800      UK
12        Kristine Williams  1822767586      UK
...                     ...         ...     ...
293878           John Evans  8338193183      UK
293886         Shelby Hanna  1713510443      UK
293892  Christina Gutierrez  3378877797      UK
293901         Amber Fields  6472396785      UK
293908           Daniel Lee  9382530370      UK

[61398 rows x 3 columns]
"""