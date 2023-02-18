
from dataclasses import dataclass

@dataclass
class Validator:
    group: str | tuple[str]


class ItemInRoom(Validator):
    pass

class ItemExists(Validator):
    pass

