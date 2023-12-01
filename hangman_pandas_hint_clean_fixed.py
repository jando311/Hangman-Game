import pandas as pd 
import random 
 
df = pd.read_csv ('words_and_def.csv')

def get_word (df):
    random_row = df.sample (n=1)
    random_word = random_row ['Word'].values[0]
    random_definition = random_row ['Definition'].values[0]
    new_definition = random_definition.replace (random_word, len(random_word)*'*')
    return random_word, random_definition, new_definition 

 
## list [word, definition, new definition] eg list [0,1,2]

list_input = get_word (df)
word = list_input [0]
unknown_word = list(len(word)*'_')
random_word = list_input [0]
random_definition = list_input [1]
new_definition = list_input [2]

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


def hangman_game_func (tries):
    while tries > 0 and guessed_word != word:
        print (tries)
        if tries == 3 and guessed_word != word:
            hint = input ('Do you want a hint? (Yes/No): ')
            lowercase_hint = hint.lower()
            if lowercase_hint == 'yes'and len (lowercase_hint) != 1:
                print (lowercase_hint)
    
            if random_word in random_definition:
                print ('Hint: ', new_definition)

            if random_word not in random_definition:
                print ('Hint: ', random_definition)

            if lowercase_hint == ('no') and len (lowercase_hint) != 1:
                print ('Good luck then')
            
        
        print (unknown_word) 
        guess = input ("Guess a letter or a word: ")


        if guess in guessed_letter and len(guess) == 1:
            print ("You already guessed,",guess,"try again") 
            continue 


        if guess in word and len(guess)==1 and guess.isalpha:
            guessed_letter.append(guess) 
            print (hangman_drawing(tries))
            print ("Congratulations",guess,"is in the word!")
            positions = [i for i, letter in enumerate (word) if letter == guess]
            for position in positions:
                unknown_word[position] = guess 
            continue
    

        if guess in guessed_word:
            print ("You already guessed,",guess,"try again") 
            continue 


        if guess != word and len(guess)==1 and guess.isalpha:
            tries -= 1
            guessed_letter.append(guess)
            print (hangman_drawing(tries))
            print ("No,",guess,"is not in the word")
            continue  


        if guess != word:
            tries -= 1 
            guessed_word.append (guess)
            print (hangman_drawing(tries))
            print ("No,",guess,"is not the word")
            continue
 

        if guess == word: 
            break
 

    if unknown_word == list (word) or guess == word:
        print ("Congratulations,",guess, "is the word!")
    else:
        print ("You lost, the word was,",word,".")

print (hangman_game_func (tries))

