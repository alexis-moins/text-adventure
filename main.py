from core.controllers.room_controller import RoomController
from core.controllers.room_controller import RoomView
from core.dungeon import Dungeon
from core.entities.player import Player
from core.generation.room import Room


room = Room('Castle entrance',
            'The castle entrance is often guarded by royal guards')

player = Player()

controller = RoomController(
    Dungeon(player, room),
    RoomView(room)
)

controller.start()
