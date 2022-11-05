from core.engine.functions import start_engine
from core.loader import use

modules = [
    'core.actions.list.attack'
]

use(modules)

start_engine()
