from core.items.item import Item


class Equipable(Item):

    def __init__(self, name: str, description: str, price: int, slot: str) -> None:
        super().__init__(name, description, price)

        self.slot = slot
        self.equiped = False

        self.stack_size = 1
