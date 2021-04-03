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
from game.cast_guy import Cast_guy
from game.factory import Factory


def main():
    # cast_guy = Cast_guy()
    # cast_guy.make_cast()
    # #create the cast {key: tag, value: list}
    # cast = {}

    # cast["player"] = []
    # cast["player"].append(Player(fighter_dicts.bob, 300, 700))
    # cast["player"].append(Player(fighter_dicts.zombie, 600, 700))


    # cast["stage"] = []

    # for x in range(184, 840, 128):
    #         brick = Stage(x,32)
    #         cast["stage"].append(brick)
        
    # cast["hud"] = []
    # cast["hud"].append(Display())
    

    
    # # create the script {key: tag, value: list}
    # script = {}
    # damping = constants.DEFAULT_DAMPING
    # gravity = (0, -constants.GRAVITY)
    # physics_engine = arcade.PymunkPhysicsEngine(damping=damping, gravity=gravity)
    
    
    # setup_game_action = SetupGameAction(physics_engine)
    # move_actors_action = MoveActorsAction(physics_engine)
    # handle_collisions_action = HandleCollisionsAction(physics_engine)
    # draw_actors_action = DrawActorsAction()
    # handle_attacks_action = HandleAttacksAction()
    
    # script[Director.ON_SETUP] = [setup_game_action]
    # script[Director.ON_KEY_PRESS] = []
    # script[Director.ON_UPDATE] = [move_actors_action, handle_collisions_action, handle_attacks_action]
    # script[Director.ON_DRAW] = [draw_actors_action]

    #start the game
    factory = Factory()
    cast = factory.create_cast("menu_scene")
    script = factory.create_script("menu_scene")
    
    director = Director(constants.MAX_X, constants.MAX_Y, factory.physics_engine)
    director.direct_scene(cast, script)
    arcade.play_sound(arcade.load_sound("background.wav"))
    arcade.run()

    # director = Director(constants.MAX_X, constants.MAX_Y, physics_engine)
    # director.direct_scene(cast, script)
    # director.on_setup()
    
    # arcade.run()


if __name__ == "__main__":
    main()