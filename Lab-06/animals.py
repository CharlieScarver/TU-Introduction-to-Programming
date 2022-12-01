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
            return 0
        elif available < 10:
            self.make_sound()
            self.make_sound()
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


c = Cat("Whiskers", 5, "fish")
d = Dog("Sparky", 7, "dog_food")

fish = 70
dog_food = 50

for i in range(10):
    print("=======")
    
    food_left = c.eat_food(fish)
    eaten_food = fish - food_left
    fish = food_left
    print(f"{c.name} the {type(c).__name__} just ate {eaten_food} {c.food}, there's {food_left} left")

    food_left = d.eat_food(dog_food)
    eaten_food = dog_food - food_left
    dog_food = food_left
    print(f"{d.name} the {type(d).__name__} just ate {eaten_food} {d.food}, there's {food_left} left")


