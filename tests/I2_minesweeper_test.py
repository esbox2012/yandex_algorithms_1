from unittest import TestCase, main
from lecture_2.I2 import minesweeper


class Test_minesweeper(TestCase):

    def test_1_mine(self):
        self.assertEqual(minesweeper(['2 2'], 3, 3), [[1, 1, 1], [1, '*', 1], [1, 1, 1]])

    def test_3_mines(self):
        self.assertEqual(minesweeper(['2 1', '2 2', '2 3'], 3, 3), [[2, 3, 2], ['*', '*', '*'], [2, 3, 2]])

    def test_9_mines(self):
        self.assertEqual(minesweeper(['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3'], 3, 3),
                         [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']])

    def test_empty(self):
        self.assertEqual(minesweeper([], 3, 3), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])


if __name__ == '__main__':
    main()
