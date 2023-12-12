import pandas as pd


data = pd.read_csv('updated_data.csv')

#
data['Math_Score'] = (data['math'] > 100).astype(int)


data.to_csv('Math_dummy.csv', index=False)