from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.menu.select_action import SelectAction
from core.controllers.scene_controller import SceneController

if TYPE_CHECKING:
    from core.actions.base_action import BaseAction
    from core.containers.container import Container
    from core.entities.describable import Describable


class SelectionController(SceneController):

    def start(self, models: Container[Describable]) -> Describable | None:
        """
        Start the controller and ask the user to select exactly one
        item from a list of items.

        Argument:
        items - a list of items to choose from
        """
        self.selection: Describable | None = None

        self.actions: list[BaseAction] = [
            SelectAction(self.dungeon, model) for model in models]

        super().start()

    def on_next_turn(self) -> None:
        """
        Method called whenever the end of turn is reached.
        """
        if self.selection:
            self.is_running = False
