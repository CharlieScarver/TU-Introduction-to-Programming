import random

class Animal:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def make_sound(self):
        pass

    def eat_food(self, available):
        pass

class Cat(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
        
    def make_sound(self):
        print("Meow!")

    def eat_food(self, available):
        if available <= 0:
            self.make_sound()
            self.make_sound()
            self.make_sound()
            self.make_sound()
            return 0
        elif available < 10:
            self.make_sound()
            self.make_sound()
            return 0
        else:
            return available - 10


class Dog(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def make_sound(self):
        print("Woof!")

    def eat_food(self, available, eat_quantity = 5):
        if available < eat_quantity:
            return 0
    
        return available - eat_quantity

class Duck(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Quack! Quack!")

    def eat_food(self, capacity):
        self.make_sound()
        result = capacity - random.randrange(1, 9)

        if result >= 0:
            return result
        return 0

class Horse(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Neeiiigh!")

    def eat_food(self, capacity):
        if capacity > 30:
            result = capacity - 15
        elif capacity > 0:
            result = capacity - 8
        else:
            return 0
        
        return result

c1 = Cat("Whiskers", 5, "fish")
d1 = Dog("Sparky", 7, "meat")
du1 = Duck("Patio", 5, "grain")
h1 = Horse("Mimi", 1, "hay")
du2 = Duck("Svetlio", 2, "grain")
h2 = Horse("Morki", 7, "hay")
c2 = Cat("Momo", 5, "fish")
d2 = Dog("Chari", 9, "meat")
c3 = Cat("Beluga", 1, "fish")
du3 = Duck("Patio", 5, "grain")

animals = [c1, d1, du1, h1, du2, h2, c2, d2, c3, du3]

food_storage = {
    "fish": 72,
    "meat": 65,
    "hay": 83,
    "grain": 69,
    "carrots": 101,
    "chaff": 94
}

for i in range(10):
    print("=======")
    
    for animal in animals:
        available = food_storage[animal.food]
        remaining = animal.eat_food(available)
        eaten_food = available - remaining
        print(f"{animal.name} the {type(animal).__name__} just ate {eaten_food} {animal.food}, there's {remaining} left")
        food_storage[animal.food] = remaining
