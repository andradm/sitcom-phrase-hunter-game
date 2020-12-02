from phrase import Phrase
import random



class Game:
   
    def __init__(self):
        
        self.missed = 0
        self.phrases = [
        Phrase("I am the master of my own bladder"),
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
        elif Phrase.check_complete(self.active_phrase, self.guesses) == True:
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
        while self.missed < 5 and Phrase.check_complete(self.active_phrase, self.guesses) == False:
            print(f"Number missed: {self.missed}")
            print("\n")
            Phrase.display(self.active_phrase, self.guesses)
            print("\n")
            user_guess = self.get_guess()
            if len(user_guess) != 1 or user_guess.isalpha() == False:
                print("This is not a valid entry. Try again.")
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
            self.game_over()
        self.play_again()
            
     
    
      
        

     

         




        
        
         
        
        
    

        
        
        

    
        
        