from __future__ import annotations

from typing import TYPE_CHECKING

from core.views.view import View

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.generation.room import Room
    from core.actions.base_action import BaseAction


class RoomView(View):
    """
    View used to render a room.
    """

    def __init__(self, dungeon: Dungeon, room: Room) -> None:
        """
        Constructor creating a new view of a room.

        Arguments:
        dungeon - the context
        room - the model rendered in the view
        """
        super().__init__(dungeon, room)

    def show(self, actions: list[BaseAction]) -> None:
        """
        Show the scenery on screen.

        Argument:
        actions - the list of available action types
        """
        self.clear()
        self.show_status_bar()

        print(self.model.long_description())

        self.show_actions(actions)
