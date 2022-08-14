#!/usr/bin/python3
'''This is a module'''

import unittest
from datetime import datetime
from models.base_model import BaseModel
from uuid import uuid4


class TestBase(unittest.TestCase):
    '''This is a class'''
    def test_task3(self):
        '''This is a method'''
        a = BaseModel()
        b = BaseModel()
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertEqual(type(a.id), str)
        id1 = a.id
        id2 = b.id
        self.assertNotEqual(id1, id2)
        crat = a.created_at
        upat = a.updated_at
        new_upat = a.save()
        self.assertEqual(type(crat), datetime)
        self.assertNotEqual(crat, upat)
        self.assertNotEqual(crat, new_upat)
        self.assertNotEqual(upat, new_upat)
        dict_of_attr = a.to_dict()
        self.assertEqual(type(dict_of_attr), dict)
        self.assertIn("__class__", dict_of_attr)
        self.assertIn("created_at", dict_of_attr)
        self.assertIn("updated_at", dict_of_attr)

    def test_task4(self):
        '''This is a method'''
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(type(my_new_model.created_at), datetime)
        self.assertEqual(type(my_new_model.updated_at), datetime)
