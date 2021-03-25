import arcade
from game import constants
from game.action import Action


class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def __init__(self, physics_engine):
        self.physics_engine = physics_engine

    def execute(self, cast, args, director):
        pass