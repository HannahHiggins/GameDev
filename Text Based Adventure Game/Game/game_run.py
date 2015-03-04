""" Game main run sequence """
import character
import world
import random
import inventory
import movement

class run():
    def __init__(self):
        print("Welcome to the game")
        name = raw_input("What is your name?")
        print("Hello "+ name)
        char_class = raw_input("Choose a class")
    
        #initialise character
        self.pchar = character.Character(name, char_class)
    
        print(name + " the " + char_class)
    
        if (char_class == "Mage"):
            print("A good choice!")
        if (char_class == "Hunter"):
            print("A great choice!")
        else:
            print("Not a valid response (Mage or Hunter)")

        print("Let us begin...")
        
        #initialise world
        self.pworld = world.World(random.randint(1,10))
        #initialise inventory
        self.pinventory = inventory.Inventory()
        
        print("Welcome to "+ self.pworld.world_name + ", a " + self.pworld.world_type + " world.")
        
        #scripted - for now
        new_item = "helm"
        
        print(self.pinventory.add_item(new_item))
        
        #test
        print("You discovered a new area - gained 500 exp")
        self.pchar.add_exp(500)
    
        self.main_run()
    
    def main_run(self):
        command = raw_input("Where do you want to go?")
        x_change, y_change = movement.movement(command)
        self.pchar.change_location(x_change, y_change)
        #calls itself
        self.main_run()
        
if __name__ == "__main__":
    run()