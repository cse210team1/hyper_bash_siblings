import arcade

from menu.start_game_action import StartGameAction
from menu.button import Button
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
from arcade.gui import UIManager


class Factory:


    def __init__(self):
        damping = constants.DEFAULT_DAMPING
        gravity = (0, -constants.GRAVITY)
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=damping, gravity=gravity)
        self.player_1_choice = None
        self.player_2_choice = None
        self.cast = {}
        #self.ui_manager = UIManager()

    def create_cast(self, scene):
        self.cast = {}
        
        if scene == "menu_scene":
            

            self.cast["start_button"] = [Button("Start Game", 650, 100, 200, 50)]

            self.cast["player_1"] = []
            self.cast["player_1"].append(Button("BOB", 325, 200, 200, 50))
            self.cast["player_1"].append(Button("ALICE", 325, 275, 200, 50))
            self.cast["player_1"].append(Button("ROBOT", 325, 350, 200, 50))
            self.cast["player_1"].append(Button("ZOMBIE", 325, 425, 200, 50))

            self.cast["player_2"] = []
            self.cast["player_2"].append(Button("BOB",  975, 200, 200, 50))
            self.cast["player_2"].append(Button("ALICE", 975, 275, 200, 50))
            self.cast["player_2"].append(Button("ROBOT", 975, 350, 200, 50))
            self.cast["player_2"].append(Button("ZOMBIE", 975, 425, 200, 50))

            self.cast["sprite_player"] = []
            # self.cast["sprite_player"].append(Player(self.player_1_choice, 300, 700))
             

            #self.ui_manager.add_ui_element(cast["player_2"][1])
            
        

        elif scene == "game_scene":
            print("Start making the cast!")
            self.cast["player"] = []
            self.cast["player"].append(Player(self.player_1_choice, 325, 600))
            self.cast["player"].append(Player(self.player_2_choice, 975, 600))


            self.cast["stage"] = []

            for x in range(184, 1160, 64):
                brick = Stage(x,32)
                self.cast["stage"].append(brick)
            
                
            self.cast["hud"] = []
            self.cast["hud"].append(Display())
            print("Finished making the cast")
            print(self.cast["player"][0].get_hit)
            print(self.cast["player"][1].jump_noise)
            
        return self.cast
            

    def create_script(self, scene):
        script = {}

        if scene == "menu_scene":
            script[Director.ON_MOUSE_RELEASE] = []
            script[Director.ON_MOUSE_RELEASE].append(StartGameAction(self))
            script[Director.ON_DRAW] = []
            script[Director.ON_DRAW].append(DrawActorsAction())
            

        elif scene == "game_scene":
            setup_game_action = SetupGameAction(self.physics_engine)
            move_actors_action = MoveActorsAction(self.physics_engine)
            handle_collisions_action = HandleCollisionsAction(self.physics_engine)
            draw_actors_action = DrawActorsAction()
            handle_attacks_action = HandleAttacksAction(self.cast)
            
            script[Director.ON_SETUP] = [setup_game_action]
            script[Director.ON_KEY_PRESS] = []
            script[Director.ON_UPDATE] = [move_actors_action, handle_collisions_action, handle_attacks_action]
            script[Director.ON_DRAW] = [draw_actors_action]
           
        return script

    def set_player_1(self, choice):
        self.player_1_choice = choice
        self.cast["sprite_player"].append(None)
        self.cast["sprite_player"][0] = Player(self.player_1_choice, 325, 600)

    def set_player_2(self, choice):
        self.player_2_choice = choice
        self.cast["sprite_player"].append(None)
        self.cast["sprite_player"][1] = Player(self.player_2_choice, 975, 600)

            