from core.dungeon import Dungeon
from core.utils.armoury import Armoury
from core.utils.bestiary import Bestiary

from core.room import Room
from core.entities.player import Player

room = Room('Wind Meadows YELLOW<East>WHITE',
            'The east part of the wind meadows is more hilly than the other 3 parts. Wolves love to stay there.')

wolf_one = Bestiary().summon('grey wolf')
iron_sword = Armoury().take('iron sword')

room.npc.add(wolf_one)
room.items.add(iron_sword)

player = Player()
dungeon = Dungeon(player, room)

controller = dungeon.factory.room_controller(room)
controller.start()
