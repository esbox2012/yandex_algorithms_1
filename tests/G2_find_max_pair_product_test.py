from unittest import TestCase, main
from lecture_2.G2 import find_max_pair_product


class Test_find_max_pair_product(TestCase):

    def test_positive_seq(self):
        self.assertEqual(find_max_pair_product([1, 2, 3, 4, 5, 6]), (5, 6))

    def test_positive_seq_2(self):
        self.assertEqual(find_max_pair_product([6, 5, 4, 3, 2, 1]), (5, 6))

    def test_negative_seq(self):
        self.assertEqual(find_max_pair_product([-1, -2, -3, -4, -5, -6]), (-6, -5))

    def test_negative_seq2(self):
        self.assertEqual(find_max_pair_product([-6, -5, -4, -3, -2, -1]), (-6, -5))

    def test_mix_seq(self):
        self.assertEqual(find_max_pair_product([-1, -2, -3, 4, 5, 6]), (5, 6))

    def test_mix_seq2(self):
        self.assertEqual(find_max_pair_product([-1, -2, -3, 3, 2, 1]), (2, 3))


if __name__ == '__main__':
    main()
