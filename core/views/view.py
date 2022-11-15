from abc import ABC, abstractmethod


class View(ABC):
    """
    Abstract view used to render models and interfaces.
    """

    def __init__(self, model, actions) -> None:
        """

        """
        self.model = model
        self.actions = actions

    @abstractmethod
    def show(self) -> None:
        """
        Show the scenery on screen.
        """
        pass
