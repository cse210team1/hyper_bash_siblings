from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        for paddle in cast["player"]:
            paddle.draw()
        for brick in cast["stage"]:
            brick.draw()

        for hud in cast["hud"]:
            hud.hud(cast)
        