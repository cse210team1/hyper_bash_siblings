from game.action import Action
from game import constants


class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller
    """

    def __init__(self, physics_engine):
        self.physics_engine = physics_engine
    
    def get_velocity(self, sprite):
        physics_object = self.physics_engine.get_physics_object(sprite)
        return physics_object.body.velocity
        
    def is_on_ground(self, object):
        if self.physics_engine.is_on_ground(object) == True:
            return True
        else:
            return False

    def execute(self, cast, args, director):
        print(cast["player"][0].center_y)
        print(self.get_velocity(cast["player"][0]))

        self.physics_engine.step()
        
        # lateral motion

        if director.j_pressed and not director.l_pressed:
            # Create a force to the left. Apply it.
            if self.is_on_ground(cast["player"][1]):
                force = (-constants.PLAYER_MOVE_FORCE_ON_GROUND * cast["player"][1].fighter_dict["ground_force"], 0)
            else:
                force = (-constants.PLAYER_MOVE_FORCE_IN_AIR * cast["player"][1].fighter_dict["air_force"], 0)
            self.physics_engine.apply_force(cast["player"][1], force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(cast["player"][1], 0)
        elif director.l_pressed and not director.j_pressed:
            # Create a force to the right. Apply it.
            if self.is_on_ground(cast["player"][1]):
                force = (constants.PLAYER_MOVE_FORCE_ON_GROUND * cast["player"][1].fighter_dict["air_force"], 0)
            else:
                force = (constants.PLAYER_MOVE_FORCE_IN_AIR * cast["player"][1].fighter_dict["air_force"], 0)
            self.physics_engine.apply_force(cast["player"][1], force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(cast["player"][1], 0)
        else:
            # Player's feet are not moving. Therefore up the friction so we stop.
            self.physics_engine.set_friction(cast["player"][1], 1.0)

        # jumping

        if director.i_pressed:
            if cast["player"][1].jumps < 1:
                if cast["player"][1].successive_jumping_frames == 0:
                    impulse = (0, constants.PLAYER_JUMP_IMPULSE)
                    x_vel = self.get_velocity(cast["player"][1])[0]
                    new_vel = (x_vel, 0)
                    self.physics_engine.set_velocity(cast["player"][1], new_vel)
                    self.physics_engine.apply_impulse(cast["player"][1], impulse)
                    cast["player"][1].jump_noise()
                    cast["player"][1].jumps += 1
                    cast["player"][1].successive_jumping_frames +=1
        else:
            cast["player"][1].successive_jumping_frames = 0

        if self.is_on_ground(cast["player"][1]):
            cast["player"][1].jumps = 0

        # fast falling
        if director.k_pressed:
            impulse = (0, constants.PLAYER_FAST_FALL_IMPULSE *-1)
            self.physics_engine.apply_impulse(cast["player"][1], impulse)


        
 # lateral motion
# player 2
        if director.a_pressed and not director.d_pressed:
            # Create a force to the left. Apply it.
            if self.is_on_ground(cast["player"][0]):
                force = (-constants.PLAYER_MOVE_FORCE_ON_GROUND * cast["player"][0].fighter_dict["ground_force"], 0)
            else:
                force = (-constants.PLAYER_MOVE_FORCE_IN_AIR * cast["player"][0].fighter_dict["air_force"], 0)
            self.physics_engine.apply_force(cast["player"][0], force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(cast["player"][0], 0)
        elif director.d_pressed and not director.a_pressed:
            # Create a force to the right. Apply it.
            if self.is_on_ground(cast["player"][0]):
                force = (constants.PLAYER_MOVE_FORCE_ON_GROUND * cast["player"][0].fighter_dict["ground_force"], 0)
            else:
                force = (constants.PLAYER_MOVE_FORCE_IN_AIR * cast["player"][0].fighter_dict["air_force"], 0)
            self.physics_engine.apply_force(cast["player"][0], force)
            # Set friction to zero for the player while moving
            self.physics_engine.set_friction(cast["player"][0], 0)
        else:
            # Player's feet are not moving. Therefore up the friction so we stop.
            self.physics_engine.set_friction(cast["player"][0], 1.0)

        # jumping
        
        if director.w_pressed:
            if cast["player"][0].jumps < 1:
                if cast["player"][0].successive_jumping_frames == 0:
                    impulse = (0, constants.PLAYER_JUMP_IMPULSE)
                    x_vel = self.get_velocity(cast["player"][0])[0]
                    new_vel = (x_vel, 0)
                    self.physics_engine.set_velocity(cast["player"][0], new_vel)
                    self.physics_engine.apply_impulse(cast["player"][0], impulse)
                    cast["player"][0].jump_noise()
                    cast["player"][0].jumps += 1
                    cast["player"][0].successive_jumping_frames +=1
        else:
            cast["player"][0].successive_jumping_frames = 0

        if self.is_on_ground(cast["player"][0]):
            cast["player"][0].jumps = 0

        # fast falling
        if director.s_pressed:
            impulse = (0, constants.PLAYER_FAST_FALL_IMPULSE *-1)
            self.physics_engine.apply_impulse(cast["player"][0], impulse)