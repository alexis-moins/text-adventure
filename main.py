import core.dungeon as dungeon
from core.engine.functions import start_engine

from core.generation.room import Room
from core.entities import NPC

starting_room = Room(
    'Castle Entrance', 'The castle entrance is usually watched over by the royal guard.')
royal_guard = NPC('Fil', 'This royal guard does not look so strong...')

starting_room.entities.add(royal_guard)

dungeon.current_room = starting_room

start_engine()
