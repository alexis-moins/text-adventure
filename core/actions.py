from core.world import World


def say(_: World, args: dict[str, str]):
    print('You "' + args['THING'] + '"')

def drink(_: World, args: dict[str, str]):
    pass

def take(_: World, args):
    pass
