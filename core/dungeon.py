from core.entities import Player, NPC
from core.generation.room import Room

# The player wandering through the corridors of the dungeon
player = Player()

royal_guard = NPC('royal guard', 'This royal guard does not look so strong...')

# The room where the scene is taking place
current_room = Room(
    'Castle Entrance', 'The castle entrance is usually watched over by the royal guard.')

current_room.entities.add(royal_guard)

# Turn counter
turn = 1

# Which level are we currently at
level = 1
