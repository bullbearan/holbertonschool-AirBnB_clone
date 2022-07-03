#!/usr/bin/python3
'''This is a module'''

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    '''This is a class'''
    def test_attributes(self):
        '''This is a method'''
        a = City()
        self.assertTrue(hasattr(a, "state_id"))
        self.assertTrue(hasattr(a, "name"))
