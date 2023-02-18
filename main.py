# from core.dungeon import Dungeon
# from core.utils.armory import Armory
# from core.utils.bestiary import Bestiary
#
# from core.room import Room
# from core.entities.player import Player
#
# room = Room('Wind Meadows YELLOW<East>WHITE',
#             'The east part of the wind meadows is more hilly than the other 3 parts. Wolves love to stay there.')
#
# armory = Armory()
# bestiary = Bestiary()
#
# room.npc.add(bestiary.summon('trader'))
# room.npc.add(bestiary.summon('grey wolf'))
#
# room.items.add(armory.take('potion of healing'))
# room.items.add(armory.take('potion of healing'))
#
# player = Player.barbarian()
# dungeon = Dungeon(player, room)
#
# controller = dungeon.architect.room_scene(room)
# controller.start()
from core import actions
from core.shortcuts import start

from core.validation import ItemInRoom, ItemExists

start('scenario.yaml', {
    'say THING': actions.say,

    'take ITEM': (actions.take, ItemInRoom('ITEM')),
    # 'get ITEM': synonym('take ITEM'),

    'drink BEVERAGE': (actions.drink, ItemExists('BEVERAGE')),
})

# Validators:
# - ItemExists -> in room or in self
# - ItemInRoom -> in room
