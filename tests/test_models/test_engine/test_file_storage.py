#!/usr/bin/python3
'''This is a module'''

import unittest
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    '''This is a class'''
    def test_task5(self):
        '''This is a method'''
        a = FileStorage()
        self.assertEqual(type(a.all()), dict)
