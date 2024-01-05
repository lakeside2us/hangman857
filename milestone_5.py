import random

computer_word_list = ['mango', 'grape', 'cherries', 'apple', 'plum']
computer_random_word = random.choice(computer_word_list)

class Hangman:
    '''
    This class is used to define the Hangman game.
    
    Attributes:
        computer_word_list (list): the list of words to be chosen from.
        num_lives (int): the number of trials allowed.
        computer_random_word (str): computer randomly chosen word.
        word_guessed (str): guesses made my the player.
        num_letters (int): number of letters in the computer randomly chosen word.
        list_of_guess (list): the list of guesses made by the player
    '''
    
    # class constructor
    
    def __init__(self, computer_word_list, num_lives =  5):
        
        # attributes
        self.computer_word_list = computer_word_list
        self.num_lives = num_lives
        self.computer_random_word = random.choice(computer_word_list)
        self.word_guessed = ['_' for letter in self.computer_random_word]
        self.num_letters = int(len(set(self.computer_random_word)))
        self.list_of_guesses = []
        # print(self.computer_random_word)
        
    # methods
    def check_guess(self, guess):
        '''
        This function is used to check if the player guess is the computer randomly chosen word.

        Args:
            guess (str): the letter guessed by the player
        '''
        
        guess = guess.lower()
        if guess in self.computer_random_word:
            print(f'Good guess! {guess} is in computer_random_word.')
            # Checking if letter guessed by the user is the secret word and returning list of guesses
            for index, letter in enumerate(self.computer_random_word):
                if letter == guess:
                    self.word_guessed[index] = letter
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(self.word_guessed)
            print('Sorry, letter is not in the word.')
            print(f'You have {self.num_lives} live(s) left')
            self.list_of_guesses.append(guess)
            
            
    def ask_for_input(self):
        '''
        This function is used to ask the player for a guess.
        '''
        while True:
            guess = input('Enter a single letter ')
            if not (guess.isalpha() and len(guess) == 1):
                #  letter = guess
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                    print('Oops! You already tried that letter!!')
                    break
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(computer_word_list):
    '''
        This is the function to play the Hangman game.

        Args:
            computer_word_list (str): the list of words.
        '''
    num_lives = 5
    game = Hangman(computer_word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('Sorry! You lost the game!!')
            secret_word = random.choice(computer_word_list)
            print(f'The mystery word is {secret_word}')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break
        
            
if __name__=="__main__":
    play_game(computer_word_list)