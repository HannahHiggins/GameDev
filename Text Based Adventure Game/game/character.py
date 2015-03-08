""" The Character Class """

import cclass

class Character():
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.char_level = 1
        self.current_exp = 0
        self.current_location = {"x-coord": 0, "y-coord":0}
        
        #character has a class
        self.char_class = cclass.Cclass()
    
    def get_exp_to_level(self):
        #something basic to start with
        self.exp_to_level = self.char_level * 400
    
    def add_exp(self, exp_to_add):
        #add exp to the char exp pool and check for level up
        self.exp_to_add = exp_to_add
        self.current_exp = self.current_exp + self.exp_to_add
        self.get_exp_to_level()
        if self.current_exp > self.exp_to_level:
            self.char_level = self.char_level + 1
            print("Congratulations, you are now Level " + str(self.char_level))
            self.current_exp = self.current_exp - self.exp_to_level
            self.get_exp_to_level()
            self.remaining_exp = self.exp_to_level - self.current_exp
            print(str(self.remaining_exp) + " Exp for next level!")
            #need to be able to deal with going up multiple levels at once
    
    def change_location(self, x_change, y_change):
        #uodates the characters location
        self.x_change = x_change
        self.y_change = y_change
        self.cur_x = self.current_location["x-coord"]
        self.cur_y = self.current_location["y-coord"]
        self.current_location["x-coord"] = self.cur_x + self.x_change
        self.current_location["y-coord"] = self.cur_y + self.y_change
        print("Location changed to: " + str(self.current_location))
      
if __name__ == "__main__":
    pass
    