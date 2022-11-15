from abc import ABC
from abc import abstractmethod
from core.dungeon import Dungeon

from core.utils.strings import StringBuilder


class View(ABC):
    """
    Abstract view used to render models and interfaces.
    """

    def __init__(self, dungeon: Dungeon, model, actions) -> None:
        """

        """
        self.model = model
        self.actions = actions

        self._builder = StringBuilder()

    @abstractmethod
    def show(self) -> None:
        """
        Show the scenery on screen.
        """
        pass

    def _show_actions(self) -> None:
        """

        """
        actions = [action for action in self.actions
                   if action.can_be_done(self.dungeon)]

        for index, action in enumerate(actions):
            self._builder.add(f'[CYAN{index}WHITE] {action}')

        print(self._builder.build())
