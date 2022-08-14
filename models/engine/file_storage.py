#!/usr/bin/python3
'''This is a module'''

import json
from os.path import isfile
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''This is a class'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''This is a method'''
        return self.__objects

    def new(self, obj):
        '''This is a method'''
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        '''This is a method'''
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        '''This is a mehtod'''
        if isfile(self.__file_path):
            with open(self.__file_path) as f:
                json_format = json.load(f)
            for key, value in json_format.items():
                self.__objects[key] = eval(value['__class__'])(**value)
