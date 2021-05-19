import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from backtracking.knapsack import Knapsack
from backtracking.knapsack import KnapsackMaxValue

class TestPattern(unittest.TestCase):

    def test_max_weight(self):
        p = Knapsack()
        weights = [2, 2, 4, 6, 3]
        p.solution(weights, 9)
        self.assertEqual(p.max_weight, 9)
    
    def test_max_value(self):
        k = KnapsackMaxValue()
        weights = [2, 2, 4, 6, 3]
        values = [3, 4, 8, 9, 6]
        k.solution(weights, 9, values)
        self.assertEqual(k.max_value, 18)

if __name__ == '__main__':
    unittest.main()