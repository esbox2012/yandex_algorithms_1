from unittest import TestCase, main
from lecture_2.D2 import bigger_than_neighbors


class Bigger_than_neighbors_test(TestCase):

    def test_constant_seq(self):
        self.assertEqual(bigger_than_neighbors('1 1 1 1 1'), 0)

    def test_increasing_seq(self):
        self.assertEqual(bigger_than_neighbors('1 2 3 4 5'), 0)

    def test_decreasing_seq(self):
        self.assertEqual(bigger_than_neighbors('5 4 3 2 1'), 0)

    def test_random_seq(self):
        self.assertEqual(bigger_than_neighbors('1 3 1 3 1'), 2)

    def test_3_numbers(self):
        self.assertEqual(bigger_than_neighbors('1 2 0'), 1)

    def test_2_numbers(self):
        self.assertEqual(bigger_than_neighbors('1 2'), 0)

    def test_1_number(self):
        self.assertEqual(bigger_than_neighbors('1'), 0)


if __name__ == '__main__':
    main()
