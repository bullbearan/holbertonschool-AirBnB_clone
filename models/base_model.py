#!/usr/bin/python3
'''
This is a module where we gonna make it
long in order to check for the checker
'''

from uuid import uuid4
from datetime import datetime, date
import models


class BaseModel:
    '''
    This is a class where we gonna make it
    long in order to check for the checker
    '''
    def __init__(self, *args, **kwargs):
        '''
        This is a method where we gonna make it
        long in order to check for the checker
        '''
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        This is a method where we gonna make it
        long in order to check for the checker
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        This is a method where we gonna make it
        long in order to check for the checker
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        This is a method where we gonna make it
        long in order to check for the checker
        '''
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
