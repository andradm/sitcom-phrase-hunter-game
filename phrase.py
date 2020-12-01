# Create your Phrase class logic here.


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower() 


    def display(self, guesses):
        # It loops through every character in the phrase"
        for letter in self.phrase:
                if letter in guesses:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
        
        
   #This method needs to use user_guess and return True if correct, and False if incorrect
    def check_guess(self, guess):
        for letter in self.phrase:
            if guess == letter:
                return True
            elif guess != letter:
                return False


          
                    
            




         