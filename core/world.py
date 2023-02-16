from __future__ import annotations

class World:

    def __init__(self, map: str) -> None:
        self.map = map

    @staticmethod
    def create(map: str) -> World:
        # create map of room
        return World(map)
