import random

class InvalidParameterError(Exception):
    def __init__(self, invalid_param):
        message = f"Invalid class parameter: {invalid_param}"
        super().__init__(message)

class InvalidAgeError(InvalidParameterError):
    def __init__(self):
        super().__init__("age")

# str name
class Person:
    def __init__(self, name, age):
        if type(name) != str:
            raise InvalidParameterError("name")
        elif type(age) != int:
            raise InvalidAgeError()

        self.name = name

    def make_sound():
        pass

class Student(Person):
    def make_sound():
        print("AAAA")

class Lecturer(Person):
    def make_sound():
        print("BBBB")

class Janitor(Person):
    def make_sound():
        print("CCCC")

p = Person("Alex", 25)
#p = Person(32, 25)
p = Person("Peter", "25")
print("Hi")
