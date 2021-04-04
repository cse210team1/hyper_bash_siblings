from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        self.background = arcade.load_texture("art/backgroundColorGrass.png")

    def execute(self, cast, args, director):

        arcade.draw_lrwh_rectangle_textured(0, 0, constants.MAX_X, constants.MAX_Y, self.background)
        try:
            for paddle in cast["player"]:
                paddle.draw()
        except:
            pass
        try:
            for brick in cast["stage"]:
                brick.draw()
        except:
            pass
        try:
            for hud in cast["hud"]:
                hud.hud(cast)
        except:
            pass

        try:
            for paddle in cast["background"]:
                paddle.draw()
        except:
            pass
        try:
            for paddle in cast["start_button"]:
                paddle.draw()
        except:
            pass
        try:
            for paddle in cast["player_1"]:
                paddle.draw()
        except:
            pass
        try:
            for paddle in cast["player_2"]:
                paddle.draw()
        except:
            pass