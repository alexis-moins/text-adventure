from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Room:
    """
    Represents a room, a space containing entities (characters and / or items).
    """
    name: str
    description: str

    entities: list = field(default_factory=list)
    is_boss_room: bool = field(default=False, init=False)
