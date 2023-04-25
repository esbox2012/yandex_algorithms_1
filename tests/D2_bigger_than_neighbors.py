from unittest import TestCase, main
from lecture_2.D2 import counter


class Bigger_than_neighbors_test(TestCase):

    def test_constant_seq(self):
        self.assertEqual(counter('1 1 1 1 1'), 0)

    def test_increasing_seq(self):
        self.assertEqual(counter('1 2 3 4 5'), 0)

    def test_decreasing_seq(self):
        self.assertEqual(counter('5 4 3 2 1'), 0)

    def test_random_seq(self):
        self.assertEqual(counter('1 3 1 3 1'), 2)

    def test_3_numbers(self):
        self.assertEqual(counter('1 2 0'), 1)

    def test_2_numbers(self):
        self.assertEqual(counter('1 2'), 0)

    def test_1_number(self):
        self.assertEqual(counter('1'), 0)


if __name__ == '__main__':
    main()
