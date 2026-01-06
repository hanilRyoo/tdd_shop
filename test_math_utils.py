# test_math_utils.py

import unittest
import math_utils  # 같은 폴더에 있는 math_utils.py

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        result = math_utils.add(2, 3)
        self.assertEqual(result, 5)

    def test_sub(self):
        result = math_utils.sub(10, 4)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()