

class Phrase:


    def __init__(self, phrase):
        self.phrase = phrase.lower() 

    def display(self, guesses):
        for letter in self.phrase:
                if letter in guesses:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
        
    def check_guess(self, guess):
        if len(guess) > 1 or guess.isalpha() == False:
            print("This is not a valid entry. Try again.")
            return False
        else:
            return guess in self.phrase  
    
    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True    
                
          


          
                    
            




         