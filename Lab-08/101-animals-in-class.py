from random import randint

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
    def __init__(self, name, age, sound) -> None:
        if type(name) != str:
            raise InvalidParameterError("name")
        if type(age) != int:
            raise InvalidAgeError()
        if type(sound) != str:
            raise InvalidSoundError()
        
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def print(self):
        pass

    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound) -> None:
        super().__init__(name, age, sound)

        if age > 15:
            raise InvalidAgeError()
        if sound.count("r") < 2:
            raise InvalidSoundError()

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals):
        for i in range(len(animals)):
            if type(animals[i]) == Lemur or type(animals[i]) == Human:
                print(f"{self.name} the Jaguar hunted down {animals[i].name} the {type(animals[i]).__name__}")
                del animals[i]
                return
        print(f"{self.name} the Jaguar was left hungry")
        self.make_sound()

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound) -> None:
        super().__init__(name, age, sound)

        if age > 10:
            raise InvalidAgeError()
        if "e" not in sound:
            raise InvalidSoundError()
            

    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def make_sound(self):
        super().make_sound()

        print("hey")

    def daily_task(self, fruits):
        if fruits >= 10:
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return fruits - 10
        elif fruits > 0:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0
        else:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0

class Human(JungleAnimal):
    def __init__(self, name, age, sound) -> None:
        super().__init__(name, age, sound)

        if age > 60:
            raise InvalidAgeError()
        if "a" in sound:
            raise InvalidSoundError()

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals, buildings):
        index = animals.index(self)

        if index == 0 and type(animals[index + 1]) == Human:
            print(f"{self.name} the Human built a Fence")
            buildings.append(Building("Fence"))
            return
        elif index == len(animals) - 1 and type(animals[index - 1]) == Human:
            print(f"{self.name} the Human built a Fence with {animals[index - 1].name}")
            buildings.append(Building("Fence"))
            return
        elif type(animals[index - 1]) == Human and type(animals[index + 1]) == Human:
            print(f"{self.name} the Human built a Hut with {animals[index - 1].name}")
            buildings.append(Building("Hut"))
            return

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
	# fill list with random animals
    ranim = randint(0, 9)
    rname = randint(0, len(names) - 1)
    rage = randint(7, 20)
    rsound = randint(0, len(sounds) - 1)

    try:
        if ranim >= 0 and ranim <= 3:
            anim = Lemur(names[rname], rage, sounds[rsound])
        elif ranim >= 4 and ranim <= 7:
            anim = Jaguar(names[rname], rage, sounds[rsound])
        else:
            anim = Human(names[rname], rage, sounds[rsound])
    except (InvalidParameterError, InvalidAgeError, InvalidSoundError) as ex:
        print(ranim, names[rname], rage, sounds[rsound], str(ex))
    else:
        animals.append(anim)

 
print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    # call daily_task() for each animal
    if type(anim) == Lemur:
        fruits = anim.daily_task(fruits)
    elif type(anim) == Jaguar:
        anim.daily_task(animals)
    elif type(anim) == Human:
        anim.daily_task(animals, buildings)

print(f"The jungle now has {len(animals)} animals, {fruits} fruits and {len(buildings)} buildings")
print(animals)
print(buildings)
