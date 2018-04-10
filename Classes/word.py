import random
import string
from sets import Set

WORDLIST_FILENAME = "TxtFiles/words.txt"

class Word():
    
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
        
    def newWord(self, secretWord, guesses):
        secret = secretWord
        differentNumber = Set(list(secret))
        while len(differentNumber) > guesses:
            print 'There is ', len(differentNumber),' different letters'
            print 'The old word was', secret
            print 'Looking for a new word'
            print '---------------------------------------------'
            secret = self.loadWord()
            differentNumber = Set(list(secret))
        print 'There is '  , len(differentNumber), ' different letters'
        return secret

