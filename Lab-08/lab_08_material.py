from jungle_animal import JungleAnimal, Human, generate_animals, animals

class Iguana(JungleAnimal):
    pass

generate_animals(10)
animals.insert(3, Iguana())
animals.insert(7, Iguana())

for anim in animals:
    t = type(anim)
    if t == Human:
        print("Hello, ", end=" ")
    print(t)
