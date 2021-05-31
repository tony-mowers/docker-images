from unittest import TestCase

from simple.calc import do_add


class Test(TestCase):
    def test_do_add(self):
        self.assertEqual(9, do_add(7, 2))
