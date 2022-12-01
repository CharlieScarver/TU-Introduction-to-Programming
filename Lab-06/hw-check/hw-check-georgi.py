class Vehicle:
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers):
        self.brand = brand
        self.model = model
        self.engine_vol = engine_vol
        self.max_speed = max_speed
        self.total_km = total_km
        self.max_passengers = max_passengers
        self.class_name = __class__.__name__

    def print_info(self):
        print(f"{self.class_name}({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}, "
              f"{self.max_passengers})")


class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, price, motor_bin):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers=2)
        self.price = price
        self.motor_bin = motor_bin
        self.class_name = __class__.__name__

class InvalidParameterError(Exception):
    def __init__(self, message="Invalid parameter value", *args):
        super().__init__(message, *args)
        print(message, args)


i = InvalidParameterError()
i = InvalidParameterError("asdasdas")
i = InvalidParameterError("asdasd", 1, 2, 3, 4, "asdasd")


class Car(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, category, type_fuel):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers)

        if type(category) != str:
            raise InvalidParameterError()
            raise ValueError()
            raise NameError()
            print('Invalid category')
            return
        
        self.category = category
        self.type_fuel = type_fuel
        self.class_name = __class__.__name__


class Bus(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, company, year):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers)
        self.company = company
        self.year = year
        self.class_name = __class__.__name__


vehicle1 = Vehicle("Mercedes", "Vito", 3.2, 187.6, 1231223.6, 9)
motorbike1 = Motorbike("Honda", "CBR", 0.6, 280.0, 1232.1, 1232.34, False)
car1 = Car("Mazda", "3", 1.6, 195.1, 110232.1, 4, "B", "Petrol")
bus1 = Bus("Iveco", "Magelys", 4.8, 104.3, 1130322.1, 52, "Dicordia", 2004)

print(motorbike1.max_passengers)
vehicle1.print_info()
motorbike1.print_info()
car1.print_info()
bus1.print_info()

print(motorbike1.engine_vol)
Vehicle.print_info(motorbike1)

