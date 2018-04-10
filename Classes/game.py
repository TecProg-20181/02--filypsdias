import string
import os 

class Game():
    def __init__(self):
        self.guesses = 8
        self.secretWord = ""

    def welcomeMessage(self, secretWord):
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(secretWord), ' letters long.'
        print '-------------'

    def isWordGuessed(self):

        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True

    def getGuessedWord(self):
        self.guessed = ''
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                self.guessed += letter
            else:
                self.guessed += '_'
        return self.guessed

    def getAvailableLetters(self):
        self.available = string.ascii_lowercase
        return self.available

    def hangman(self, secretWord, guess):

        self.guesses = guess
        self.lettersGuessed = []
        self.secretWord = secretWord
        self.welcomeMessage

        while self.isWordGuessed() == False and self.guesses > 0:
            print 'You have ', self.guesses, 'guesses left.'

            self.available = self.getAvailableLetters()
            for letter in self.available:
                if letter in self.lettersGuessed:
                    self.available = self.available.replace(letter, '')

            print 'Available letters', self.available
            letter = raw_input('Please guess a letter: ').lower()
            if letter in self.lettersGuessed:

                self.guessed = self.getGuessedWord()

                print 'Oops! You have already guessed that letter: ' , self.guessed

            elif letter in secretWord:
                self.lettersGuessed.append(letter)

                self.guessed = self.getGuessedWord()

                print 'Good Guess: ', self.guessed

            else:
                self.guesses -=1
                self.lettersGuessed.append(letter)

                self.guessed = self.getGuessedWord()

                print 'Oops! That letter is not in my word: ', self.guessed
            print '-------------------------------------------------'

        else:
            if self.isWordGuessed() == True:
                os.system('clear')
                print secretWord, '!Congratulations, you won!'
            else:
                os.system('clear')
                print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'
    