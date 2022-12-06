from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from core.items.weapon import Weapon


class Equipments(TypedDict, total=False):
    """
    Equipments for fighters.
    """
    weapon: Weapon
