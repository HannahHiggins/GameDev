""" The Character Class """

class Character():
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.char_level = 1
        self.current_exp = 0
    
    def exp_to_level(self):
        #something basic to start with
        self.exp_to_level = char_level * 400
    
    def add_exp(self, exp_to_add):
        #add exp to the char exp pool and check for level up
        self.exp_to_add = exp_to_add
        self.current_exp = self.current_exp + self.exp_to_add
        if self.current_exp > self.exp_to_level:
            self.char_level = self.char_level + 1
            print("Congratulations, you are now Level " + self.char_level)
            self.current_exp = self.current_exp - self.exp_to_level
            exp_to_level()
            self.remaining_exp = self.exp_to_level - self.current_exp
            print(self.remaining_exp + " Exp to go!")
            #need to be able to deal with going up multiple levels at once
      
    
    
if __name__ == "__main__":
    pass
    