from core.entities.entity import Entity


class Item(Entity):

    def __init__(self, name: str, description: str, price: int) -> None:
        """

        """
        super().__init__(name, description)
        self.price = price
