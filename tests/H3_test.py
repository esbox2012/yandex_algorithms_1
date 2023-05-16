import unittest
from lecture_3.H3 import shots


class Test_H3(unittest.TestCase):
    def test_shots(self):
        self.assertEqual(shots(['1 1', '2 3', '-1 6']), 3)
        self.assertEqual(shots(['1 1', '2 2', '3 3']), 3)
        self.assertEqual(shots(['1 1', '1 2', '1 3']), 1)
        self.assertEqual(shots(['-1 -1', '-1 -2', '-1 -3']), 1)
        with self.assertRaises(TypeError):
            shots('ABC')


if __name__ == '__main__':
    unittest.main()
