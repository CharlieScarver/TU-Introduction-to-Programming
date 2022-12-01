import random


class Animal:
    def __init__(self, name, years, food_type):
        self.name = name
        self.years = years
        self.food_type = food_type

        def make_sound():
            return

        def eat_food():
            return


class Cat(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)

    def make_sound(self):
        print("Meow!")

    def eat_food(self, food_count):
        if food_count >= 10:
            food_count -= 10
            return food_count
        elif food_count <= 0:
            self.make_sound()
            self.make_sound()
            return 0


class Dog(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)

    def make_sound(self):
        print("Bark!")

    def eat_food(self, food_count, eat_quantity=5):
        if food_count <= 0:
            food_count = 0
            return food_count
        else:
            food_count -= eat_quantity
            return food_count


class Duck(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)

    def make_sound(self):
        print("Quack!")

    def eat_food(self, food_count, random_food):
        if food_count <= 0:
            food_count = 0
            return food_count
        else:
            self.make_sound()
            food_count -= random_food
            return food_count


class Horse(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)

    def make_sound(self):
        print("Snort!")

    def eat_food(self, food_count):
        if food_count >= 15:
            food_count -= 15
            return food_count
        elif 15 >= food_count > 0:
            food_count -= 8
            return food_count
        else:
            food_count = 0
            return food_count


animals_list = []
food = {"fish":90, "dog_food":55, "fish_food":50, "horse_food":40}

cat1 = Cat("Elizabeth", 2, "fish")
cat2 = Cat("Ivan", 5, "fish")
cat3 = Cat("Gosho", 4, "fish")
dog1 = Dog("Tita", 5, "dog_food")
dog2 = Dog("Petko", 8, "dog_food")
duck1 = Duck("Dani", 2, "fish_food")
duck2 = Duck("Luyben", 1, "fish_food")
duck3 = Duck("Petur", 2, "fish_food")
horse1 = Horse("Veni", 7, "horse_food")
horse2 = Horse("Evtimii", 5, "horse_food")

animals_list.append(cat1)
animals_list.append(cat2)
animals_list.append(cat3)
animals_list.append(dog1)
animals_list.append(dog2)
animals_list.append(duck1)
animals_list.append(duck2)
animals_list.append(duck3)
animals_list.append(horse1)
animals_list.append(horse2)

for i in range(0, 10):
    print("=======")
    for n in animals_list:

        if isinstance(n, Cat):
            fish_count = 10
            if fish_count >= food["fish"]:
                fish_count = 0
            food["fish"] = n.eat_food(food["fish"])
            print(f"{n.name} the {n.__class__.__name__} just ate {fish_count} {n.food_type}, there's {food['fish']} left")
            
        elif isinstance(n, Dog):
            quantity = 5
            if quantity > food["dog_food"]:
                quantity = 0
            food["dog_food"] = n.eat_food(food["dog_food"], quantity)
            print(f"{n.name} the {n.__class__.__name__} just ate {quantity} {n.food_type}, there's {food['dog_food']} left")
            
        elif isinstance(n, Duck):
            random_food = random.randint(1, 9)
            if random_food >= food["fish_food"]:
                food["fish_food"] = 0
                random_food = 0

            food["fish_food"] = n.eat_food(food["fish_food"], random_food)
            print(f"{n.name} the {n.__class__.__name__} just ate {random_food} {n.food_type}, there's {food['fish_food']} left")
            
        elif isinstance(n, Horse):
            horse_food = 16
            if horse_food > food["horse_food"]:
                horse_food = 8
            if horse_food > food["horse_food"]:
                horse_food = 0
                food["horse_food"] = 0
            food["horse_food"] = n.eat_food(food["horse_food"])
            print(f"{n.name} the {n.__class__.__name__} just ate {horse_food} {n.food_type}, there's {food['horse_food']} left")