from random import randint
#from lab_08_material import Iguana
# circular import

class JungleAnimal:
    pass

class Jaguar(JungleAnimal):
    pass

class Human(JungleAnimal):
    pass

class Lemur(JungleAnimal):
    pass

fruits = 100
animals = []
buildings = []

# from lab_08_material import Iguana

def generate_animals(n):
    for i in range(0, n):
        rtype = randint(0, 9)
        # ...
        if rtype >= 0 and rtype <= 3:
            animals.append(Lemur())
        # elif rtype >= 3 and rtype <= 4:
        #      animals.append(Iguana())
        elif rtype >= 4 and rtype <= 7:
            animals.append(Jaguar())
        elif rtype >= 8 and rtype <= 9:
            animals.append(Human())

    print(f"There are {len(animals)} in the jungle")

print("Module name", __name__)

if __name__ == "__main__":
    generate_animals(10)

    for anim in animals:
        t = type(anim)
        if t == Human:
            print("Hello", end=" ")
        print(t)
