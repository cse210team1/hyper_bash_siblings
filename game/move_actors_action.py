from game.action import Action
from game.control_actors_action import ControlActorsAction
from game import constants


class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller
    """

    def __init__(self, physics_engine):
        self.physics_engine = physics_engine
        

    def execute(self, cast, args, director):
        self.physics_engine.step()
        is_on_ground = self.physics_engine.is_on_ground(cast["paddle"][0])
        if director.left_pressed and not director.right_pressed:
            # Create a force to the left. Apply it.
            if is_on_ground:
                force = (-constants.PLAYER_MOVE_FORCE_ON_GROUND, 0)
            else:
                force = (-constants.PLAYER_MOVE_FORCE_IN_AIR, 0)
            self.physics_engine.apply_force(cast["paddle"][0], force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(cast["paddle"][0], 0)
        elif director.right_pressed and not director.left_pressed:
            # Create a force to the right. Apply it.
            if is_on_ground:
                force = (constants.PLAYER_MOVE_FORCE_ON_GROUND, 0)
            else:
                force = (constants.PLAYER_MOVE_FORCE_IN_AIR, 0)
            self.physics_engine.apply_force(cast["paddle"][0], force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(cast["paddle"][0], 0)
        else:
            # Player's feet are not moving. Therefore up the friction so we stop.
            self.physics_engine.set_friction(cast["paddle"][0], 1.0)
        if director.up_pressed:
            if self.physics_engine.is_on_ground(cast["paddle"][0]):
                
                impulse = (0, constants.PLAYER_JUMP_IMPULSE)
                self.physics_engine.apply_impulse(cast["paddle"][0], impulse)
        pass
        
    
        