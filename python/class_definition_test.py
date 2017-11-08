# -*- coding: utf-8 -*-
import unittest
from class_definition import Num


class TestNumMethods(unittest.TestCase):
    '''
        Test cases for Num Class
    '''

    def test_square(self):
        self.assertEqual(Num(2).square(), 4)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
