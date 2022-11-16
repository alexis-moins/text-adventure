from core.controllers.room_controller import RoomController
from core.dungeon import Dungeon
from core.entities import NPC
from core.entities.player import Player
from core.fight.fighter import Fighter
from core.generation.room import Room
from core.views.room_view import RoomView


room = Room('Castle entrance',
            'The castle entrance is often guarded by royal guards.')

royal_guard = NPC('Fil', 'That royal guard is super strong',
                  Fighter(), is_hostile=False, character='~')

room.entities.add(royal_guard)

player = Player()
dungeon = Dungeon(player, room)

controller = RoomController(dungeon, RoomView(dungeon, room))
controller.start()
