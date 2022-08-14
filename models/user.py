#!/usr/bin/python3
'''This is a method'''

from models.base_model import BaseModel


class User(BaseModel):
    '''This is a class'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
