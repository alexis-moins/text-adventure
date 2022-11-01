class ActionException(Exception):

    def __init__(self, message: str) -> None:
        """
        """
        super().__init__()
        self.message = message

    def __str__(self) -> str:
        """
        """
        return self.message
