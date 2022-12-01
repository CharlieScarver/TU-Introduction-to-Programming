class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b


b = B(1, 2)

#####

class Animal:
    pass

class Duck(Animal):
    pass
 
a = Animal()
b = Duck()

# isinstance(obj, class)
# Returns if obj is an object of that class

isinstance(5, int)      # True
isinstance(a, Animal)   # True
isinstance(b, Duck)     # True
isinstance(b, Animal)   # True!! due to Polymorphism

