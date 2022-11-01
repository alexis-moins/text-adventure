import core.generation.room as room
import core.entities.classes as classes

# The player wandering through the corridors of the dungeon
player = classes.Player()

# The room where the scene is taking place
current_room: room.Room = None

# Turn counter
turn = 1

# Which level are we currently at
level = 1
