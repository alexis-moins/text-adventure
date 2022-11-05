from core.entities import Character

from core.actions.functions import register_action
from core.actions.exception import ActionException

from core.actions import BaseAction


class AttackAction(BaseAction):

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
            case [*target, 'with', weapon]:
                # target = dungeon.current_room.entities.find(target)
                #
                # if not target:
                #   raise ActionException('I don\'t see anything like that here!')
                #
                # if not isinstance(target, NPC):
                #   raise ActionException(f'Trying to ... {target.determiner} {target.name} ? What a silly idea...')
                #
                print(f'success -> {target=} {weapon=}')

            case _:
                raise ActionException(
                    'Am I supposed to guess the target of the attack ?!')

    def _execute(self, parameters: list[str]) -> None:
        pass


register_action('attack', AttackAction)
