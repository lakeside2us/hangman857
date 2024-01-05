import random

word_list = ['mango', 'grape', 'cherries', 'apple', 'plum']
word = random.choice(word_list)

class Hangman:
    
    # class constructor
    def __init__(self, word_list, num_lives = 5):
        
        # attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_', '_', '_', '_', '_']
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        
        # methods
    def check_guess(self, guess):
        guess = guess.lower()
        # self.guess = input('Enter a single letter ')
        if guess in self.word:
            print(f'Good guess! {guess} is in word.')
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
                    print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter} is not in the word.')
            print(f'You have {self.num_lives} left')
            self.list_of_guesses.append(guess)
            print(f'Letters guessed so far: {self.list_of_guesses}')
            
            
    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter ")
            if not (guess.isalpha() and len(guess) == 1):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                    print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guess.append(guess)
        ask_for_input(self)
    
    