""" The Character Class """

class Character():
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
    
if __name__ == "__main__":
    name = "default"
    char_class = "default"
    Character(name, char_class)
    