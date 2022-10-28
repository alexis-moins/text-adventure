from core.generation.room import generator, Room
import core.entities.classes as classes

# The player wandering through the corridors of the dungeon
player = classes.Player(name='hero')

# The room where the scene is taking place
current_room: Room = generator.generate(1)[0]

# Turn counter
turn = 1

# Which level are we currently at
level = 1
