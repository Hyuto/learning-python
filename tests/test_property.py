import unittest
from src.property import *


class TestHuman(unittest.TestCase):
    def test_get_height(self):
        human = Human(1.7)
        self.assertEqual(human.get_height(), 1.7)
        # test inch
        self.assertAlmostEqual(human.get_height("inch"), 66.9291, 3)
        # test foot
        self.assertAlmostEqual(human.get_height("foot"), 5.57743, 3)
        # test Error
        self.assertRaises(KeyError, human.get_height, unit="cm")

    def test_height_property(self):
        expects = {"above average": 1.7, "average": 1.628, "below average": 1.5}
        for expected in expects:
            human = Human(expects[expected])
            self.assertEqual(human.desc, expected)
