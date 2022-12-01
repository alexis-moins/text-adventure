from __future__ import annotations
from abc import ABC, abstractmethod

from typing import TYPE_CHECKING
from core.controllers.controller import Controller


if TYPE_CHECKING:
    from core.dungeon import Dungeon


class Selector(ABC, Controller):

    def __init__(self, dungeon: Dungeon, view) -> None:
        """"""
        super().__init__(dungeon, view)

    @abstractmethod
    def select(self, items):
        """
        Start the controller and ask the user to select exactly one
        item from a list of items.

        Argument:
        items - a list of items to choose from
        """
        pass
