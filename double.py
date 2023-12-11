import pandas as pd


df1 = pd.read_csv('dataset_final.csv')
df2 = pd.read_csv('results.csv')



combined_df = pd.concat([df1, df2])


combined_df.to_csv('combined_file.csv')