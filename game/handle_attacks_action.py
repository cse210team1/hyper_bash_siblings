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

    def __init__(self, cast):
        self.player_1 = cast["player"][0]
        self.player_2 = cast["player"][1]


    def execute(self, cast, args, director):
        if director.f_pressed:
            self.player_1.successive_a_attack_frames += 1
            if self.player_1.successive_a_attack_frames <= 40:
                self.player_1.a_attack_active = True
            else:
                self.player_1.a_attack_active = False
        elif director.f_pressed == False:
            self.player_1.a_attack_active = False
            self.player_1.successive_a_attack_frames = 0
                
        if director.v_pressed == True and director.f_pressed == False:
            if self.player_1.successive_b_attack_frames <= 15:
                self.player_1.b_attack_active = True
            else:
                self.player_1.b_attack_active = False
            self.player_1.successive_b_attack_frames += 1
        elif director.v_pressed == False:
            self.player_1.b_attack_active = False
            self.player_1.successive_b_attack_frames = 0
        

        if director.h_pressed:
            self.player_2.successive_a_attack_frames += 1
            if self.player_2.successive_a_attack_frames <= 40:
                self.player_2.a_attack_active = True
            else:
                self.player_2.a_attack_active = False
        elif director.h_pressed == False:
            self.player_2.a_attack_active = False
            self.player_2.successive_a_attack_frames = 0
                
        if director.b_pressed == True and director.h_pressed == False:
            if self.player_2.successive_b_attack_frames <= 15:
                self.player_2.b_attack_active = True
            else:
                self.player_2.b_attack_active = False
            self.player_2.successive_b_attack_frames += 1
        elif director.b_pressed == False:
            self.player_2.b_attack_active = False
            self.player_2.successive_b_attack_frames = 0
