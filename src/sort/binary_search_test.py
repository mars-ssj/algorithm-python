import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from sort.binary_search import BinarySearch, BinarySearchApplication

class TestBinarySearch(unittest.TestCase):

    def test_solution1(self):
        array = [8, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        bs = BinarySearch()
        self.assertEqual(bs.solution1(array, 19), 2)
        self.assertEqual(bs.solution1(array, 28), -1)
        self.assertEqual(bs.solution1(array, 8), 0)
        self.assertEqual(bs.solution1(array, 98), len(array)-1)

    def test_solution2(self):
        array = [8, 11, 19, 23, 27, 33, 45, 55, 67, 98]
        bs = BinarySearch()
        self.assertEqual(bs.solution2(array, 19), 2)
        self.assertEqual(bs.solution2(array, 28), -1)
        self.assertEqual(bs.solution2(array, 8), 0)
        self.assertEqual(bs.solution2(array, 98), len(array)-1)
    
    def test_square_root(self):
        bsa = BinarySearchApplication()
        self.assertEqual(bsa.square_root(5, 0.000001), 2.236068)
    
    def test_solution3(self):
        array = [8, 11, 19, 19, 19, 19, 23, 27, 33, 45, 55, 67, 98]
        bs = BinarySearch()
        self.assertEqual(bs.solution3(array, 19), 2)
        self.assertEqual(bs.solution4(array, 19), 5)
        self.assertEqual(bs.solution5(array, 19), 2)
        self.assertEqual(bs.solution6(array, 19), 5)

if __name__ == '__main__':
    unittest.main()
