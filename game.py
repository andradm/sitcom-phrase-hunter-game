
import random

from phrase import Phrase


class Game:
   
    
    def __init__(self):
        self.missed = 0
        self.phrases = [
        Phrase("how the turntables"),
        Phrase("how you doing"),
        Phrase("I am awesome"),
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
     
    def game_over(self):
        if self.missed == 5:
            print("Oh no! You lost! :( ")
        elif self.active_phrase.check_complete(self.guesses) == True:
            print("Congratulations! You won!")

    def play_again(self):
        self.answer = input("Would you like to play again? y/n ").lower()
        if self.answer == "y":
           self.guesses = [" "]
           self.missed = 0
           self.active_phrase = random.choice(self.phrases)
           return self.start()
        elif self.answer == 'n':
            print("Ok, see you next time!")
        else:
            print("This is not a valid answer. Try again.")
            return self.start() 

    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"Number missed: {self.missed}")
            print("\n")
            Phrase.display(self.active_phrase, self.guesses)
            print("\n")

            user_guess = self.get_guess()

            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1

            self.game_over()
            
        self.play_again()
            
     
    
      
        

     

         




        
        
         
        
        
    

        
        
        

    
        
        