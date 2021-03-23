from game.fighter import Fighter
from game.characters.fighter_numbers import zombie


class Zombie(Fighter):
    def __init__(self):
        super().__init__()
        self.set_ground_speed(zombie["ground_speed"])
        self.set_air_speed(zombie["air_speed"])
        self.set_damage_multiplier(zombie["damage_multiplier"])
        self.set_a_attack(zombie["a_attack"])
        self.set_b_attack(zombie["b_attack"])
