import arcade
from game import constants
from game.action import Action
import time


class HandleAttacksAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def __init__(self):

        pass

    def execute(self, cast, args, director):
        player_1 = cast["player"][0]
        player_2 = cast["player"][1]

        player_1_concurrent_attacking_frames = 0
        player_2_concurrent_attacking_frames = 0

        if director.f_pressed:
            if player_1_concurrent_attacking_frames <= 40:
                player_1.a_attack_active = True
            else:
                player_1.a_attack_active = False
            player_1_concurrent_attacking_frames += 1
            print(player_1_concurrent_attacking_frames)
        elif director.v_pressed:
            if player_1_concurrent_attacking_frames <= 15:
                player_1.b_attack_active = True
            else:
                player_1.b_attack_active = False
            player_1_concurrent_attacking_frames += 1

        if not director.f_pressed:
            player_1.a_attack_active = False
            player_1_concurrent_attacking_frames = 0
        if not director.v_pressed:
            player_1.b_attack_active = False
            player_1_concurrent_attacking_frames = 0
        

        if director.h_pressed:
            if player_2_concurrent_attacking_frames <= 40:
                player_2.a_attack_active = True
            else:
                player_2.a_attack_active = False
            player_2_concurrent_attacking_frames += 1
        elif director.b_pressed:
            if player_2_concurrent_attacking_frames <= 40:
                player_2.a_attack_active = True
            else:
                player_2.a_attack_active = False
            player_2_concurrent_attacking_frames += 1

        if not director.h_pressed:
            player_2.a_attack_active = False
            player_2_concurrent_attacking_frames = 0
        if not director.b_pressed:
            player_2.b_attack_active = False
            player_2_concurrent_attacking_frames = 0
