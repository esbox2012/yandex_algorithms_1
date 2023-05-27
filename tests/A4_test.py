import unittest
from lecture_4.A4 import find_synonym


class Test_A4(unittest.TestCase):
    def test_find_synonym(self):
        self.assertEqual(find_synonym(['hi bye'], 'bye'), 'hi')
        self.assertEqual(find_synonym(['hi bye', 'beep car'], 'car'), 'beep')
        self.assertEqual(find_synonym(['hi bye', '123 456'], '123'), '456')
        with self.assertRaises(ValueError):
            find_synonym(['hi bye'], '')
        with self.assertRaises(TypeError):
            find_synonym(['hi bye'], 123)


if __name__ == '__main__':
    unittest.main()
