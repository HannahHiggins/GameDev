""" Game main run sequence """
import character

def run_sequence():
    print("welcome to the text based game")
    name = raw_input("what is your name?")
    print("hello "+ name)
    char_class = raw_input("choose a class")
    
    #initialise character
    pchar = character.Character(name, char_class)
    
    print(name + " the " + char_class)
    
    if (char_class == "Mage"):
        print("a good choice")
    if (char_class == "Hunter"):
        print("a great choice")
        
if __name__ == "__main__":
    run_sequence()