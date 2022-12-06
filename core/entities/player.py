from core.fight.fighter import Fighter
from core.containers.container import Container
from core.items.item import Item
from core.utils.armoury import Armoury


class Player:

    def __init__(self) -> None:
        """
        Constructor creating a new player.
        """
        armoury = Armoury()
        inventory: Container[Item] = Container([
            armoury.take('iron sword')
        ])

        self.fighter = Fighter(health=20, magic=10,
                               strength=2, defence=2, inventory=inventory)
