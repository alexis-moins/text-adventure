from importlib import import_module
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def use(modules: list[str]) -> None:
    """
    """
    for module in modules:
        import_module(module)

    print()
