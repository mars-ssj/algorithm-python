import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from backtracking.pattern import Pattern

class TestPattern(unittest.TestCase):

    def test_pattern(self):
        p = Pattern('*')
        self.assertEqual(p.match('arc'), True)

if __name__ == '__main__':
    unittest.main()