from game.action import Action
from game import fighter_dicts


class StartGameAction(Action):
    
    def __init__(self, factory):
        self._factory = factory
        

    def execute(self, cast, args, director):
        print("We are starting to start game thing")
        if "start_button" in cast.keys():
            print("First if statement")
            start_button = cast["start_button"][0]
            player_1_bob = cast["player_1"][0]
            player_1_alice = cast["player_1"][1]
            player_1_robot = cast["player_1"][2]
            player_1_zombie = cast["player_1"][3]

            player_2_bob = cast["player_2"][0]
            player_2_alice = cast["player_2"][1]
            player_2_robot = cast["player_2"][2]
            player_2_zombie = cast["player_2"][3]

            point = (args["x"], args["y"])
            
            if start_button.collides_with_point(point):
                if self._factory.player_1_choice != None and self._factory.player_2_choice != None:
                    cast = self._factory.create_cast("game_scene")
                    script = self._factory.create_script("game_scene")
                    director.direct_scene(cast, script)
                    director.on_setup()

            elif player_1_bob.collides_with_point(point):
                self._factory.set_player_1(fighter_dicts.bob)

            elif player_1_alice.collides_with_point(point):
                self._factory.set_player_1(fighter_dicts.alice)

            elif player_1_robot.collides_with_point(point):
                self._factory.set_player_1(fighter_dicts.robot)

            elif player_1_zombie.collides_with_point(point):
                self._factory.set_player_1(fighter_dicts.zombie)



            elif player_2_bob.collides_with_point(point):
                self._factory.set_player_2(fighter_dicts.bob)

            elif player_2_alice.collides_with_point(point):
                self._factory.set_player_2(fighter_dicts.alice)

            elif player_2_robot.collides_with_point(point):
                self._factory.set_player_2(fighter_dicts.robot)

            elif player_2_zombie.collides_with_point(point):
                self._factory.set_player_2(fighter_dicts.zombie)


 
        