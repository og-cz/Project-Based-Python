import random

class Game:
    def __init__(self, tries=0):
        self._tries = tries
    
    def tries(self):
        self._tries += 1

    def get_tries(self):
        return self._tries

class Guess:
    guess = ['rock', 'paper', 'scissors']
  
    def randomize(self):
        return random.choice(self.guess)
    
    def get_guesses(self):
        return self.guess
