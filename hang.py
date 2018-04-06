import random
import string

WORDLIST_FILENAME = "words.txt"

class word():
    
    def __init__(self):
        self.inFile = ""
        self.line = ""
        self.wordlist = ""

    def loadingMessage(self):
        print "Loading word list from file..."
        print "   ", len(self.wordlist), "words loaded."

    def loadWord(self):
        self.inFile = open(WORDLIST_FILENAME, 'r', 0)
        self.line = self.inFile.readline()
        self.wordlist = string.split(self.line)
        return random.choice(self.wordlist)


class game():
    def welcomeMessage(self, secretWord):
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(secretWord), ' letters long.'
        print '-------------'

    def wordDifferentLetters(self, secretWord):
        self.differentLetters = []
        for letter in secretWord:
            if letter not in self.differentLetters:
                self.differentLetters.append(letter)
        return len(self.differentLetters)

    def newWord(self, secretWord):
        if (self.wordDifferentLetters(secretWord)) > self.guesses:
            if raw_input('You are in the hard mode. Do you want a new random word? (Y/N): ').lower() == 'y':
                print 'New word selected!'
                secret = word()
                secretWord = secret.loadWord().lower()
            else:
                pass

    def isWordGuessed(self, secretWord, lettersGuessed):
        self.secretLetters = []

        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False

        return True

    def getGuessedWord(self, secretWord, lettersGuessed):
        self.guessed = ''
        for letter in secretWord:
            if letter in lettersGuessed:
                self.guessed += letter
            else:
                self.guessed += '_'
        return self.guessed

    def getAvailableLetters(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        self.available = string.ascii_lowercase

        return self.available

    def hangman(self, secretWord):
        self.guesses = 5
        self.lettersGuessed = []
        self.welcomeMessage(secretWord)
        self.wordDifferentLetters(secretWord)
        self.newWord(secretWord)

        while self.isWordGuessed(secretWord, self.lettersGuessed) == False and self.guesses > 0:
            print 'You have ', self.guesses, 'guesses left.'

            self.available = self.getAvailableLetters()
            for letter in self.available:
                if letter in self.lettersGuessed:
                    self.available = self.available.replace(letter, '')

            print 'Available letters', self.available
            letter = raw_input('Please guess a letter: ').lower()
            if letter in self.lettersGuessed:

                self.guessed = self.getGuessedWord(secretWord, self.lettersGuessed)
                print 'Oops! You have already guessed that letter: ', self.guessed.upper()

            elif letter in secretWord:
                self.lettersGuessed.append(letter)

                self.guessed = self.getGuessedWord(secretWord, self.lettersGuessed)
                print 'Good Guess: ', self.guessed.upper()

            else:
                self.guesses -=1
                self.lettersGuessed.append(letter)

                self.guessed = self.getGuessedWord(secretWord, self.lettersGuessed)

                print 'Oops! That letter is not in my word: ',  self.guessed.upper()
            print '------------'

        else:
            if self.isWordGuessed(secretWord, self.lettersGuessed) == True:
                print 'Congratulations, you won!'
            else:
                print 'Sorry, you ran out of guesses. The word was ', secretWord.upper(), '.'


secretWord = word()
secret = secretWord.loadWord().lower()
secretWord.loadingMessage()

game = game()
game = game.hangman(secret)


