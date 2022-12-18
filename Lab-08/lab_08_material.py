from jungle_animal import JungleAnimal, animals, generate_animals

# class Iguana(JungleAnimal):
#      pass

print(animals)
generate_animals(10)
print(len(animals))

# animals.insert(3, Iguana())
# animals.insert(7, Iguana())

# for anim in animals:
#     t = type(anim)
#     if t == Human:
#         print("Hello, ", end=" ")
#     print(t)

print("Module name", __name__)
