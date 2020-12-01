# Create your Game class logic in here.
from phrase import Phrase
import random



class Game:
   
    def __init__(self):
        
        self.missed = 0
        self.phrases = [
        Phrase("I am the master of my own bladder"),
        Phrase("how you doing"),
        Phrase("You got it"),
        Phrase("we were on a break"), 
        Phrase("fish meat is practically a vegetable")
        ]
        self.active_phrase = random.choice(self.phrases)
        self.guesses = [" "]
        
    
    def welcome(self):
        print("===================================", "\n")
        print("  Welcome to Sitcom Phrase Hunter!", "\n")
        print("===================================")
    
    
    def get_guess(self):
        self.guess = input("Enter a letter: ")
        return self.guess

    def start(self):
        self.welcome()
        print(f"Number missed: {self.missed}")
        print("\n")
        Phrase.display(self.active_phrase, self.guesses)
        print("\n")
        user_guess = self.get_guess()
        self.guesses.append(user_guess)
        if self.active_phrase.check_guess(user_guess):
            print("YAY")
        else:
            print("Bummer!")
        
    

        
        
        

    
        
        