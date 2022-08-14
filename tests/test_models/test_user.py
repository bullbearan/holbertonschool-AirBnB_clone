#!/usr/bin/python3
'''This is a module'''

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''This is a class'''
    def test_attributes(self):
        '''This is a method'''
        a = User()
        self.assertTrue(hasattr(a, "email"))
        self.assertTrue(hasattr(a, "password"))
        self.assertTrue(hasattr(a, "first_name"))
        self.assertTrue(hasattr(a, "last_name"))
