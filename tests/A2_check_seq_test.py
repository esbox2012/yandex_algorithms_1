from unittest import TestCase, main
from lecture_2.A2 import check_seq


class CheckSeqTest(TestCase):
    def test_increasing_seq(self):
        self.assertEqual(check_seq('1 2 3'), 'YES')

    def test_non_decreasing_seq(self):
        self.assertEqual(check_seq('1 2 2'), 'NO')

    def test_decreasing_se1(self):
        self.assertEqual(check_seq('3 2 1'), 'NO')

    def test_non_increasing_seq(self):
        self.assertEqual(check_seq('3 2 2'), 'NO')

    def test_const_seq(self):
        self.assertEqual(check_seq('1 1 1'), 'NO')


if __name__ == '__main__':
    main()
