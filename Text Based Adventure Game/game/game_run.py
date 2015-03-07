""" Game main run sequence """
import character
import world
import random
import inventory
import movement
import MySQLdb

#not very classy class
class run():
    def __init__(self):
        print("Welcome to the game")
        choice = raw_input("New Account or Existing Account?")
        if choice == "New":
            self.new_account()
        if choice == "Existing":
            existing_account()
        #else:
            #print("Not a valid response (New or Existing)")
    
    def new_account(self):
        account_username = raw_input("Enter Account Username")
        account_password = raw_input("Enter Account Password")
        account_email = raw_input("Enter Account Email")
        
        #access database
        db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="", db = "game")
        cur = db.cursor()
        cur.execute("INSERT INTO game_account (ACCOUNT_NAME, ACCOUNT_PASS, ACCOUNT_EMAIL) VALUES (%s, %s, %s)", (account_username, account_password, account_email))
        db.commit()
        db.close()
        
        new_char()
            
    def new_char(self):
        print('Create a new character!')
        username = raw_input("Enter Username")
        password = raw_input("Enter Password")
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
        
    def game_start(self):
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
