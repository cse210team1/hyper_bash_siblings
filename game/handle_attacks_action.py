import arcade
from game import constants
from game.action import Action


class HandleAttacksAction(Action):
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

        if director.f_pressed:
            player_1.a_attack_active = True
        elif director.v_pressed:
            player_1.b_attack_active = True

        if director.h_pressed:
            player_2.a_attack_active = True
        elif director.b_pressed:
            player_2.b_attack_active = True

        # add somethign for animations
