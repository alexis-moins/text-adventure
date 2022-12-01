from __future__ import annotations
from typing import TYPE_CHECKING

from core.actions.base_action import BaseAction

if TYPE_CHECKING:
    from core.dungeon import Dungeon


class MenuAction(BaseAction):

    def __init__(self, *, key: str = '') -> None:
        """"""
        super().__init__(key=key)

    def can_be_performed(self, _: Dungeon) -> bool:
        """
        Return true whether this action can be performed in the given context.

        Argument:
        context - the currently opened dungeon

        Returns:
        a boolean
        """
        return True
