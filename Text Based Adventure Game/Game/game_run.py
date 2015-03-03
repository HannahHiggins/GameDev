""" Game main run sequence"""

def run_sequence():
    print("welcome to the text based game")
    name = raw_input("what is your name?")
    print("hello "+ name)
    char_class = raw_input("choose a class")
    
    if (char_class == "mage"):
        print("a good choice")
        
if __name__ == "__main__":
    run_sequence()