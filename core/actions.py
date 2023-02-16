from core.world import World


def say(_: World, args: dict[str, str]):
    print('You "' + args['THING'] + '"')
