class Animal:
    def __init__(self, name, years, food_type):
        self.name = name
        self.years = years
        self.food_type = food_type
    def make_sound(self):
        pass
    def eat_food(self, quantity):
        pass
    
class Cat(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)
    def make_sound(self):
        print("Meow!")
    def eat_food(self, quantity):
        if quantity == 0:
            for a in range(4):
                self.make_sound()
            return 0
        elif quantity < 10:
            for a in range(2):
                self.make_sound()
            return 0
        return quantity - 10
        
class Dog(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)
    def make_sound(self):
        print("Bau, Bau!")
    def eat_food(self, quantity, eat_quantity = 5):
        if quantity > eat_quantity:
            return quantity - eat_quantity
        return 0
        
class Duck(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)
    def make_sound(self):
        print("Wakk, Wakk!")
    def eat_food(self, quantity):
        import random
        random_number = random.randint(1, 9)
        if random_number > quantity:
            return 0
        return quantity - random_number
        
class Horse(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)
    def make_sound(self):
        print("Ihuhu!")
    def eat_food(self, quantity):
        if quantity == 0:
            for a in range(4):
                self.make_sound()
            return 0
        if quantity < 30 and quantity > 8:
            return quantity - 8
        if quantity < 8:
            return 0
        return quantity - 15

list_animals = [Cat("Matsa", 2, "cat_food"), Dog("Sara", 4, "meat"), Horse("Vihur", 6, "grass"),Cat("Matsuna", 2, "meat"), Duck("Anaconda", 3, "meat"), Horse("Jenata", 17, "grass"), Duck("Melisa", 3, "duck_food"), Horse("Mufasa", 10, "grass"), Horse("Magare", 5, "grass"), Dog("Diego", 6, "meat")
                ]
food_dictionary = {'grass':300, 'meat':145, 'duck_food':75, 'cat_food':125}

for a in list_animals:
    print("=======")
    for x in range(5):
        current_quantity = food_dictionary[a.food_type]
        food_dictionary[a.food_type] = a.eat_food(current_quantity)
        print(f"{a.name} the {type(a).__name__} just ate {current_quantity - food_dictionary[a.food_type]} {a.food_type}, there's {food_dictionary[a.food_type]} left.")
        