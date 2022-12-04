
# OOP - Classes and Objects

name = "Alex"
specialty = "Computer Science"

name2 = "Ivan"
specialty2 = "Electrical Engineering"

# We can use a class to combine these properties into Student objects

class Student:
    uni = "TU"

    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

student1 = Student("Alex", "Computer Science")
student2 = Student("Ivan", "Electrical Engineering")
print(student1, student1.name, student1.specialty)
print(type(student1))
print(Student.uni)

dir()           # list with local names
vars()          # same as locals() - dict with local names-values
vars(student1)  # {'name': 'Alex', 'specialty': 'Computer Science'}

# Define Student with name and grade and
# a boolean method check_if_passes() that uses the grade

print()

### EmptyClass

class EmptyClass:
    pass

empty = EmptyClass()
print(empty)

empty.name = "Petar"
print(empty.name)

print()

### EmptyClass

class Dog:
    def bark(self):
        print("Woof!")

class Cat:
    def __init__(self, name):
        self.name = name
    
    def meow(self):
        print("Meow!")


dog = Dog()
print(dog)
dog.bark()

cat = Cat('Fluffers')
print(cat)
print(cat.name)
cat.meow()

