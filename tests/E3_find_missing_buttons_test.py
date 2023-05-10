from unittest import TestCase, main
from lecture_3.E3 import find_missing_buttons


class Test_find_missing_buttons(TestCase):

    def test_no_common_buttons(self):
        self.assertEqual(find_missing_buttons([1, 2, 3], '456'), 3)

    def test_only_common_buttons(self):
        self.assertEqual(find_missing_buttons([1, 2, 3], '123'), 0)

    def test_some_common_buttons(self):
        self.assertEqual(find_missing_buttons([1, 2, 3], '453'), 2)

    def test_no_buttons(self):
        self.assertEqual(find_missing_buttons([1, 2, 3], ''), 0)


if __name__ == '__main__':
    main()
