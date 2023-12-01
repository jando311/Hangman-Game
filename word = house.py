import random 

word = 'house'
unknown_word = list (len(word)* '_')



random_index = random.randint (0, len(word)-1)
unknown_word [random_index] = word [random_index]
random_word_str = ''.join(unknown_word)

print (random_word_str)


