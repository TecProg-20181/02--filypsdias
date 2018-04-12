from Classes.word import Word
from Classes.game import Game

secretWord = Word()
game = Game()

def guessNumber():
    while True:
        try:
            guesses = int(raw_input('How many guesses do you want?: '))
            break
        except ValueError:
            print "Sorry! Can't understand"
            print '----------------------------------------------'
    return guesses

secret = secretWord.loadWord().lower()
guesses = guessNumber()

secret = secretWord.newWord(secret, guesses)
game.hangman(secret, guesses)