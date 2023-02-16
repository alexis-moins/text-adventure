from __future__ import annotations
from dataclasses import dataclass
from typing import Callable
from re import match

from core.world import World

Action = Callable[[World, dict[str, str]], None]



@dataclass(frozen=True)
class ActionManager:
    """
    Class responsible for the management and registration of actions.
    """
    actions: dict[str, Action]
    _determiners: str = r'(the |a |an )?'

    @staticmethod
    def use(actions: dict[str, Action]) -> ActionManager:
        return ActionManager({ActionManager.parse_pattern(pattern): action for pattern, action in actions.items()})

    def get_action(self, user_input: str) -> tuple[Action | None, dict[str, str] | None]:
        """"""
        for pattern, action in self.actions.items():
            if _match := match(pattern, user_input):
                return action, _match.groupdict()

        return None, None

    @staticmethod
    def parse_pattern(pattern: str) -> str:
        regex = r'^'

        for word in pattern.split(' '):
            if len(regex) > 1:
                regex += ' '

            regex += f'{ActionManager._determiners}(?P<{word}>.*)' if word.isupper(
            ) else word

        return regex + r'$'
