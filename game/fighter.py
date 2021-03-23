from game.sprite import Sprite

class Fighter(Sprite):
    def __init__(self):
        super().__init__()
    
    def set_ground_speed(self, number):
        self.__ground_speed = number

    #etc...