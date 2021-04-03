from game.action import Action
from game.stage import Stage
class Cast_guy(Action):

    def __init__(self):
        self.player_1_choice = None
        self.player_2_choice = None
        self.cast_1 = {}
        self.cast_2 = {}
        self.one = True
        self.two = False

    def execute(self, cast, args, director):
        pass
        # if self.one:
        #     cast["stage"] = []

        #     for x in range(184, 840, 128):
        #             brick = Stage(x,32)
        #             cast["stage"].append(brick)
    def make_cast(self):
        if self.one:
            self.cast_1["stage"] = []

            for x in range(184, 840, 128):
                    brick = Stage(x,32)
                    self.cast_1["stage"].append(brick)

        if self.two:

            self.cast_2["player"] = []
            self.cast_2["player"].append(Player(fighter_dicts.bob, 300, 700))
            self.cast_2["player"].append(Player(fighter_dicts.zombie, 600, 700))


            self.cast_2["stage"] = []

            for x in range(184, 840, 128):
                    brick = Stage(x,32)
                    self.cast_2["stage"].append(brick)
                
            self.cast_2["hud"] = []
            self.cast_2["hud"].append(Display())
    def get_cast(self):
        if self.one:
            return self.cast_1

        elif self.two:
            return self.cast_2


