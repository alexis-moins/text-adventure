from abc import ABC, abstractmethod

from core.entities import Character, Player
from core.actions.functions import register_action


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


class AttackAction(Action):

    def __init__(self, actor: Character) -> None:
        """
        Constructor creating a new attack action.

        Argument:
        actor - the character realizing the action
        """
        super().__init__(actor)

    def validate(self, parameters: list[str]) -> bool:
        """
        """
        match parameters:
            case [target, 'with', weapon]:
                # target = dungeon.current_room.entities.find(target)
                #
                # if not target:
                #   raise ActionException('I don\'t see anything like that here!')
                #
                # if not isinstance(target, NPC):
                #   raise ActionException(f'Trying to ... {target.determiner} {target.name} ? What a silly idea...')
                #
                pass

            case _:
                raise ActionException(
                    'Am I supposed to guess the target of the attack ?!')


register_action('attack', AttackAction)
