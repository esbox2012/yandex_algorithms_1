from unittest import TestCase, main
from lecture_3.G3 import count_honest_turtles


class Test_G3(TestCase):

    def test_count_honest_turtles(self):
        self.assertEqual(count_honest_turtles(['1 1', '0 2', '2 0'], 3), 3)
        self.assertEqual(count_honest_turtles(['1 1', '2 1', '1 2'], 3), 1)
        self.assertEqual(count_honest_turtles(['1 1', '1 1', '1 1'], 3), 1)
        with self.assertRaises(TypeError):
            count_honest_turtles(['1 1', '0 2', '2 0'], 'ABC')


if __name__ == '__main__':
    main()
