from game.player import Player
import unittest

from game.creatures import GiantShrimp


class TestCreatures(unittest.TestCase):

    def test_shrimp_name(self):
        shrimp = GiantShrimp()
        self.assertEqual(shrimp.name, "Giant Shrimp")

    def test_shrimp_gift(self):
        shrimp = GiantShrimp()
        self.assertEqual(shrimp.gift, "slingshot")

    def test_shrimp_speak(self):
        shrimp = GiantShrimp()
        self.assertIn("token", shrimp.speak().lower())

    def test_add_item(self):
        player = Player()

        player.inventory.append("map")

        self.assertIn("map", player.inventory)

if __name__ == "__main__":
    unittest.main()