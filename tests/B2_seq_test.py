from unittest import TestCase, main
from lecture_2.B2 import seq


class seq_test(TestCase):
    def test_constant_seq(self):
        self.assertEqual(seq('4\n4\n4\n-2000000000'), 'CONSTANT')

    def test_ascending_seq(self):
        self.assertEqual(seq('1\n2\n3\n-2000000000'), 'ASCENDING')

    def test_weakly_ascending_seq(self):
        self.assertEqual(seq('1\n1\n2\n-2000000000'), 'WEAKLY ASCENDING')

    def test_descending_seq(self):
        self.assertEqual(seq('3\n2\n1\n-2000000000'), 'DESCENDING')

    def test_weakly_descending_seq(self):
        self.assertEqual(seq('3\n3\n1\n-2000000000'), 'WEAKLY DESCENDING')


if __name__ == '__main__':
    main()
