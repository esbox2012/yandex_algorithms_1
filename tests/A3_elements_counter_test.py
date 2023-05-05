from unittest import TestCase, main
from lecture_3.A3 import elements_counter


class Test_elements_counter(TestCase):
    def test_diff_seq(self):
        self.assertEqual(elements_counter([1, 2, 3, 4, 5]), 5)

    def test_diff_seq_2(self):
        self.assertEqual(elements_counter([-1, -2, -3, -4, -5]), 5)

    def test_constant_seq(self):
        self.assertEqual(elements_counter([1, 1, 1, 1, 1]), 1)

    def test_empty_seq(self):
        self.assertEqual(elements_counter([]), 0)
