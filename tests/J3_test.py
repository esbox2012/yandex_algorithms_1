import unittest
from lecture_3.J3 import lang


class Test_J3(unittest.TestCase):

    def test_lang(self):
        self.assertEqual(lang([{'English'}, {'Russian'}, {'French'}]), (0, set(), 3, {'English', 'Russian', 'French'}))
        self.assertEqual(lang([{'English', 'Russian'}, {'Russian', 'English'}, {'French', 'Russian'}]),
                         (1, {'Russian'}, 3, {'English', 'Russian', 'French'}))
        self.assertEqual(lang([{'English'}, {'English'}, {'English'}]), (1, {'English'}, 1, {'English'}))
        with self.assertRaises(TypeError):
            lang(3)


if __name__ == '__main__':
    unittest.main()
