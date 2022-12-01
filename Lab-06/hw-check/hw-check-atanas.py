import random


class Animal:
    def __init__(self, name, age, food_type):
        self.name = name
        self.age = age
        self.food_type = food_type

    def make_sound(self):
        pass

    def eat_food(self, amount):
        pass


class Cat(Animal):
    def __init__(self, name, age, food_type):
        super().__init__(name, age, food_type)

    def make_sound(self):
        print("Meow!")

    def eat_food(self, amount):
        if amount < 10:
            print(self.make_sound())
            print(self.make_sound())
            return 0
        elif amount == 0:
            print(self.make_sound())
            print(self.make_sound())
            print(self.make_sound())
            print(self.make_sound())
        else:
            return amount - 10


class Dog(Animal):
    def __init__(self, name, age, food_type):
        super().__init__(name, age, food_type)

    def make_sound(self):
        print("Jaf!")

    def eat_food(self, amount, eat_quantity=5):
        if amount >= eat_quantity:
            return amount - eat_quantity
        else:
            return 0


class Duck(Animal):
    def __init__(self, name, age, food_type):
        super().__init__(name, age, food_type)

    def make_sound(self):
        print("Kwak!")

    def eat_food(self, amount, eat_quantity=random.randint(1, 9)):
        if amount >= eat_quantity:
            print(self.make_sound())
            return amount - eat_quantity
        else:
            return 0


class Horse(Animal):
    def __init__(self, name, age, food_type):
        super().__init__(name, age, food_type)

    def make_sound(self):
        print("Neigh!")

    def eat_food(self, amount):
        if 8 < amount < 2 * 15:
            return amount - 8
        elif amount <= 8:
            return 0
        else:
            return amount - 15


animals_1 = [Cat("Maca", 1, "milk"), Cat("Kati", 2, "milk"), Cat("Neli", 3, "milk"), Dog("Sharo", 4, "bones"),
             Dog("Bobi", 5, "bones"), Dog("Roni", 6, "bones"), Duck("Dafi", 1, "seeds"), Duck("Donald", 2, "seeds"),
             Horse("Kokos", 10, "chaff"), Horse("Putin", 15, "chaff")]

animal_food = {"milk": 278, "bones": 150, "seeds": 150, "chaff": 250}

for i in range(10):
    print("=======")
    for j in animals_1:
        amount_1 = animal_food[j.food_type]
        animal_food[j.food_type] = j.eat_food(amount_1)
        print(f"{j.name} the {type(j).__name__} just ate {amount_1 - animal_food[j.food_type]} {j.food_type},"
              f" there's {animal_food[j.food_type]} left")