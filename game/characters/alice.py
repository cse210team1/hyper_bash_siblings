from game.fighter import Fighter
from game.characters.fighter_numbers import alice

class Alice(Fighter):
    def __init__(self):
        super().__init__()
        self.set_ground_speed(alice["ground_speed"])
        self.set_air_speed(alice["air_speed"])
        self.set_damage_multiplier(alice["damage_multiplier"])
        self.set_a_attack(alice["a_attack"])
        self.set_b_attack(alice["b_attack"])

    

        