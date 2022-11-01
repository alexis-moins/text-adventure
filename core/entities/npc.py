from core.entities.character import Character


class NPC(Character):

    def __init__(self, name: str, description: str) -> None:
        """
        Constructor creating a new NPC, whether it is hostile or not.

        Arguments:
        name - the name of the NPC
        description - the description of the NPC
        """
        super().__init__(name, description)

    def take_turn(self) -> bool:
        """
        Make the NPC take its turn.

        Returns:
        true if the actor has executed an action, false otherwise
        """
        pass

    def short_description(self) -> str:
        """
        Return the short description of the Npc.

        Returns:
        A string
        """
        return self._builder.add(self.name + f' RED[!]WHITE').build()

    def long_description(self) -> str:
        """
        Return the long description of the NPC.

        Returns:
        A string
        """
        pass