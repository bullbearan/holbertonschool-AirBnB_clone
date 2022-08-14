# AirBnB clone project
![Holberton logo](/assets/hbnb.png "hbnb")
## Description
### The AirBnB clone project consists of:
- #### The console and Storage
	- This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself), you won’t have to pay attention (take care) of how your objects are stored.  
	- This abstraction will also allow you to change the type of storage easily without updating all of your codebase.  
	- The console will be a tool to validate this storage engine.

- #### Web static
- #### MySQL storage
- #### Web framework - templating
- #### RESTful API
- #### Web dynamic
- #### Storage

So far only the **console** and part of the **storage** is covered.

## How to start the console
```bash
Type in your terminal the following command
./console
```

## Usage
### quit and help
```bash
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$
```
Keep in mind that after pressing ENTER key with an empty line won't do anything.
However, cmd class will execute what it had previously did by default.

### EOF
Exists the program.
```bash
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) EOF
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$
```

#### The following 5 commands below only support these classes: BaseModel, User, State, City, Amenity, Place, Review

### create
Creates a new instance of a class, saves it (to the JSON file) and prints the
id.
```bash
$ create <class_name>
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) 
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$
```

### show
Prints the string representation of an instance bases on the class name and id.
```bash
$ show <class_name> <class_id>
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) quit
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$
```

### destroy
Deletes an instance based on the class name and id(save the change into the JSON
file).
```bash
show <class_name> <class_id>
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) quit
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$
```

### all
Prints all string representation of all instances bases or not on the class
name.
```bash
$ all
$ all <class_name>
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) quit
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$
```

### update
Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
```bash
$ update <class_name> <id> <attribute_name> "<attribute_value>"
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) quit
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$
```

## "Special" usage
### User.all()
Retrieve all instances of a class.
```bash
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
(hbnb)
```

### User.count()
Retrieve the number of instances of a class.
```bash
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) User.count()
2
(hbnb)
```

### User.show("id") 
Retrieve an instance based on its ID.
```bash
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb)
```

### User.destroy("id)
Destroy an instance based on his ID.
```bash
ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.count()
1
(hbnb)
```

### User.update("id", "attribute\_name", "atribute\_value")
 update an instance based on his ID
 ```bash
 ahmed@ubuntu:~/holbertonschool-AirBnB_clone$ ./console.py
 (hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
(hbnb)
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb)
```

## Author
- Ahmed Elzowawi
