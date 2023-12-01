import pandas as pd 

df = pd.read_excel ('words_and_def.xlsx')

print (df.columns)

new_df = df.drop (columns = ['Unnamed: 0'])

print (new_df)

new_df.to_csv ('words_and_def.csv')

