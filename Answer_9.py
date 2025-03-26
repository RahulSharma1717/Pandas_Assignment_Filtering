# Check the product category with bad feedback.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

print(df.loc[df['Feedback'] == 'Bad', ['Product_Category', 'Feedback']].value_counts())


"""Output:
Product_Category  Feedback
Clothing          Bad         8599
Grocery           Bad         8449
Electronics       Bad         8399
Books             Bad         8379
Home Decor        Bad         8354
dtype: int64
"""
