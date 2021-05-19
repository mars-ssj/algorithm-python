import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from backtracking.queens import Queens

class TestPattern(unittest.TestCase):

    def test_pattern(self):
        p = Queens()
        p.cal_8_queens(0)

if __name__ == '__main__':
    unittest.main()