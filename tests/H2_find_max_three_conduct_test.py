from unittest import TestCase, main
from lecture_2.H2 import find_max_three_conduct


class Test_find_max_three_conduct(TestCase):

    def test_increasing_positive_seq(self):
        self.assertEqual(find_max_three_conduct([1, 2, 3, 4, 5]), (5, 4, 3))

    def test_constant_positive_seq(self):
        self.assertEqual(find_max_three_conduct([1, 1, 1, 1, 1]), (1, 1, 1))

    def test_decreasing_positive_seq(self):
        self.assertEqual(find_max_three_conduct([5, 4, 3, 2, 1]), (5, 4, 3))

    def test_increasing_negative_seq(self):
        self.assertEqual(find_max_three_conduct([-5, -4, -3, -2, -1]), (-1, -2, -3))

    def test_constant_negative_seq(self):
        self.assertEqual(find_max_three_conduct([-1, -1, -1, -1, -1]), (-1, -1, -1))

    def test_decreasing_negative_seq(self):
        self.assertEqual(find_max_three_conduct([-1, -2, -3, -4, -5]), (-1, -2, -3))


if __name__ == '__main__':
    main()
