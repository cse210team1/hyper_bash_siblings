from game.sprite import Sprite
from game.attack import Attack

class Fighter(Sprite):
    def __init__(self):
        super().__init__()
        self.__ground_speed = None
        self.__air_speed = None
        self.__damage_multiplier = None

        self.a_attack = None
        self.b_attack = None

        self.lives = 3
        self.damage = 0
        self.jumps = 0
    
    # setters
    def set_ground_speed(self, number):
        self.__ground_speed = number

    def set_air_speed(self, number):
        self.__air_speed = number

    def set_damage_multiplier(self, number):
        self.__damage_multiplier = number

    def set_a_attack(self, number):
        self.a_attack = Attack(number)

    def set_b_attack(self, number):
        self.b_attack = Attack(number)

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
