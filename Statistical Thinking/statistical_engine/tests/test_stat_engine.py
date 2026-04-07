import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from stat_engine import StatEngine
import unittest
import math

class TestStatEngine(unittest.TestCase):

    def test_mean_median_odd_list(self):
        data = [1, 3, 5]
        engine = StatEngine(data)
        self.assertEqual(engine.get_mean(), 3)
        self.assertEqual(engine.get_median(), 3)

    def test_mean_median_even_list(self):
        data = [2, 4, 6, 8]
        engine = StatEngine(data)
        self.assertEqual(engine.get_mean(), 5)
        self.assertEqual(engine.get_median(), 5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            engine = StatEngine([])

    def test_standard_deviation_known(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        engine = StatEngine(data)
        self.assertAlmostEqual(engine.get_standard_deviation(), 2.0, places=5)

if __name__ == '__main__':
    unittest.main()