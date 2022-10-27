import core.dungeon as dungeon


def start_engine() -> None:
    """
    """
    # Display once the current room
    while True:
        if dungeon.player.take_turn():
            pass

        # for character in dungeon.current_room.get_characters():
        #     character.take_turn()

        # increase turn count
        # Update all entities
