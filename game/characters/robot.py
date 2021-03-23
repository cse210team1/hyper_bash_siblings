from game.fighter import Fighter
from game.characters.fighter_numbers import robot


class Robot(Fighter):
    def __init__(self):
        super().__init__()
        self.set_ground_speed(robot["ground_speed"])
        self.set_air_speed(robot["air_speed"])
        self.set_damage_multiplier(robot["damage_multiplier"])
        self.set_a_attack(robot["a_attack"])
        self.set_b_attack(robot["b_attack"])
