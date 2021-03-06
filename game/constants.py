import os

MAX_X = 1300
MAX_Y = 750

PADDLE_Y = 25

PADDLE_MOVE_SCALE = 5

hit_multiplier = .0875


# --- Physics forces. Higher number, faster accelerating.

# Gravity
GRAVITY = 1500

# Damping - Amount of speed lost per second
DEFAULT_DAMPING = 1.0
PLAYER_DAMPING = 0.4

# Friction between objects
PLAYER_FRICTION = 1.0
WALL_FRICTION = 0.7
DYNAMIC_ITEM_FRICTION = 0.6

# Mass (defaults to 1)
PLAYER_MASS = 2.0

# Keep player from going too fast
PLAYER_MAX_HORIZONTAL_SPEED = 4500
PLAYER_MAX_VERTICAL_SPEED = 1600

PLAYER_MOVE_FORCE_ON_GROUND = 2000

# Force applied when moving left/right in the air
PLAYER_MOVE_FORCE_IN_AIR = 1300

# Strength of a jump
PLAYER_JUMP_IMPULSE = 1800

# Force applied during fast fall
PLAYER_FAST_FALL_IMPULSE = 50

# Scale sprites up or down
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_TILES = 0.5

RIGHT_FACING = 0
LEFT_FACING = 1

DISTANCE_TO_CHANGE_TEXTURE = 20

DEAD_ZONE = 0.1

PLAYER_HIT_SIDE = 400
PLAYER_HIT_UP = 75

# Scaled sprite size for tiles
#SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)
