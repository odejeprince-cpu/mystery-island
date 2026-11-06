import copy
import unittest

import game


def do(player, *actions):
    """Apply several actions in a row."""
    for action in actions:
        game.apply_action(player, action)


def winning_moves():
    return ["go:Jungle", "take", "go:Cave", "take", "go:Old Bridge", "go:Lighthouse", "light"]


class TestMysteryIsland(unittest.TestCase):
    def setUp(self):
        self.player = game.new_game("Ada")

    def test_t1_new_game(self):
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)
        self.assertEqual(self.player["inventory"], [])

    def test_t2_invalid_action_changes_nothing(self):
        before = copy.deepcopy(self.player)
        game.apply_action(self.player, "banana")
        self.assertEqual(self.player, before)

    def test_t3_legal_move_costs_one_energy(self):
        do(self.player, "go:Jungle")
        self.assertEqual(self.player["location"], "Jungle")
        self.assertEqual(self.player["energy"], 4)

    def test_t4_wrong_direction_is_free(self):
        do(self.player, "go:Cave")
        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)

    def test_t5_rope_collected_once(self):
        do(self.player, "go:Jungle", "take", "take")
        self.assertEqual(self.player["inventory"].count("rope"), 1)
        self.assertEqual(self.player["energy"], 4)

    def test_t6_bridge_blocked_without_rope(self):
        do(self.player, "go:Jungle", "go:Cave", "take", "go:Old Bridge", "go:Lighthouse")
        self.assertEqual(self.player["location"], "Old Bridge")
        self.assertEqual(self.player["energy"], 2)
        self.assertFalse(game.can_cross_bridge(self.player))

    def test_t7_cannot_light_without_lantern(self):
        self.player["location"] = "Lighthouse"
        self.player["inventory"] = ["rope"]
        do(self.player, "light")
        self.assertFalse(self.player["won"])
        self.assertFalse(self.player["game_over"])

    def test_t8_correct_inventory_and_location_wins(self):
        do(self.player, *winning_moves())
        self.assertTrue(self.player["won"])
        self.assertTrue(game.is_over(self.player))
        self.assertEqual(self.player["energy"], 1)

    def test_t9_energy_exhaustion_loses(self):
        do(self.player, "go:Jungle", "go:Beach", "go:Jungle", "go:Beach", "go:Jungle")
        self.assertEqual(self.player["energy"], 0)
        self.assertTrue(self.player["game_over"])
        self.assertFalse(self.player["won"])

    def test_t10_replay_resets_everything(self):
        do(self.player, "go:Jungle", "take")
        fresh = game.new_game("Ada")
        self.assertEqual(fresh["location"], "Beach")
        self.assertEqual(fresh["energy"], 5)
        self.assertEqual(fresh["inventory"], [])
        self.assertIsNot(fresh["inventory"], self.player["inventory"])

    def test_no_moves_after_game_over(self):
        do(self.player, "swim")
        self.assertTrue(self.player["game_over"])
        do(self.player, "go:Jungle")
        self.assertEqual(self.player["location"], "Beach")

    def test_fruit_only_once_and_capped(self):
        do(self.player, "go:Jungle", "eat", "eat")
        self.assertEqual(self.player["energy"], 5)
        self.assertTrue(self.player["ate_fruit"])

    def test_energy_never_negative(self):
        do(self.player, "go:Jungle", "go:Beach", "go:Jungle", "go:Beach", "go:Jungle", "go:Beach")
        self.assertEqual(self.player["energy"], 0)


if __name__ == "__main__":
    unittest.main()