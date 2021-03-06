from game import constants


import arcade

class Player(arcade.Sprite):
    def __init__(self, fighter_dict, start_x, start_y):
        super().__init__(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")
        self.center_x = start_x
        self.center_y = start_y
        """ Init """
        
        self.fighter_dict = fighter_dict
        main_path = fighter_dict["avatar"]

        # Load textures for idle standing
        self.idle_texture_pair = arcade.load_texture_pair(f"{main_path}_idle.png")
        self.jump_texture_pair = arcade.load_texture_pair(f"{main_path}_jump.png")
        self.fall_texture_pair = arcade.load_texture_pair(f"{main_path}_fall.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range(8):
            texture = arcade.load_texture_pair(f"{main_path}_walk{i}.png")
            self.walk_textures.append(texture)

        # Set the initial texture
        self.texture = self.idle_texture_pair[0]

        # Hit box will be set based on the first image used.
        self.hit_box = self.texture.hit_box_points

        # Default to face-right
        self.character_face_direction = constants.RIGHT_FACING

        # Index of our current texture
        self.cur_texture = 0

        # How far have we traveled horizontally since changing the texture
        self.x_odometer = 0



        self.lives = 3
        self.jumps = 0
        self.damage = 0

        self.jump_sound = arcade.load_sound(":resources:sounds/jump5.wav")
        self.hit_noise = arcade.load_sound(":resources:sounds/hit4.wav")

        self.a_attack_active = False
        self.b_attack_active = False

        self.successive_jumping_frames = 0
        self.successive_a_attack_frames = 0
        self.successive_b_attack_frames = 0

    def pymunk_moved(self, physics_engine, dx, dy, d_angle):
        """ Handle being moved by the pymunk engine """
        # Figure out if we need to face left or right
        if dx < -constants.DEAD_ZONE and self.character_face_direction == constants.RIGHT_FACING:
            self.character_face_direction = constants.LEFT_FACING
        elif dx > constants.DEAD_ZONE and self.character_face_direction == constants.LEFT_FACING:
            self.character_face_direction = constants.RIGHT_FACING

        # Are we on the ground?
        is_on_ground = physics_engine.is_on_ground(self)

        # Add to the odometer how far we've moved
        self.x_odometer += dx
        if self.a_attack_active or self.b_attack_active:
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return

        # Jumping animation
        if not is_on_ground:
            if dy > constants.DEAD_ZONE:
                self.texture = self.jump_texture_pair[self.character_face_direction]
                return
            elif dy < -constants.DEAD_ZONE:
                self.texture = self.fall_texture_pair[self.character_face_direction]
                return

        # Idle animation
        if abs(dx) <= constants.DEAD_ZONE:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Have we moved far enough to change the texture?
        if abs(self.x_odometer) > constants.DISTANCE_TO_CHANGE_TEXTURE:

            # Reset the odometer
            self.x_odometer = 0

            # Advance the walking animation
            self.cur_texture += 1
            if self.cur_texture > 7:
                self.cur_texture = 0
            self.texture = self.walk_textures[self.cur_texture][self.character_face_direction]

    def jump_noise(self):
        arcade.play_sound(self.jump_sound)

    def get_hit(self):
        
        arcade.play_sound(self.hit_noise)