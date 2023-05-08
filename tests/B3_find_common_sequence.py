from unittest import TestCase, main
from lecture_3.B3 import find_common_sequence


class Test_find_common_sequence(TestCase):
    def test_random_sequences(self):
        self.assertEqual(find_common_sequence([1, 2, 3], [2, 3, 4]), [2, 3])

    def test_different_sequences(self):
        self.assertEqual(find_common_sequence([1, 2, 3], [4, 5, 6]), [])

    def test_common_sequences(self):
        self.assertEqual(find_common_sequence([1, 2, 3], [3, 2, 1]), [1, 2, 3])

    def test_empty_sequences_1(self):
        self.assertEqual(find_common_sequence([], [2, 3, 4]), [])

    def test_empty_sequences_2(self):
        self.assertEqual(find_common_sequence([], []), [])


if __name__ == '__main__':
    main()
