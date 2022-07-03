#!/usr/bin/python3
'''This is a method'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''This is a class'''
    place_id = ""
    user_id = ""
    text = ""
