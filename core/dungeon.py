from core.entities import Player
from core.generation.room import Room

# The player wandering through the corridors of the dungeon
player = Player()

# The room where the scene is taking place
current_room: Room = None

# Turn counter
turn = 1

# Which level are we currently at
level = 1
