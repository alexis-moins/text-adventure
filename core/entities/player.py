import core.engine.parser as parser
from core.entities.character import Character
from core.fight.fighter import Fighter


class Player(Character):

    def __init__(self) -> None:
        """
        Constructor creating a new player.
        """
        super().__init__('Hero', 'Whaou! A hero!', Fighter())

    def take_turn(self) -> bool:
        """
        Let the player write something and behave based on the input.

        Returns:
        true if the player has executed a command, false otherwise
        """
        user_input = parser.get_input()
        action, arguments = parser.parse_input(user_input)

        if not action:
            print('I don\'t understand that')
            return False

        return action(actor=self).execute(arguments)

    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        return self.name

    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        pass
