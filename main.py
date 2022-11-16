from core.controllers.room_controller import RoomController
from core.dungeon import Dungeon
from core.entities.player import Player
from core.generation.room import Room
from core.views.room_view import RoomView


room = Room('Castle entrance',
            'The castle entrance is often guarded by royal guards')

player = Player()
dungeon = Dungeon(player, room)

controller = RoomController(dungeon, RoomView(dungeon, room))
controller.start()
