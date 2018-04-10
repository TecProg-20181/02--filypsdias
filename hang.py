from Classes.word import Word
from Classes.game import Game
from Classes.player import Player

secretWord = Word()
player = Player()
game = Game()

player.numberOfGuesses()

secret = secretWord.loadWord().lower()
guesses = player.getGuesses()

secret = secretWord.newWord(secret, guesses)
game.hangman(secret, guesses)