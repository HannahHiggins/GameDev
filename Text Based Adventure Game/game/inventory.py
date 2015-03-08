""" The Inventory Class 
Basic Inventory - just a list of item names"""

class Inventory():
    def __init__(self,):
        self.inventory = []
    def add_item(self, item):
        self.inventory.append(item)  
        return("You found a new item!")          
        
if __name__ == "__main__":
   pass