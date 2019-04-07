""" Check location for events """
import enemy
import character

def location_check(current_location):
    #check if a location has anything there
    for enemy in enemyList:
        if enemy.get_location() == character.current_location():
            print("An Enemy has appeared!")


if __name__ == "__main__":
   pass
