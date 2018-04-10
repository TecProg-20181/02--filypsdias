from Classes.word import Word
from Classes.game import Game

secretWord = Word()
game = Game()

def guessNumber():
    while True:
        try:
            guesses = int(raw_input('Choose the number of guesses to play: '))
            break
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
            print '----------------------------------------------'
    print 'Cool you have', guesses, 'guesses'
    return guesses

secret = secretWord.loadWord().lower()
guesses = guessNumber()

secret = secretWord.newWord(secret, guesses)
game.hangman(secret, guesses)