#!/usr/bin/python3
'''This is a module'''

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''This is a class'''
    def test_attributes(self):
        '''This is a method'''
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
