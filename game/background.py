import arcade
import arcade.gui

class Background:
       
    def __init__(self, color):
        self._color = color
        self._is_set = False

    def draw(self):
        if not self._is_set:
            arcade.set_background_color(self._color)
            self._is_set = True