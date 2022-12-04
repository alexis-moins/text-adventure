from __future__ import annotations

from typing import TYPE_CHECKING
from core.controllers.scene_controller import SceneController

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.actions.base_action import BaseAction
    from core.views.sceneries.room_scenery import RoomScenery


class RoomController(SceneController):

    def __init__(self, dungeon: Dungeon, view: RoomScenery, actions: list[BaseAction], pinned: dict[str, BaseAction]) -> None:
        """
        Constructor creating a new room controller

        Arguments:
        dungeon - the current dungeon
        view - the room scenery
        """
        super().__init__(dungeon, view, actions, pinned)

    def on_next_turn(self) -> None:
        """
        Method called whenever the end of turn is reached.
        """
        for npc in self.dungeon.room.entities:
            npc.take_turn(self.dungeon)

        self.dungeon.show_logs()
