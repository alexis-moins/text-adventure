from core.controllers.room_controller import RoomController
from core.dungeon import Dungeon
from core.entities.player import Player
from core.generation.room import Room
from core.utils.bestiary import Bestiary
from core.views.room_view import RoomView


room = Room('Castle entrance',
            'The castle entrance is often guarded by royal guards.')

royal_guard = Bestiary().summon('royal-guard')
room.entities.add(royal_guard)

player = Player()
dungeon = Dungeon(player, room)

controller = RoomController(dungeon, RoomView(dungeon, room))
controller.start()
