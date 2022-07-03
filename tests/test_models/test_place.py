#!/usr/bin/python3
'''This is a module'''

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''This is a class'''
    def test_attributes(self):
        '''This is a method'''
        a = Place()
        self.assertTrue(hasattr(a, "city_id"))
        self.assertTrue(hasattr(a, "user_id"))
        self.assertTrue(hasattr(a, "name"))
        self.assertTrue(hasattr(a, "description"))
        self.assertTrue(hasattr(a, "number_bathrooms"))
        self.assertTrue(hasattr(a, "max_guest"))
        self.assertTrue(hasattr(a, "price_by_night"))
        self.assertTrue(hasattr(a, "latitude"))
        self.assertTrue(hasattr(a, "longitude"))
        self.assertTrue(hasattr(a, "amenity_ids"))
