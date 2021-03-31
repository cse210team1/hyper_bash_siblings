import arcade
from game import constants
from game.action import Action


class HandleCollisionsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def __init__(self, physics_engine):
        self.physics_engine = physics_engine

    def execute(self, cast, args, director):
        player_1 = cast["player"][0]
        player_2 = cast["player"][1]

        if player_1.collides_with_sprite(player_2):
            

            if not player_1.a_attack_active and not player_1.b_attack_active and not player_2.a_attack_active and not player_2.b_attack_active:
                pass
                #no damage
                #no knockback
            elif player_1.a_attack_active and not player_2.a_attack_active and not player_2.b_attack_active:
                # an instant kill will be around 60k force and a basic around 12k  
                base_hit = constants.PLAYER_HIT_SIDE * 5 # Replace with damage later to figure knockback based on health
                hit_strength = base_hit * player_1.fighter_dict["a_attack"]
                force = (hit_strength, 0)
                self.physics_engine.apply_force(player_1, force)
                base_up = constants.PLAYER_HIT_UP * 7
                hit_up = base_up * player_1.fighter_dict["a_attack"]
                if hit_up > 1650:
                    hit_up = 1650
                # a instant kill is around 1600 total, base is around 225 for jump force. 
                impulse = (0, hit_up)
                print(hit_up)
                self.physics_engine.apply_impulse(player_1, impulse)
                #damage player 2
                #knockback player 2
            elif player_1.b_attack_active and not player_2.a_attack_active and not player_2.b_attack_active:
                
                pass
                #damage player 2
                #knockback player 2
            elif not player_1.a_attack_active and not player_1.a_attack_active and player_2.a_attack_active:
                pass
                #damage player 1
                #knockback player 2
            elif not player_1.a_attack_active and not player_1.a_attack_active and player_2.b_attack_active:
                pass
                #damage plauyer 1
                #knockback plauyer 1
            elif player_1.a_attack_active and player_2.a_attack_active:
                pass
                #damage both
                #no knockback
            elif player_1.a_attack_active and player_2.b_attack_active:
                pass
                #damage both
                #knockback playre 1
            elif player_1.b_attack_active and player_2.a_attack_active: 
                pass
                #damage both
                #knockback player 2
            elif player_1.b_attack_active and player_2.b_attack_active:
                pass
                #damage both
                # no knockback           

