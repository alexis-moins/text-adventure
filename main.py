from core.dungeon import Dungeon
from core.utils.bestiary import Bestiary

from core.generation.room import Room
from core.entities.player import Player

room = Room('Wind Meadows YELLOW<East>WHITE',
            'The east part of the wind meadows is more hilly than the other 3 parts. Wolves love to stay there.')

royal_guard = Bestiary().summon('grey-wolf')
room.npc.append(royal_guard)

player = Player()
dungeon = Dungeon(player, room)

controller = dungeon.factory.room_controller(room)
controller.start()
