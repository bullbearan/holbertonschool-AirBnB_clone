#!/usr/bin/python3
'''This is a method'''

import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
commands = ["all", "count", "show", "destroy", "update"]


def check_digit(str_num):
    '''This is a function'''
    if str_num is not str:
        return False
    for i in str_num:
        if i == "-" or i == "+" or i == ".":
            continue
        if ord(i) < 48 or ord(i) > 57:
            return False
    return True


class HBNBCommand(cmd.Cmd):
    '''This is a class'''
    prompt = "(hbnb) "

    def default(self, line):
        arg = re.split("[.(), \"\"]+", line)
        if arg[0] in classes and arg[1] in commands:
            if arg[1] == "all":
                self.do_all(arg[0])
            elif arg[1] == "count":
                counter = 0
                dict_of_objs = storage.all()
                for key in dict_of_objs:
                    if arg[0] in key:
                        counter += 1
                print(counter)
            elif arg[1] == "show":
                self.do_show(f"{arg[0]} {arg[2]}")
            elif arg[1] == "destroy":
                self.do_destroy(f"{arg[0]} {arg[2]}")
            elif arg[1] == "update":
                print(arg)
                self.do_update(f"{arg[0]} {arg[2]} {arg[3]} \"{arg[4]}\"")
        else:
            cmd.Cmd.default(self, line)

    def do_quit(self, arg):
        '''Quit command to exit the program
        '''
        return True

    def emptyline(self):
        '''This is a method'''
        pass

    def do_EOF(self, arg):
        '''This is a method'''
        print()
        return True

    def do_create(self, arg):
        '''This is a method'''
        if arg == "":
            print("** class name missing **")
            return
        arg = arg.split(" ")
        if arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj = eval(arg[0])()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        '''This is a method'''
        if arg == "":
            print("** class name missing **")
            return
        arg = arg.split(" ")
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        dict_of_objs = storage.all()
        if f"{arg[0]}.{arg[1]}" in dict_of_objs:
            print(dict_of_objs[f"{arg[0]}.{arg[1]}"])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        '''This is a method'''
        if arg == "":
            print("** class name missing **")
            return
        arg = arg.split(" ")
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        dict_of_objs = storage.all()
        if f"{arg[0]}.{arg[1]}" in dict_of_objs:
            del dict_of_objs[f"{arg[0]}.{arg[1]}"]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        '''This is a method'''
        list_of_objs = []
        dict_of_objs = storage.all()
        if arg == "":
            for value in dict_of_objs.values():
                list_of_objs.append(str(value))
        else:
            if arg in classes:
                for key, value in dict_of_objs.items():
                    if arg in key:
                        list_of_objs.append(str(value))
            else:
                print("** class doesn't exist **")
                return
        print(list_of_objs)

    def do_update(self, arg):
        '''This is a method'''
        if arg == "":
            print("** class name missing **")
            return
        arg = arg.split(" ")
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        dict_of_objs = storage.all()
        if f"{arg[0]}.{arg[1]}" not in dict_of_objs:
            print("** no instance found **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return
        if len(arg) > 3:
            value = eval(arg[3])
            if check_digit(value):
                try:
                    n = int(value)
                    setattr(dict_of_objs[f"{arg[0]}.{arg[1]}"], arg[2], n)
                except Exception:
                    f = float(value)
                    setattr(dict_of_objs[f"{arg[0]}.{arg[1]}"], arg[2], f)
            else:
                setattr(dict_of_objs[f"{arg[0]}.{arg[1]}"], arg[2], value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
