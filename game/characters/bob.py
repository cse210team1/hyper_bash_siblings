from game.fighter import Fighter
from game.characters.fighter_numbers import bob


class Bob(Fighter):
    def __init__(self):
        super().__init__()
        self.set_ground_speed(bob["ground_speed"])
        self.set_air_speed(bob["air_speed"])
        self.set_damage_multiplier(bob["damage_multiplier"])
        self.set_a_attack(bob["a_attack"])
        self.set_b_attack(bob["b_attack"])
        
