from __future__ import annotations

from typing import TYPE_CHECKING
from core.controllers.scene_controller import SceneController

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.entities.npc import NPC
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

    def loot(self, npc: NPC) -> None:
        """

        """
        self.dungeon.room.npc.remove(npc)
        self.dungeon.add_log(f'\nThe {npc.short_description()} is dead.')

        # TODO: would be better to work directly with slots here
        # in case we have 64+ items in a slot.
        for item in npc.inventory.get_entities():
            self.dungeon.room.items.add(item)

        self.dungeon.add_log(
            '\nIt YELLOWdropped somethingWHITE on the ground:')
        self.dungeon.add_log(npc.inventory.long_description())

    def on_next_turn(self) -> None:
        """
        Method called whenever the end of turn is reached.
        """
        for npc in self.dungeon.room.npc.get_entities():

            if not npc.is_alive():
                self.loot(npc)
                continue

            npc.take_turn(self.dungeon)

        self.dungeon.show_logs()
