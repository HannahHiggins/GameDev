""" Game main run sequence """
import character
import world
import random
import inventory

def run_sequence():
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

    print("Let us begin...")
    
    #initialise world
    pworld = world.World(random.randint(1,10))
    #initialise inventory
    pinventory = inventory.Inventory()
    
    print("Welcome to "+ pworld.world_name + ", a " + pworld.world_type + " world.")
    
    #scripted - for now
    new_item = "helm"
    
    print(pinventory.add_item(new_item))
    
    
        
if __name__ == "__main__":
    run_sequence()