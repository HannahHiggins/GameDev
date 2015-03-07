""" Enemy Class - Inherits from Creature Class """

class enemy(creature):
    def __new__(self, eclass):
        enemy_class = eclass
        super(creature, self).__init__(name)
        
if __name__ == "__main__":
   pass