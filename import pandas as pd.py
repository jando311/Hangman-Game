import pandas as pd 
import random

df = pd.read_csv ('words_and_def.csv')

random_row = df.sample (n=1)

random_word = random_row ['Word'].values[0]
random_definition = random_row ['Definition'].values[0]

print (f'Random word: {random_word}')
print (f'{random_definition}')

