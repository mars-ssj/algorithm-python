import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from dp.knapsack import Knapsack

class TestKnapsack(unittest.TestCase):

    def test_solution_max_weight(self):
        weights = [2, 2, 4, 6, 3]
        k = Knapsack()
        result = k.solution_max_weight(weights, 9, len(weights))
        self.assertEqual(result, 9)
    
    def test_solution_max_weight2(self):
        weights = [2, 2, 4, 6, 3]
        k = Knapsack()
        result = k.solution_max_weight2(weights, 9, len(weights))
        self.assertEqual(result, 9)
    
    def test_solution_max_value(self):
        weights = [2, 2, 4, 6, 3]
        values = [3, 4, 8, 9, 6]
        k = Knapsack()
        result = k.solution_max_value(weights, 9, len(weights), values)
        self.assertEqual(result, 18)

    def test_solution_max_value2(self):
        weights = [2, 2, 4, 6, 3]
        values = [3, 4, 8, 9, 6]
        k = Knapsack()
        result = k.solution_max_value2(weights, 9, len(weights), values)
        self.assertEqual(result, 18)


if __name__ == '__main__':
    unittest.main()