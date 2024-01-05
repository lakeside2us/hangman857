import random

# Creating a list of favorites fruits

word_list = ['Mango', 'Banana', 'Watermelon', 'Apple', 'Orange']
print(word_list)

# Generating a random fruit and assigning it to word variable

word = random.choice(word_list)
print(word)

# Getting user input

guess = input('Enter a single letter ')
print(guess)

# Validating that the user input is single alphabet character

if len(guess) == 1 and guess.isalpha():
    print('Good guess') 
else:
    print('Oops! That is not a valid input')