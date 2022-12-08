from abc import ABC

from core.entities.describable import Describable


def indefinite_determiner(entity_name: str) -> str:
    """
    Return the correct indefinite determiner for the given entity name.

    Arguments:
    entity_name - the name of an entity

    Returns:
    A string corresponding to a determiner
    """
    return 'an' if entity_name[0] in 'aeiouy' else 'a'


class Entity(Describable, ABC):
    """
    Represents a generic entity, wether it be an item or a character.
    """

    def __init__(self, name: str, description: str) -> None:
        """
        Constructor creating a new abstract Entity.

        Arguments:
        name - the name of the character
        description - the description of the character
        """
        super().__init__()

        self.name = name
        self._description = description

        self.stack_size = 20
        self.determiner = indefinite_determiner(self.name)
