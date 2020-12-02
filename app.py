# Import your Game class
from game import Game
from phrase import Phrase
# Create your Dunder Main statement.

if __name__ =='__main__':
    # Inside Dunder Main:
    ## Create an instance of your Game class
    
    
    def print_phrase(phrase_object):
        print(f'The phrase is: {phrase_object.phrase}')
    
    game = Game()
    game.start()
    
    
   
## Start your game by calling the instance method that starts the game loop
   