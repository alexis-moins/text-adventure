from __future__ import annotations
import textwrap

def P(objects) -> None:
    """"""
    print(textwrap.fill(objects, width=75))

class StringBuilder:

    def __init__(self) -> None:
        """"""
        self._strings = []

    def add(self, string: str, *, new_line: bool =True) -> StringBuilder:
        """"""
        end = '\n' if new_line else ''
        self._strings.append(string + end)

    def __str__(self) -> str:
        """
        """
        return ''.join(self._strings)


class RoomRenderer:

    def __init__(self, room: Room) -> None:
        self.room = room

    def render(self) -> None:
        """
        """
        builder = StringBuilder()

        builder.add(self.room.name).add(self.room.description)

        if not self.room.entities:
            return print(builder)

        word = 'are' if len(self.room.entities) > 1 else 'is'
        print(f'\nAround you {word}:')

        for item in self.room.entities:
            print(f'{item.indefinite_name}')

        print(builder)


class Room:
    """
    Represents a room, a space containing entities (characters and / or items).
    """

    def __init__(self, name: str, description: str, entities: list = None) -> None:
        self.name = name
        self.description = description
        self.entities = entities or []

        self.is_boss_room: bool = False
        self.rendering = RoomRenderer(self)
