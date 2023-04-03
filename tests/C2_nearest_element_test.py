from unittest import TestCase, main
from lecture_2.C2 import nearest_element


class Nearest_element_test(TestCase):
    def test_increasing_seq(self):
        self.assertEqual(nearest_element('5\n1 2 3 4 5\n3'), 3)

    def test_increasing_seq_without_x(self):
        self.assertEqual(nearest_element('5\n1 2 4 6 7\n3'), 4)

    def test_decreasing_seq(self):
        self.assertEqual(nearest_element('5\n5 4 3 2 1\n5'), 5)

    def test_decreasing_seq_without_x(self):
        self.assertEqual(nearest_element('5\n5 4 3 2 1\n6'), 5)

    def test_constant_seq(self):
        self.assertEqual(nearest_element('5\n1 1 1 1 1\n1'), 1)

    def test_constant_seq_without_x(self):
        self.assertEqual(nearest_element('5\n1 1 1 1 1\n2'), 1)


if __name__ == '__main__':
    main()
