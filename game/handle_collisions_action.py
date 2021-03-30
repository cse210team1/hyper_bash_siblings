import arcade
from game import constants
from game.action import Action


class HandleCollisionsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def __init__(self):

        pass

    def execute(self, cast, args, director):
        player_1 = cast["paddle"][0]
        player_2 = cast["paddle"][1]

        if player_1.collides_with_sprite(player_2):
            print("collided")

            if not player_1.a_attack_active and not player_1.b_attack_active and not player_2.a_attack_active and not player_2.b_attack_active:
                pass
                #no damage
                #no knockback
            elif player_1.a_attack_active and not player_2.a_attack_active and not player_2.b_attack_active:
                pass
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

