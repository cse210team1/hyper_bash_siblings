import arcade


from game import constants
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.setup_game_action import SetupGameAction


from game.brick import Brick
from game.director import Director
from game.player import Player


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["player"] = []
    cast["player"].append(Player(600, 700))
    cast["player"].append(Player(300, 700))


    cast["bricks"] = []

    for x in range(184, 840, 64):
            brick = Brick(x,32)
            cast["bricks"].append(brick)
    
    # create the script {key: tag, value: list}
    script = {}
    damping = constants.DEFAULT_DAMPING
    gravity = (0, -constants.GRAVITY)
    physics_engine = arcade.PymunkPhysicsEngine(damping=damping, gravity=gravity)
    
    
    setup_game_action = SetupGameAction(physics_engine)
    control_actors_action = ControlActorsAction(physics_engine)
    move_actors_action = MoveActorsAction(physics_engine)
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction()
    
    script[Director.ON_SETUP] = [setup_game_action]
    script[Director.ON_KEY_PRESS] = [control_actors_action]
    script[Director.ON_UPDATE] = [move_actors_action, handle_collisions_action]
    script[Director.ON_DRAW] = [draw_actors_action]

    # start the game
    director = Director(constants.MAX_X, constants.MAX_Y, physics_engine)
    director.direct_scene(cast, script)
    director.on_setup()
    
    arcade.run()


if __name__ == "__main__":
    main()