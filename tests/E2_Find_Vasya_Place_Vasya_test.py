from unittest import TestCase, main
from lecture_2.E2 import Find_Vasya, Place_Vasya


class Test_Find_Vasya(TestCase):

    def test_constant_seq(self):
        self.assertEqual(Find_Vasya([1, 1, 1], 0), [])

    def test_decreasing_seq(self):
        self.assertEqual(Find_Vasya([3, 2, 1], 3), [])

    def test_decreasing_seq_with_5(self):
        self.assertEqual(Find_Vasya([25, 15, 5], 3), [15])

    def test_incr_seq(self):
        self.assertEqual(Find_Vasya([1, 2, 3], 3), [])

    def test_incr_seq_with_5(self):
        self.assertEqual(Find_Vasya([5, 15, 25], 3), [])


class Test_Place_Vasya(TestCase):

    def test_one_key(self):
        self.assertEqual(Place_Vasya([25, 15, 5], [15], 3), 2)

    def test_many_keys(self):
        self.assertEqual(Place_Vasya([25, 15, 24, 5, 1], [15, 5], 5), 3)

    def test_no_keys(self):
        self.assertEqual(Place_Vasya([1, 2, 3], [], 3), 0)


if __name__ == '__main__':
    main()
