import random
import string

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
    
    def wordDifferentLetters(self, secretWord):
        self.differentLetters = []
        for letter in secretWord:
            if letter not in self.differentLetters:
                self.differentLetters.append(letter)
        return len(self.differentLetters)
        
        
    def newWord(self, secretWord, guesses):
        secret = secretWord
        differentNumber = self.wordDifferentLetters(secret)
        while differentNumber > guesses:
            print 'The old word was', secret
            print "Too hard to guess. Let's look for a new word"
            print '---------------------------------------------'
            secret = self.loadWord()
            differentNumber = self.wordDifferentLetters(secret)
        print 'There is '  , differentNumber, ' different letters'
        return secret

