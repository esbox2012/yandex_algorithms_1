from unittest import TestCase, main
from yandex_algorithms_1.A2 import check_seq

class CheckSeqTest(TestCase):
    def increasing_seq(self):
        self.assertEqual(check_seq('1 2 3'),'YES')

if __name__ == '__main__':
    main()