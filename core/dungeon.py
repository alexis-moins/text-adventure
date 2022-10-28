from core.generation.room import Room
import core.entities.classes as classes

# The player wandering through the corridors of the dungeon
player = classes.Player(name='hero')

# The room where the scene is taking place
current_room: Room = None

# Turn counter
turn = 1

# Which level are we currently at
level = 1
