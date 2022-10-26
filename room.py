from __future__ import annotations
from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Room:
    """
    Represents a room, a space containing entities (characters and or items).
    """
    name: str
    description: str

    entities: list = field(default_factory=list)
    exits: tuple[Room, Room] = field(default_factory=tuple)
