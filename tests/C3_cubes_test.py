from unittest import TestCase, main
from lecture_3.C3 import cubes


class Test_cubes(TestCase):
    def test_random_cubes(self):
        self.assertEqual(cubes([1, 2, 3], [3, 4, 5]), (1, [3], 2, [1, 2], 2, [4, 5]))

    def test_common_cubes(self):
        self.assertEqual(cubes([1, 2, 3], [3, 2, 1]), (3, [1, 2, 3], 0, [], 0, []))

    def test_different_cubes(self):
        self.assertEqual(cubes([1, 2, 3], [4, 5, 6]), (0, [], 3, [1, 2, 3], 3, [4, 5, 6]))

    def test_empty_cubes_1(self):
        self.assertEqual(cubes([1, 2, 3], []), (0, [], 3, [1, 2, 3], 0, []))

    def test_empty_cubes_2(self):
        self.assertEqual(cubes([], []), (0, [], 0, [], 0, []))


if __name__ == '__main__':
    main()
