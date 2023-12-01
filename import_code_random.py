import pandas as pd 
import random 

## First, defining the DataFrame from where we want our Word to be
## choosen from 
df = pd.read_csv ('words_and_def.csv')

## Then we want the Program to only select Data from one single row
random_row = df.sample (n=1)


random_word = random_row ['Word'].values[0]
random_definition = random_row ['Definition'].values[0]

print (f'Random Word: {random_word}')
print (f'Random Definition: {random_definition}')