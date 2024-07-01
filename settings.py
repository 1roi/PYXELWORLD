import math

from game.blocks.Block import tex_coords

# World
TICKS_PER_SEC = 60
# SECTOR_SIZE = Moved at Block.py

# Physics
GRAVITY = 22.0
MAX_JUMP_HEIGHT = 1.15
JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)
TERMINAL_VELOCITY = 50

# Player
WALKING_SPEED = 4
SPRINTING_SPEED = 5
FLYING_SPEED = 12
PLAYER_HEIGHT = 2
FLYING_UP_SPEED = JUMP_SPEED * (FLYING_SPEED / 100)

# Camera
CAMERA_SENSIBILITY = 0.15

# Textures
TEXTURE_PATH = 'textures/blocktextures.png'
FONT_PATH = 'fonts/pyxelfont.TTF'
RETICLE_PATH = 'textures/reticle.png'

# Block List
GRASS = tex_coords((1, 0), (0, 1), (0, 0))
SAND = tex_coords((1, 1), (1, 1), (1, 1))
BRICK = tex_coords((2, 0), (2, 0), (2, 0))
STONE = tex_coords((2, 1), (2, 1), (2, 1))
WOODEN_PLANKS = tex_coords((1, 2), (1, 2), (1, 2))
STONE_BRICKS = tex_coords((2, 2), (2, 2), (2, 2))
COBBLESTONE = tex_coords((2, 3), (2, 3), (2, 3))

FACES = [
    ( 0, 1, 0),
    ( 0,-1, 0),
    (-1, 0, 0),
    ( 1, 0, 0),
    ( 0, 0, 1),
    ( 0, 0,-1),
]

# Other
VERSION = "ALPHA 0.1"