from __future__ import annotations
from dataclasses import dataclass, field
from typing import Generic, TypeVar


@dataclass
class Room:
    """
    Represents a room, a space containing entities (characters and / or items).
    """
    name: str
    description: str

    entities: list = field(default_factory=list)
    is_boss_room: bool = field(default=False, init=False)




T = TypeVar('T')

class Generator(Generic[T]):
    """
    """
    pass

    def generate(self, amount: int) -> list[Room]:
        """
        Generate and return as many instance of T as possible.

        Returns:
        A list of instances of T
        """
        return [Room(name='', description='') for _ in range(amount)]


generator: Generator[Room] = Generator()
