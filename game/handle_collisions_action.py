import arcade
from game import constants
from game.action import Action



class HandleCollisionsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def __init__(self, physics_engine):
        self.physics_engine = physics_engine

    def execute(self, cast, args, director):
        player_1 = cast["player"][0]
        player_2 = cast["player"][1]

        if player_1.collides_with_sprite(player_2):
            
            # Player 1 hits attack a
            if player_1.a_attack_active and not player_2.a_attack_active and not player_2.b_attack_active:
                direction = None
                if player_1.center_x < player_2.center_x:
                    direction = 1
                else:
                    direction = -1

                # an instant kill will be around 60k force and a basic around 12k  
                base_hit = constants.PLAYER_HIT_SIDE * (1+ player_2.damage) # Replace with damage later to figure knockback based on health
                hit_strength = base_hit * player_1.fighter_dict["a_attack"]
                force = (direction * hit_strength, 0)
                self.physics_engine.apply_force(player_2, force)
                base_up = constants.PLAYER_HIT_UP * (1+ player_2.damage)
                hit_up = base_up * player_1.fighter_dict["a_attack"] 
                if hit_up > 1650:
                    hit_up = 1650
                # a instant kill is around 1600 total, base is around 225 for jump force. 
                impulse = (0, hit_up)
                print(hit_up)
                self.physics_engine.apply_impulse(player_2, impulse)
                
                #damage:
                player_2.damage += hit_strength * 0.0001 * player_2.fighter_dict["damage_multiplier"]

            #Player 1 hits attack b 
            elif player_1.b_attack_active and not player_2.a_attack_active and not player_2.b_attack_active:
                direction = None
                if player_1.center_x < player_2.center_x:
                    direction = 1
                else:
                    direction = -1

                # an instant kill will be around 60k force and a basic around 12k  
                base_hit = constants.PLAYER_HIT_SIDE * (1+ player_2.damage) # Replace with damage later to figure knockback based on health
                hit_strength = base_hit * player_1.fighter_dict["b_attack"]
                force = (direction * hit_strength, 0)
                self.physics_engine.apply_force(player_2, force)
                base_up = constants.PLAYER_HIT_UP * (1+ player_2.damage)
                hit_up = base_up * player_1.fighter_dict["b_attack"] 
                if hit_up > 1650:
                    hit_up = 1650
                # a instant kill is around 1600 total, base is around 225 for jump force. 
                impulse = (0, hit_up)
                print(hit_up)
                self.physics_engine.apply_impulse(player_2, impulse)
                #damage:
                player_2.damage += hit_strength * 0.0001 * player_2.fighter_dict["damage_multiplier"]

            # player 2 hits attack a 
            if not player_1.a_attack_active and not player_1.a_attack_active and player_2.a_attack_active:
                direction = None
                if player_1.center_x > player_2.center_x:
                    direction = 1
                else:
                    direction = -1

                # an instant kill will be around 60k force and a basic around 12k  
                base_hit = constants.PLAYER_HIT_SIDE * (1+ player_1.damage)
                print(base_hit) # Replace with damage later to figure knockback based on health
                hit_strength = base_hit * player_2.fighter_dict["a_attack"]
                force = (direction * hit_strength, 0)
                self.physics_engine.apply_force(player_1, force)
                base_up = constants.PLAYER_HIT_UP * (1+ player_1.damage)
                hit_up = base_up * player_2.fighter_dict["a_attack"] 
                if hit_up > 1650:
                    hit_up = 1650
                # a instant kill is around 1600 total, base is around 225 for jump force. 
                impulse = (0, hit_up)
                print(hit_up)
                self.physics_engine.apply_impulse(player_1, impulse)

                #damage:
                player_1.damage += hit_strength * 0.0001 * player_1.fighter_dict["damage_multiplier"]


            # Player 2 hits attack b 
            elif not player_1.a_attack_active and not player_1.a_attack_active and player_2.b_attack_active:
                direction = None
                if player_1.center_x > player_2.center_x:
                    direction = 1
                else:
                    direction = -1

                # an instant kill will be around 60k force and a basic around 12k  
                base_hit = constants.PLAYER_HIT_SIDE * (1+ player_1.damage) # Replace with damage later to figure knockback based on health
                hit_strength = base_hit * player_2.fighter_dict["b_attack"]
                force = (direction * hit_strength, 0)
                self.physics_engine.apply_force(player_1, force)
                base_up = constants.PLAYER_HIT_UP * (1+ player_1.damage)
                hit_up = base_up * player_2.fighter_dict["b_attack"]
                if hit_up > 1650:
                    hit_up = 1650
                # a instant kill is around 1600 total, base is around 225 for jump force. 
                impulse = (0, hit_up)
                print(hit_up)
                self.physics_engine.apply_impulse(player_1, impulse)

                #damage:
                player_1.damage += hit_strength * 0.0001 * player_1.fighter_dict["damage_multiplier"]