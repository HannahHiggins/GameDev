""" The World Class """

class World():
    def __init__(self, rand_numb):
        #ganerates a random world type
        self.rand_numb = rand_numb
        self.world_name = "World " + str(rand_numb)
        if self.rand_numb == 1:
            self.world_type = "snowy"
        if self.rand_numb == 2:
            self.world_type = "subtropical"            
        if self.rand_numb == 3:
            self.world_type = "tropical"            
        if self.rand_numb == 4:
            self.world_type = "desert"            
        if self.rand_numb == 5:
            self.world_type = "temporate"            
        if self.rand_numb == 6:
            self.world_type = "forest"            
        if self.rand_numb == 7:
            self.world_type = "savanah"            
        if self.rand_numb == 8:
            self.world_type = "marshland"            
        if self.rand_numb == 9:
            self.world_type = "heathland"            
        if self.rand_numb == 10:
            self.world_type = "mountainous"            
        
if __name__ == "__main__":
   pass