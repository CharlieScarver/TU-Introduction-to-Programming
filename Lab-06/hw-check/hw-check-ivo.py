#Exercise 1
#brand, model -> str
#engine_volume, max_speed, total_km -> float
#max_passengers -> int
class Vehicle:
    def __init__(self, brand, model, engine_volume, maximum_speed, total_km, max_passengers):
        self.brand = brand
        self.model = model
        self.engine_volume = engine_volume
        self.maximum_speed = maximum_speed
        self.total_km = total_km
        self.max_passengers = max_passengers

    def print_info(self):
        print(f"Vehicle: {self.brand}, {self.model}, {self.engine_volume}, {self.maximum_speed}, {self.total_km}, {self.max_passengers}")

#price -> float
#has_basket -> boolean
class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_volume, maximum_speed, total_km, price, has_basket):
        super().__init__(brand, model, engine_volume, maximum_speed, total_km, 2)
        self.price = price
        self.has_basket = has_basket
    def print_info(self):
        print(f"Motorbike: {self.brand}, {self.model}, {self.engine_volume}, {self.maximum_speed}, {self.max_passengers}, {self.total_km}, {self.price}, {self.has_basket}")

#category, fuel_type -> str
class Car(Vehicle):
    def __init__(self, brand, model, engine_volume, maximum_speed, total_km, category, fuel_type):
        super().__init__(brand, model, engine_volume, maximum_speed, total_km, 4)
        self.category = category
        self.fuel_type = fuel_type

    def print_info(self):
        print(f"Car: {self.brand}, {self.model}, {self.engine_volume}, {self.maximum_speed}, {self.total_km}, {self.max_passengers}, {self.category}, {self.fuel_type}")

#firm -> str
#year_production -> int
class Bus(Vehicle):
    def __init__(self, brand, model, engine_volume, maximum_speed, total_km, max_passengers, firm, year_production):
        super().__init__(brand, model, engine_volume, maximum_speed, total_km, max_passengers)
        self.firm = firm
        self.year_production = year_production

    def print_info(self):
        print(f"Bus: {self.brand}, {self.model}, {self.engine_volume}, {self.maximum_speed}, {self.total_km}, {self.max_passengers}, {self.firm}, {self.year_production}")


#modelX = Vehicle("Volvo", "S30", 140.0, 240.0, 145.123, 5)
#modelY = Motorbike("Suzuki", "v3", 500.0, 300.0, 123.321, 3000.0, True)
#modelZ = Car("Audi", "A6", 400.0, 320.0, 100.000, "A", "Diesel")
#modelD = Bus("Ford", "Sprinter", 120.0, 160.0, 140.000, 7, "PetrovAuto", 2020)
#modelX.print_info()
#modelY.print_info()
#modelZ.print_info()
#modelD.print_info()

#Exercise 2
#name, food_type -> str
#years -> int
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
            for x in range(4):
                self.make_sound()
            return 0
        elif quantity < 10:
            for x in range(2):
                self.make_sound()
            return 0
        return quantity - 10
class Dog(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)

    def make_sound(self,):
        print("Baf!")

    def eat_food(self, quantity, eat_quantity = 5):
        if quantity > eat_quantity:
            return quantity - eat_quantity
        return 0
class Duck(Animal):
    def __init__(self, name, years, food_type):
        super().__init__(name, years, food_type)

    def make_sound(self):
        print("Kvak!")

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
        print("III!")

    def eat_food(self, quantity):
        if quantity < 30 and quantity > 8:
            return quantity - 8
        if quantity < 8:
            return 0
        return quantity - 15


list_animals = [Cat("Rosen", 4, "meat"), Dog("Spartak", 7, "dog_food"), Horse("Joro", 11, "grass"),Cat("Sharly", 2, "meat"),
                Dog("Mitko", 3, "dog_food"), Horse("Joro2", 8, "grass"), Duck("Ceca", 5, "duck_food"), Dog("Spartak2", 5, "dog_food"),
                Duck("Pesho", 1, "duck_food"), Cat("Sparky", 3, "meat")]
food_dict = {'grass':60, 'meat':70, 'duck_food':80, 'dog_food':90}

for x in list_animals:
    print("=======")
    for y in range(10):
        current_quantity = food_dict[x.food_type]
        food_dict[x.food_type] = x.eat_food(current_quantity)
        print(f"{x.name} the {type(x).__name__} just ate {current_quantity - food_dict[x.food_type]} {x.food_type}, there's {food_dict[x.food_type]} left")