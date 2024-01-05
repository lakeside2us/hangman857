import random

# Creating a list of favorites fruits
word_list = ['mango', 'grape', 'cherries', 'apple', 'plum']

# Generating a random fruit and assigning it to word variable
word = random.choice(word_list)
print(word)

# Creating a function to validate user's guess  
def check_guess(guess):
    
    guess = guess.lower()
    # guess = input('Enter a single letter ')
    
    while True:
        if len(guess) == 1 and guess.isalpha():
            break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
    return guess
    check_guess(guess)
    
 # Creating a function to check if user input is in computer random word
def ask_for_input():
    
    guess = input('Enter a single letter ')
    guess = guess.lower()
    
    if guess in word:
        print(f'Good guess! {guess} is in word.')
    
    else:
        print(f'Sorry, {guess} is not in the word')
        
ask_for_input()