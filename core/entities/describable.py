from abc import ABC, abstractmethod

from core.utils.strings import StringBuilder


class Describable(ABC):
    """
    Represents any element of the world that is describable, whether it
    be a Room or an Entity.
    """

    def __init__(self) -> None:
        """
        Constructor creating a new describable element of the world.
        """
        self._builder = StringBuilder()

    @abstractmethod
    def short_description(self) -> str:
        """
        Return the short description of this element.

        Returns:
        A string
        """
        pass

    @abstractmethod
    def long_description(self) -> str:
        """
        Return the long description of this element.

        Returns:
        A string
        """
        pass
