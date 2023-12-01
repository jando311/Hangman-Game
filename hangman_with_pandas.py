import pandas as pd 
import random 

 
df = pd.read_csv ('words_and_def.csv')


random_row = df.sample (n=1)


random_word = random_row ['Word'].values[0]
random_definition = random_row ['Definition'].values[0]
new_definition = random_definition.replace (random_word, len(random_word)*'*')

word = random_word
unknown_word = list(len(word)*'_')


guessed_letter = []
guessed_word = []


tries = 6 


def hangman_drawing (tries):
    drawing = ["""  
                    --------
                    |      |
                    |      O
                    |     /|\\
                    |      |
                    |     / \\
                    ---
               """,
               """
                    --------
                    |      |
                    |      O
                    |     /|\\
                    |      |
                    |     /
                    ---
                """,
                """
                    --------
                    |      |
                    |      O
                    |     /|\\
                    |      |
                    |
                    ---
                """,
                """
                    --------
                    |      |
                    |      O
                    |     /|
                    |      |
                    |
                    ---
                """,
                """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |
                    ---
                """,
                """
                    --------
                    |      |
                    |      
                    |      
                    |
                    |
                    ---
                """,
                """
                    --------
                    |      
                    |      
                    |      
                    |
                    |
                    ---
                """
                ] 
    return drawing [tries] 

print ("Let's play some Hangman")
print ("\n")
print (hangman_drawing(tries))
print ('\n')
hint = input ('Do you want a hint? (Yes/No): ')
lowercase_hint = hint.lower()

if lowercase_hint == ('yes'):
    if random_word in random_definition:
        print (new_definition)

    if random_word not in random_definition:
        print (random_definition)

if lowercase_hint == ('no'):
    print ('Good luck then')

while tries > 0 and guessed_word != word:
    print (tries)
    print (unknown_word) 
    guess = input ("Guess a letter or a word: ")


    if guess in guessed_letter and len(guess) == 1:
        print ("You already guessed,",guess,"try again") 
        continue 

    if guess in word and len(guess)==1 and guess.isalpha:
        print ("Congratulations",guess,"is in the word!")
        guessed_letter.append(guess) 
        print (hangman_drawing(tries))
        positions = [i for i, letter in enumerate (word) if letter == guess]
        for position in positions:
            unknown_word[position] = guess 
        continue
    

    if guess in guessed_word:
        print ("You already guessed,",guess,"try again") 
        continue 

    if guess != word and len(guess)==1 and guess.isalpha:
        print ("No,",guess,"is not in the word")
        tries -= 1
        guessed_letter.append(guess)
        print (hangman_drawing(tries))
        continue  


    if guess != word:
        print ("No,",guess,"is not the word")
        tries -= 1 
        guessed_word.append (guess)
        print (hangman_drawing(tries))
        continue 

    if guess == word: 
        break

if unknown_word == list (word) or guess == word:
    print ("Congratulations,",guess, "is the word!")
else:
    print ("You lost, the word was,",word,".")


