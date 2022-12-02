from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.menu.quit_action import QuitAction
from core.actions.scene.attack_action import AttackAction
from core.controllers.scene_controller import SceneController


if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.views.sceneries.room_scenery import RoomScenery


class RoomController(SceneController):

    def __init__(self, dungeon: Dungeon, view: RoomScenery) -> None:
        """
        Constructor creating a new room controller.

        Arguments:
        dungeon - the currently opened dungeon
        view - the view associated with the controller
        """
        super().__init__(dungeon, view)

        self.add_actions(
            AttackAction()
        )

        self.add_pinned_actions(
            QuitAction(key='q')
        )

    def start(self) -> None:
        """
        Start the controller.
        """
        while self.is_running:
            actions, pinned = self.filter_actions()

            self.view.show()
            self.view.show_actions(actions, pinned)

            action = self.get_action(actions, pinned)

            if not action:
                continue

            action.execute(self)
