from core.fight.fighter import Fighter


class Player(Fighter):

    def __init__(self) -> None:
        """
        Constructor creating a new player.
        """
        super().__init__(health=20, magic=10, strength=2, defence=2)
