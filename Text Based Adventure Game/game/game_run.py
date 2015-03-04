""" Game main run sequence """
import character
import world
import random
import inventory
import movement


def intro():
    print("Welcome to the game")
    name = raw_input("What is your name?")
    print("Hello "+ name)
    char_class = raw_input("Choose a class")
    
    #initialise character
    pchar = character.Character(name, char_class)
    
    print(name + " the " + char_class)
    
    if (char_class == "Mage"):
        print("A good choice!")
    if (char_class == "Hunter"):
        print("A great choice!")
    else:
        print("Not a valid response (Mage or Hunter)")

    print("Let us begin...")
    
    #initialise world
    pworld = world.World(random.randint(1,10))
    #initialise inventory
    pinventory = inventory.Inventory()
    
    print("Welcome to "+ pworld.world_name + ", a " + pworld.world_type + " world.")
    
    #scripted - for now
    new_item = "helm"
    
    print(pinventory.add_item(new_item))
    
    #test
    print("You discovered a new area - gained 500 exp")
    pchar.add_exp(500)
    
    main_run(pchar)
    
def main_run(pchar):
    command = raw_input("Where do you want to go?")
    x_change, y_change = movement.movement(command)
    pchar.change_location(x_change, y_change)
    #calls itself
    main_run(pchar)
        
if __name__ == "__main__":
    intro()