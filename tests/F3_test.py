from unittest import TestCase, main
from lecture_3.F3 import make_pairs, make_genome_dict, similarity


class Test_F3(TestCase):

    def test_make_pairs(self):
        self.assertEqual(make_pairs('ABCD'), ['AB', 'BC', 'CD'])
        self.assertEqual(make_pairs('AAAA'), ['AA', 'AA', 'AA'])
        self.assertEqual(make_pairs(''), [])
        with self.assertRaises(TypeError):
            make_pairs([1, 2])

    def test_make_genome_dict(self):
        self.assertEqual(make_genome_dict(['AB', 'BC', 'CD']), {'AB': 1, 'BC': 1, 'CD': 1})
        self.assertEqual(make_genome_dict(['AA', 'AA', 'AA']), {'AA': 3})
        self.assertEqual(make_genome_dict([]), dict())
        with self.assertRaises(TypeError):
            make_genome_dict('ABCD')

    def test_similarity(self):
        self.assertEqual(similarity('ABC', 'ABC'), 2)
        self.assertEqual(similarity('ABC', 'CDE'), 0)
        self.assertEqual(similarity('ABAB', 'AB'), 2)
        self.assertEqual(similarity('', ''), 0)
        with self.assertRaises(TypeError):
            similarity([1, 2, 3], [4, 5, 6])


if __name__ == '__main__':
    main()
