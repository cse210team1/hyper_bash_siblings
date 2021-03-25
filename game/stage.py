from game import constants

import arcade

class Stage(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(":resources:images/tiles/grassMid.png")
        self.center_x = x
        self.center_y = y


