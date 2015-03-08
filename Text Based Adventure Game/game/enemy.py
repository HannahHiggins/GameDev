""" Enemy Class - Inherits from Creature Class """
import creature

class Enemy(creature.Creature):
    def __new__(self, eclass):
        enemy_class = eclass
        super(creature, self).__init__(name)
    
    def get_location(self):
        print(creature.Creature.current_location())
        
if __name__ == "__main__":
   pass