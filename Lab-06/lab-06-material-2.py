#
### Computer components
print("\n\n### Computer components\n")

# str username
# str email
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(\'{self.username}\', \'{self.email}\')"

user = User('Alex673', 'alex673@gmail.com')
print(user)

# str model
# float price
# int generation (0 < x < 10)
class Component:
    def __init__(self, model, price, generation):
        if type(generation) != int or generation <= 0 or generation > 9:
            raise Exception("Invalid parameter: generation")
        
        self.model = model
        self.price = price
        self.generation = generation

    def print(self):
        print(f"Component: {{\n\tmodel = {self.model}, \n\tprice = ${self.price}, \n\tgeneration = {self.generation}\n}}")

# int ram (0 < x < 32) (in GB)
class VideoCard(Component):
    def __init__(self, model, price, generation, ram):
        super().__init__(model, price, generation)

        if type(ram) != int or ram <= 0 or ram > 32:
            raise Exception("Invalid parameter: ram")
        
        self.ram = ram

    def print(self):
        print(f"VideoCard: {{\n\tmodel = {self.model}, \n\tprice = ${self.price}, \n\tgeneration = {self.generation}, \n\tram = {self.ram} GB\n}}")

    def render(self, text):
        print(f"Rendered {text}")

# float frequency (in GHz)
class Processor(Component):
    def __init__(self, model, price, generation, frequency):
        super().__init__(model, price, generation)
    
        self.frequency = frequency

    def __repr__(self):
        return f"Processor(\'{self.model}\', {self.price}, {self.generation}, {self.frequency})"

    def print(self):
        super().print()
        print(f"++ Processor {self.frequency} GHz")

    def calculate(self, a, b):
        print(f"Calculated a + b = {a + b}")


# ram = Component('KINGSTON DDR4 RAM', 120.0, 10)
# Invalid argument: generation

ram = Component('KINGSTON DDR4 RAM', 120.0, 4)
ram.print()
        
print(ram)
print()

cpu = Processor('Intel Core i7 10700K', 450.0, 7, 3.80)
cpu.print()
cpu.calculate(2, 5)

print()

vc = VideoCard('Nvidia GeForce RTX 2060', 750.0, 6, 2)
vc.print()
vc.render("Hello")

print("=====")
print()

cmps = [ram, cpu, vc]
for c in cmps:
    c.print()

print(cpu)
print()

class Computer:
    def __init__(self, owner, components):
        if type(owner) != User:
            raise Exception("Invalid argument: owner")
        
        if type(components) != list:
            raise Exception("Invalid argument: components")
        
        self.owner = owner
        self.components = components

    def __repr__(self):
        return f"Computer({self.owner}, {self.components})"


computer = Computer(user, [cpu, vc, ram])

print(computer)

        
