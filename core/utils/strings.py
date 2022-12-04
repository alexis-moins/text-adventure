"""
Module providing a StringBuilder class to build and format strings, as
well as a parse_colors function to create colored strings.
"""
from typing import Self
from textwrap import TextWrapper

from colorama import Fore


_colors = {
    'RED': Fore.RED,
    'GREEN': Fore.GREEN,
    'YELLOW': Fore.YELLOW,
    'BLUE': Fore.BLUE,
    'MAGENTA': Fore.MAGENTA,
    'CYAN': Fore.CYAN,
    'WHITE': Fore.WHITE,
    'GREY': Fore.LIGHTBLACK_EX,
}


def parse_colors(string: str) -> str:
    """
    Parse the color markers in a string and return a string in which
    the markers have been replaced with ANSI color codes. Markers

    Argument:
    string - the string containing color markers

    Returns:
    a colored string
    """
    for color, ANSI_code in _colors.items():
        string = string.replace(color, ANSI_code)

    return string


class StringBuilder:
    """
    Represents a buffer of formatted and colored strings to create
    multi-line outputs with ease.
    """

    def __init__(self, width: int = 70) -> None:
        """
        Constructor creating a new StringBuilder, useful for creating
        formatted multi-line strings with ease.
        """
        self._buffer = []
        self._new_line = False
        self._wrapper = TextWrapper(width=width, break_long_words=False,
                                    replace_whitespace=False)

    def add(self, string: str, *, wrap: bool = True) -> Self:
        """
        Add a string to the builder's internal buffer.

        Argument:
        string - the string to add to the builder

        Keyword Argument:
        wrap - whether the string should be wrapped or not

        Returns:
        The current StringBuilder instance
        """
        colored_string = parse_colors(string)

        if '\n' in colored_string:
            self._buffer.extend(colored_string.split('\n'))
            return self

        self._buffer.append(self._wrapper.fill(
            colored_string) if wrap else colored_string)

        if self._new_line:
            self._new_line = False
            self._buffer[0] = '\n' + self._buffer[0]

        return self

    def new_line(self, number: int = 1) -> Self:
        """
        Add a number of new lines to the buffer (default: 1).

        Argument:
        number - the number of new lines to add to the buffer

        Returns:
        The current StringBuilder instance
        """
        if not self._buffer:
            self._new_line = True
        else:
            self._buffer[-1] += '\n' * number
        return self

    def build(self) -> str:
        """
        Return the final string, then clear the builder.

        Returns:
        A string
        """
        string = '\n'.join(self._buffer)
        self._buffer = []

        return string

    def print(self) -> None:
        """
        Build and print the buffer on screen.
        """
        string = self.build()
        print(string)
