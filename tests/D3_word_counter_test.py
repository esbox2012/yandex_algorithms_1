from unittest import TestCase, main
from lecture_3.D3 import word_counter


class Test_word_counter(TestCase):

    def test_text_with_whitespace(self):
        self.assertEqual(word_counter('one two three'), 3)

    def test_text_with_whitespaces(self):
        self.assertEqual(word_counter('one   two      three'), 3)

    def test_text_with_tab(self):
        self.assertEqual(word_counter('one\ntwo\nthree'), 3)

    def test_text_with_tabs(self):
        self.assertEqual(word_counter('one\n\ntwo\n\nthree'), 3)

    def test_text_with_whitespace_tab(self):
        self.assertEqual(word_counter('one two\nthree'), 3)

    def test_text_with_whitespace_tab_2(self):
        self.assertEqual(word_counter('one \n\ntwo\n three'), 3)

    def test_no_text(self):
        self.assertEqual(word_counter(''), 0)


if __name__ == '__main__':
    main()
