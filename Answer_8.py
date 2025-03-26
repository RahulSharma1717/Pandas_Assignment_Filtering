# Check the product brands which has feedback as good.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[df['Feedback'] == 'Good', ['Product_Brand', 'Feedback']])


"""Output:
            Product_Brand Feedback
5                   Apple     Good
17                  Apple     Good
23      Bed Bath & Beyond     Good
26                Samsung     Good
29              Coca-Cola     Good
...                   ...      ...
293889              Pepsi     Good
293890               Zara     Good
293893      HarperCollins     Good
293899      Penguin Books     Good
293909               IKEA     Good

[92696 rows x 2 columns]
"""