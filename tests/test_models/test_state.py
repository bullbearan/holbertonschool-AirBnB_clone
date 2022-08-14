#!/usr/bin/python3
'''This is a module'''

import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''This is a class'''
    def test_attributes(self):
        '''This is a method'''
        a = State()
        self.assertTrue(hasattr(a, "name"))
