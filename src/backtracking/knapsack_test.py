import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from backtracking.knapsack import Knapsack

class TestPattern(unittest.TestCase):

    def test_pattern(self):
        p = Knapsack()
        weights = [2, 2, 4, 5, 6, 3]
        p.dp(0, 0, 9, weights, 6)
        self.assertEqual(p.max_weight, 9)

if __name__ == '__main__':
    unittest.main()