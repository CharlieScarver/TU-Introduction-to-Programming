class Component:
    def __init__(self, model, price, generation):
        self.model = model
        self.price = price
        self.generation = generation

    def print(self):
        print("Component")


# str model
# float price (in USD)
# int generation
# float frequency (in GHz)
class Processor(Component):
    def __init__(self, model, price, generation, frequency):
        super().__init__(model, price, generation)
        
        self.frequency = frequency

    def print(self):
        print(f"Processor(\"{self.model}\", {self.price}, {self.generation}, {self.frequency})")

# str model
# float price (in USD)
# int generation
# int vram (in GB)
class VideoCard(Component):
    def __init__(self, model, price, generation, vram):
        super().__init__(model, price, generation)
        
        self.vram = vram

    def print(self):
        print(f"VideoCard(\"{self.model}\", {self.price}, {self.generation}, {self.vram})")


cpu = Processor("Intel Core i7 100400K", 450.0, 7, 3.8)
vc = VideoCard("Nvidia GeForce RTX 2060", 750.0, 6, 2)

cpu.print()
vc.print()

l = [cpu, vc]
