import random

class InvalidParameterError(Exception):
    def __init__(self, invalid_param):
        message = f"Invalid class parameter: {invalid_param}"
        super().__init__(message)

class InvalidAgeError(InvalidParameterError):
    def __init__(self):
        super().__init__("age")

class InvalidSoundError(InvalidParameterError):
    def __init__(self):
        super().__init__("sound")


class JungleAnimal:
    def __init__(self, name, age, sound):
        if type(name) != str:
            raise InvalidParameterError("name")
        elif type(age) != int:
            raise InvalidAgeError()
        elif type(sound) != str:
            raise InvalidSoundError()

        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def print(self):
        pass

    def daily_task(self):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 15:
            raise InvalidAgeError()
        elif sound.count("r") < 2:
            raise InvalidSoundError()
        
        super().__init__(name, age, sound)

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals):
        for i in range(len(animals)):
            anim_type = type(animals[i])
            if anim_type == Lemur or anim_type == Human:
                print(f"{self.name} the Jaguar hunted down {animals[i].name} the {anim_type.__name__}")
                del animals[i]
                return
        
        print(f"{self.name} the Jaguar couldn't find anything to eat")
        self.make_sound()

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 10:
            raise InvalidAgeError()
        elif "e" not in sound:
            raise InvalidSoundError()
        
        super().__init__(name, age, sound)

    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def daily_task(self, fruits):
        if fruits >= 10:
            fruits -= 10
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return fruits
        elif fruits > 0:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0
        else:
            print(f"{self.name} the Lemur couldn't find anything to eat")
            self.make_sound()
            self.make_sound()
            return 0

class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 60:
            raise InvalidAgeError()
        elif "a" not in sound:
            raise InvalidSoundError()
        
        super().__init__(name, age, sound)

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals, buildings):
        index = animals.index(self)
        
        if index == 0 and type(animals[index + 1]) == Human:
            buildings.append(Building("Fence"))
            print(f"{self.name} the Human built a Fence")
        elif index == len(animals) - 1 and type(animals[index - 1]) == Human:
            buildings.append(Building("Fence"))
            print(f"{self.name} the Human built a Fence")
        elif type(animals[index + 1]) == Human and type(animals[index - 1]) == Human:
            buildings.append(Building("Hut"))
            print(f"{self.name} the Human built a Hut")
        else:
            print(f"{self.name} the Human roamed around in search for other humans")
            

class Building:
    def __init__(self, type):
        self.type = type


fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steven",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Arnold",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle",
    "Ramona"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
    rand_num = random.randint(0, 9)
    rand_name = names[random.randint(0, len(names)-1)]
    rand_age = random.randint(7, 20)
    rand_sound = sounds[random.randint(0, len(sounds)-1)]

    try:
        if rand_num >= 0 and rand_num <= 3:
            animals.append(Lemur(rand_name, rand_age, rand_sound))
        elif rand_num >= 4 and rand_num <= 7:
            animals.append(Jaguar(rand_name, rand_age, rand_sound))
        elif rand_num >= 8 and rand_num <= 9:
            animals.append(Human(rand_name, rand_age, rand_sound))
    except Exception as ex:
        print(rand_num, rand_name, rand_age, rand_sound, str(ex))

print()
print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if type(anim) == Lemur:
        fruits = anim.daily_task(fruits)
    elif type(anim) == Jaguar:
        anim.daily_task(animals)
    elif type(anim) == Human:
        anim.daily_task(animals, buildings)

print()
print(f"The jungle now has {len(animals)} animals, {fruits} fruits and {len(buildings)} buildings")
print(animals)
print(buildings)

