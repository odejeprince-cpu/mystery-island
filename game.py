"""Game rules for Mystery Island. No input() or print() in this file."""

MAX_ENERGY = 5

MAP = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"],
}

ITEMS = {"Jungle": "rope", "Cave": "lantern"}

SCENES = {
    "Beach": "You stand on a windy beach. Broken planks wash ashore.",
    "Jungle": "Thick jungle. Fruit hangs from the trees and a rope lies coiled on a root.",
    "Cave": "A damp cave. Something metal glints in the dark.",
    "Old Bridge": "A rotten rope bridge, broken in the middle, leads to the lighthouse.",
    "Lighthouse": "The lighthouse stands dark. The beacon is at the top.",
}


def new_game(name):
    """Return a fresh player dict. A new inventory list is created every time."""
    return {
        "name": name,
        "location": "Beach",
        "energy": MAX_ENERGY,
        "inventory": [],
        "ate_fruit": False,
        "game_over": False,
        "won": False,
    }


def can_cross_bridge(player):
    """True only if the player holds the rope."""
    return "rope" in player["inventory"]


def can_light_beacon(player):
    """True only at the Lighthouse with the lantern."""
    return player["location"] == "Lighthouse" and "lantern" in player["inventory"]


def describe(player):
    """Return the scene text for the current location."""
    return SCENES[player["location"]]


def available_actions(player):
    """Return the list of action strings the player can choose right now."""
    here = player["location"]
    actions = ["look"]
    for destination in MAP[here]:
        actions.append(f"go:{destination}")
    item = ITEMS.get(here)
    if item and item not in player["inventory"]:
        actions.append("take")
    if here == "Jungle" and not player["ate_fruit"]:
        actions.append("eat")
    if here == "Beach":
        actions.append("swim")
    if here == "Lighthouse":
        actions.append("light")
    return actions


def label(player, action):
    """Return the menu text for an action."""
    if action == "look":
        return "Look around"
    if action.startswith("go:"):
        return f"Go to {action[3:]}"
    if action == "take":
        return f"Pick up the {ITEMS[player['location']]}"
    if action == "eat":
        return "Eat the jungle fruit"
    if action == "swim":
        return "Swim straight for the lighthouse"
    if action == "light":
        return "Light the beacon"
    return action


def is_over(player):
    """True if the game has been won or lost."""
    return player["game_over"]


def _move(player, destination):
    here = player["location"]
    if here == "Old Bridge" and destination == "Lighthouse" and not can_cross_bridge(player):
        return "The bridge is broken in the middle. You need a rope to cross."
    player["location"] = destination
    player["energy"] -= 1
    text = describe(player)
    if player["energy"] <= 0:
        player["energy"] = 0
        player["game_over"] = True
        player["won"] = False
        text += "\nYou collapse from exhaustion. The rescue boat never comes."
    return text


def apply_action(player, action):
    """Apply an action and return a message. Rejected actions change nothing."""
    if player["game_over"]:
        return "The game is over."
    if action not in available_actions(player):
        return "You can't do that right now."

    if action == "look":
        return describe(player)

    if action.startswith("go:"):
        return _move(player, action[3:])

    if action == "take":
        item = ITEMS[player["location"]]
        player["inventory"].append(item)
        return f"You pick up the {item}."

    if action == "eat":
        player["ate_fruit"] = True
        player["energy"] = min(MAX_ENERGY, player["energy"] + 1)
        return "The fruit is sweet. You regain 1 energy."

    if action == "swim":
        player["game_over"] = True
        player["won"] = False
        player["energy"] = 0
        return "The current is too strong. The sea pulls you under."

    if action == "light":
        if can_light_beacon(player):
            player["game_over"] = True
            player["won"] = True
            return "The beacon blazes. A rescue boat turns toward the island!"
        return "It is pitch dark and you have nothing to light the beacon with. You need the lantern."

    return "You can't do that right now."