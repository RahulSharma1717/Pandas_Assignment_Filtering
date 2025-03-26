# Display sales data of Berlin state of Germany and New South Wales of Australia.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[(df['State'] == 'Berlin') & (df['Country'] == 'Germany') | (df['State'] == 'New South Wales') & (df['Country'] == 'Australia')].iloc[:, 6:10])


"""Output:
              City            State  Zipcode    Country
0         Dortmund           Berlin    77985    Germany
2          Geelong  New South Wales    75929  Australia
5         Brisbane  New South Wales    74430  Australia
7           Munich           Berlin    86862    Germany
8       Wollongong  New South Wales    39820  Australia
...            ...              ...      ...        ...
293897   Nuremberg           Berlin    91049    Germany
293902    Ballarat  New South Wales    99633  Australia
293904      Cairns  New South Wales    39837  Australia
293906  Townsville  New South Wales     4567  Australia
293907     Hanover           Berlin    16852    Germany

[95603 rows x 4 columns]
"""