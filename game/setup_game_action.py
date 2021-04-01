import arcade
from game import constants
from game.action import Action


class SetupGameAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_engine):
        self.physics_engine = physics_engine
        self.background_music = arcade.load_sound("background.wav")

    def execute(self, cast, args, director):
        self.physics_engine.add_sprite(cast["player"][0], friction=constants.PLAYER_FRICTION,  mass=constants.PLAYER_MASS, moment=arcade.PymunkPhysicsEngine.MOMENT_INF, collision_type="player",  max_horizontal_velocity=constants.PLAYER_MAX_HORIZONTAL_SPEED,  max_vertical_velocity=constants.PLAYER_MAX_VERTICAL_SPEED)
        self.physics_engine.add_sprite(cast["player"][1], friction=constants.PLAYER_FRICTION,  mass=constants.PLAYER_MASS, moment=arcade.PymunkPhysicsEngine.MOMENT_INF, collision_type="player",  max_horizontal_velocity=constants.PLAYER_MAX_HORIZONTAL_SPEED,  max_vertical_velocity=constants.PLAYER_MAX_VERTICAL_SPEED)
        self.physics_engine.add_sprite_list(cast["stage"], friction=constants.WALL_FRICTION,  collision_type="wall", body_type=arcade.PymunkPhysicsEngine.STATIC)
        arcade.play_sound(self.background_music)