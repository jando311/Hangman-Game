import pandas as pd 
import random 
 
df = pd.read_csv ('words_and_def.csv')

def get_word (df):
    random_row = df.sample (n=1)
    random_word = random_row ['Word'].values[0]
    random_definition = random_row ['Definition'].values[0]
    new_definition = random_definition.replace (random_word, len(random_word)*'*')
    return random_word, random_definition, new_definition 

 

list_input = get_word (df)
word = list_input[0]
unknown_word = list(len(word)*'_')
random_word = list_input[0]
random_definition = list_input [1]
new_definition = list_input [2]

random_letter = random.choice (list_input [0])
guessed_letter = []
guessed_word = []

tries = 6 
hint_used = False 
hint_2_used = False 


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


def get_index (variable):
    positions = [i for i, letter in enumerate (word) if letter == variable]
    for position in positions:
        unknown_word[position] = variable

    
def hangman_game_func (tries):
    value = 0 
    while tries > 0 and guessed_word != word:
        print (tries)
        print (value)


        if value == 3 and not hint_used:
            hint = input ('Do you want a hint? (Y/N): ')
            lowercase_hint = hint.lower()

            if lowercase_hint == 'y' and len (lowercase_hint) == 1:
                if random_word in random_definition:
                    print ('Your hint is: ', new_definition)

                if random_word not in random_definition: 
                    print ('Your hint is: ', random_definition)

            elif lowercase_hint == 'n' and len (lowercase_hint) == 1:
                print ('Okay, good Luck!')

            elif lowercase_hint != 'n' or 'y':
                print ('Invalid input, please answer only with (Y/N)')
                continue

        if value == 4 and not hint_used: 
            hint_2 = input ('Do you want another hint? (Y/N): ')
            lowercase_hint_2 = hint_2.lower()

            if lowercase_hint_2 == 'y' and len (lowercase_hint_2) == 1:
                indexes_word = [i for i, value in enumerate (unknown_word) if value == '_']
                random_index = random.choice (indexes_word)
                get_index (word [random_index])

            elif lowercase_hint_2 == 'n' and len (lowercase_hint_2) == 1:
                print ('You are almost out of luck!')

            else:
                print ('Invalid input, please answer only with (Y/N)')
                continue
            
        
        print (unknown_word) 
        guess = input ("Guess a letter or a word: ")


        if guess in guessed_letter and len(guess) == 1:
            print ("You already guessed,",guess,"try again") 
            continue 


        if guess in word and len(guess)==1 and guess.isalpha:
            value -= 1
            guessed_letter.append(guess) 
            print (hangman_drawing(tries))
            print ("Congratulations",guess,"is in the word!")
            get_index (guess)
            continue
    

        if guess in guessed_word:
            print ("You already guessed,",guess,"try again") 
            continue 


        if guess != word and len(guess)==1 and guess.isalpha:
            tries -= 1
            value += 1
            guessed_letter.append(guess)
            print (hangman_drawing(tries))
            print ("No,",guess,"is not in the word")
            continue  


        if guess != word:
            tries -= 1
            value += 1
            guessed_word.append (guess)
            print (hangman_drawing(tries))
            print ("No,",guess,"is not the word")
            continue
 

        if guess == word: 
            break
 

    if unknown_word == list (word) or guess == word:
        print ("Congratulations,",guess, "is the word!")
        return True
    
    else:
        print ("You lost, the word was,",word,".")
        return False

result = hangman_game_func (tries)

if result: 
    print ('You won!')
else: 
    print ('Better luck next time.')



