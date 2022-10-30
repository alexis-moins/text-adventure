import core.dungeon as dungeon


def start_engine() -> None:
    """
    """
    # Display once the current room
    print(dungeon.current_room)

    while True:
        action_costs_a_turn = dungeon.player.take_turn()

        if not action_costs_a_turn:
            continue

        for character in dungeon.current_room.get_characters():
            character.take_turn()

        dungeon.turn += 1

        # Update all entities
