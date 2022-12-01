class Animal:
    def __init__(self, name, age, type_food):
        self.name = name
        self.age = age
        self.type_food = type_food

    def make_sound(self):
        pass

    def eat_food(self, quantity):
        pass

class Cat(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Meow!")

    def eat_food(self, quantity):
        if quantity == 0:
            for x in range(4):
                self.make_sound()
            return 0
        elif quantity < 10:
            for x in range(2):
                self.make_sound()
            return 0
        return quantity - 10


class Dog(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Woof-Woof!")

    def eat_food(self, quantity, eat_quantity=5):
        result = quantity - eat_quantity
        if result >= 0:
            return result
        return 0


class Duck(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Quack-Quack!")

    def eat_food(self, quantity):
        self.make_sound()
        import random
        random_number = random.randint(1, 9)
        if random_number > quantity:
            return 0
        return quantity - random_number


class Horse(Animal):
    def __init__(self, name, age, type_food):
        super().__init__(name, age, type_food)

    def make_sound(self):
        print("Hiiiiihhh!")

    def eat_food(self, quantity):
        if quantity > 30:
            result = quantity - 15
        else:
            result = quantity - 8
        if result < 0:
            return 0
        return result



dic_food = {"meat":120, "fish":158, "grass": 70, "apples": 252}

animal_1 = Cat("Garfield", 6, "fish")
animal_2 = Dog("Yasuo", 4, "meat")
animal_3 = Duck("Alexa", 2, "grass")
animal_4 = Horse("Apoloniq", 8, "apples")
animal_5 = Duck("Azis", 1, "grass")
animal_6 = Horse("Veigar", 10, "apples")
animal_7 = Cat("Alf", 9, "fish")
animal_8 = Dog("Rexy", 3, "meat")

list_animals = [animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8]


for x in list_animals:
    print("========================")
    for y in range(10):

        class_name = list_animals[y].__class__.__name__
        name_animal = list_animals[y].name
        food = list_animals[y].type_food
        left_food = list_animals[y].eat_food(dic_food[food])
        print(f"{name_animal} the {class_name} just ate {dic_food[food]-left_food} {food}, "
              f"there's {left_food} left")
        dic_food[food] = left_food
