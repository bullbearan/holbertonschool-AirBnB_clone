#!/usr/bin/python3
'''This is a module'''

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''This is a class'''
    def test_attributes(self):
        '''This is a method'''
        a = Review()
        self.assertTrue(hasattr(a, "place_id"))
        self.assertTrue(hasattr(a, "user_id"))
        self.assertTrue(hasattr(a, "text"))
