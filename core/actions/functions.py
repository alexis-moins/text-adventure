from core.actions.base_action import BaseAction


# Dictionary of all the available actions
actions: dict[str, BaseAction] = dict()


def get_action(name: str) -> BaseAction | None:
    """
    Return the action matching the given name or None if no action
    is found.

    Argument:
    name - the name of the action

    Returns:
    A class to instanciate to execute the action or None
    """
    return actions.get(name, None)


def register_action(name: str, _class: BaseAction, *, override: bool = False) -> bool:
    """
    Register a new action.

    Arguments:
    name - the name of the action. Corresponds to the text that the user
    will have to type to trigger the action

    _class - the class that will be instanciated

    override - whether or not to override any pre-existing action

    Returns:
    True if the operation succeeds, False otherwise
    """
    if name in actions and not override:
        return False

    actions[name] = _class
    return True
