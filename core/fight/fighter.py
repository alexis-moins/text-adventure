class Fighter:

    def __init__(self, health: int = 20, magic: int = 10, strength: int = 2, defense: int = 2) -> None:
        """
        Constructor creating a Fighter component.

        Arguments:
        health - used to take damage
        magic - used to cast spells

        strength - used to deal physical damage
        defense - used to mitigate physical damages
        """
        self._health = health
        self.max_health = health

        self._magic = magic
        self.max_magic = magic

        self.strength = strength
        self.defense = defense

    @property
    def health(self) -> int:
        """
        Return the health of the fighter.

        Returns:
        An integer
        """
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """
        Set the health of the fighter. The method ensures the
        value of health stays between 0 and max_health.

        Argument:
        value - the new health of the fighter
        """
        self._health = max(0, min(value, self.max_health))

    def receive_damage(self, amount: int) -> None:
        """
        Decrease the health of the fighter according to the
        amount of damage received.

        Argument:
        amount - how many damag is received
        """
        self.health -= amount