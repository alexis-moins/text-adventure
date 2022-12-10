from core.dungeon import Dungeon
from core.utils.armory import Armory
from core.utils.bestiary import Bestiary

from core.room import Room
from core.entities.player import Player

room = Room('Wind Meadows YELLOW<East>WHITE',
            'The east part of the wind meadows is more hilly than the other 3 parts. Wolves love to stay there.')

armory = Armory()
bestiary = Bestiary()

room.npc.add(bestiary.summon('grey wolf'))
room.npc.add(bestiary.summon('grey wolf'))

room.items.add(armory.take('leather armor'))
room.items.add(armory.take('iron sword'))

player = Player()
dungeon = Dungeon(player, room)

controller = dungeon.factory.room_controller(room)
controller.start()
