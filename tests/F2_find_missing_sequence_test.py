from unittest import TestCase, main
from lecture_2.F2 import find_missing_sequence


class Test_find_missing_sequence(TestCase):

    def test_good_sequence_1(self):
        self.assertEqual(find_missing_sequence(['1', '2', '3', '4', '5', '4'], 6), '3\n3 2 1')

    def test_good_sequence_2(self):
        self.assertEqual(find_missing_sequence(['3', '2', '3', '5', '4'], 5), '4\n5 3 2 3')

    def test_nothing_to_add(self):
        self.assertEqual(find_missing_sequence(['1', '2', '3', '2', '1'], 5), '0\n')

    def test_shortest_sequence(self):
        self.assertEqual(find_missing_sequence(['1'], 1), '0')


if __name__ == '__main__':
    main()
