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
        is_on_ground = self.physics_engine.is_on_ground(cast["player"][0])
        
        # lateral motion

        if director.j_pressed and not director.l_pressed:
            # Create a force to the left. Apply it.
            if is_on_ground:
                force = (-constants.PLAYER_MOVE_FORCE_ON_GROUND, 0)
            else:
                force = (-constants.PLAYER_MOVE_FORCE_IN_AIR, 0)
            self.physics_engine.apply_force(cast["player"][0], force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(cast["player"][0], 0)
        elif director.l_pressed and not director.j_pressed:
            # Create a force to the right. Apply it.
            if is_on_ground:
                force = (constants.PLAYER_MOVE_FORCE_ON_GROUND, 0)
            else:
                force = (constants.PLAYER_MOVE_FORCE_IN_AIR, 0)
            self.physics_engine.apply_force(cast["player"][0], force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(cast["player"][0], 0)
        else:
            # Player's feet are not moving. Therefore up the friction so we stop.
            self.physics_engine.set_friction(cast["player"][0], 1.0)

        # jumping

        if director.i_pressed:
            if self.physics_engine.is_on_ground(cast["player"][0]):
                
                impulse = (0, constants.PLAYER_JUMP_IMPULSE)
                self.physics_engine.apply_impulse(cast["player"][0], impulse)
        pass
        
 # lateral motion
# player 2
        if director.a_pressed and not director.d_pressed:
            # Create a force to the left. Apply it.
            if is_on_ground:
                force = (-constants.PLAYER_MOVE_FORCE_ON_GROUND, 0)
            else:
                force = (-constants.PLAYER_MOVE_FORCE_IN_AIR, 0)
            self.physics_engine.apply_force(cast["player"][1], force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(cast["player"][1], 0)
        elif director.d_pressed and not director.a_pressed:
            # Create a force to the right. Apply it.
            if is_on_ground:
                force = (constants.PLAYER_MOVE_FORCE_ON_GROUND, 0)
            else:
                force = (constants.PLAYER_MOVE_FORCE_IN_AIR, 0)
            self.physics_engine.apply_force(cast["player"][1], force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(cast["player"][1], 0)
        else:
            # Player's feet are not moving. Therefore up the friction so we stop.
            self.physics_engine.set_friction(cast["player"][1], 1.0)

        # jumping
        
        if director.w_pressed:
            if self.physics_engine.is_on_ground(cast["player"][1]):
                
                impulse = (0, constants.PLAYER_JUMP_IMPULSE)
                self.physics_engine.apply_impulse(cast["player"][1], impulse)
        pass
        
    
                