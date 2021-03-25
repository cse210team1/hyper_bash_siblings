from game.sprite import Sprite
from game.attack import Attack

class Fighter(Sprite):
    def __init__(self, dictionary):
        super().__init__()
        self.__ground_speed = dictionary["ground_speed"]
        self.__air_speed = dictionary["air_speed"]
        self.__damage_multiplier = dictionary["damage_multiplier"]

        self.a_attack = Attack(dictionary["a_attack"])
        self.b_attack = Attack(dictionary["b_attack"])

        self.lives = 3
        self.damage = 0
        self.jumps = 0
    
    # getters
    def get_ground_speed(self):
        return self.__ground_speed

    def get_air_speed(self):
        return self.__air_speed

    def get_damage_multiplier(self):
        return self.__damage_multiplier

    # movement     # These moving methods can use velocity and move from Sprite, or something from the arcade physics engine
    def ground_move(self):
        pass

    def air_move(self):
        pass

    def jump(self):
        if self.jumps == 2:
            pass
        else:
            # jumping code
            jumps += 1
    
    def get_hit(self):
        pass
        # knockback code
        # update damage code

    # attacks
    def a_attack(self):
        pass

    def b_attack(self):
        pass

    # others
    def lose_life(self):
        self.lives -= 1

    def check_for_death(self):
        # check that fighter position is within limits
        # return bool
        pass

    def lose_match(self):
        if self.lives == 0:
            return True
        else:
            return False
