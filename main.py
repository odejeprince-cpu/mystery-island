import game


def play(name):
    """Run one game. Return True if it finished, False if the player quit."""
    player = game.new_game(name)
    print()
    print(game.describe(player))

    while not game.is_over(player):
        actions = game.available_actions(player)
        inventory = ", ".join(player["inventory"]) or "empty"
        print(f"\nLocation: {player['location']} | Energy: {player['energy']} | Inventory: {inventory}")
        for number, action in enumerate(actions, start=1):
            print(f"{number}. {game.label(player, action)}")
        print("q. Quit")

        choice = input("> ").strip().lower()

        if choice in ("q", "quit", "exit"):
            print("Goodbye!")
            return False

        if not choice.isdigit() or not 1 <= int(choice) <= len(actions):
            print(f"Invalid choice. Enter a number from 1 to {len(actions)}, or q.")
            continue

        print(game.apply_action(player, actions[int(choice) - 1]))

    if player["won"]:
        print(f"\n*** YOU WIN, {name}! ***")
    else:
        print(f"\n*** GAME OVER, {name}. ***")
    return True


def main():
    print("====== MYSTERY ISLAND: THE LOST LIGHTHOUSE ======")
    print("You wake up on an island after a storm. Light the beacon to be rescued.")
    print("Every move costs 1 energy. Find the rope and the lantern first.")

    name = input("Enter your name: ").strip() or "Stranger"
    print(f"Welcome, {name}!")

    while True:
        finished = play(name)
        if not finished:
            break
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()