import arcade


from game import constants
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.setup_game_action import SetupGameAction
from game import fighter_dicts
from game.handle_attacks_action import HandleAttacksAction

from game.stage import Stage
from game.director import Director
from game.player import Player
from game.display import Display
from factory import Factory


def main():

    
    factory = Factory()
    cast = factory.create_cast("menu_scene")
    script = factory.create_script("menu_scene")
    
    director = Director(constants.MAX_X, constants.MAX_Y, factory.physics_engine)
    director.direct_scene(cast, script)
    arcade.play_sound(arcade.load_sound("art/background.wav"))
    arcade.run()

if __name__ == "__main__":
    main()