from __future__ import annotations

from typing import TYPE_CHECKING
from core.views.view import View

if TYPE_CHECKING:
    from core.dungeon import Dungeon
    from core.entities.describable import Describable


class Scenery(View):

    def __init__(self, dungeon: Dungeon, model: Describable) -> None:
        """
        Constructor creating a new scenery for a describable model.
        """
        super().__init__(dungeon)
        self.model = model
