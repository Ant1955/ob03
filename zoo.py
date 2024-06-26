import pickle
import os


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} кушает.")


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} поет.")


class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} храпит.")


class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит.")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, person):
        self.staff.append(person)


class ZooKeeper:

    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Сохранение состояния зоопарка в файл


def save_zoo(zoo_name, filename):
    with open(filename, 'wb') as file:
        pickle.dump(zoo_name, file)


# Загрузка состояния зоопарка из файла
def load_zoo(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


zoo = Zoo()
zoo.add_animal(Bird("Соловей", 5))
zoo.add_animal(Mammal("Лошадь", 3))
zoo.add_animal(Reptile("Змея", 2))

zoo.add_staff(ZooKeeper("Михаил"))
zoo.add_staff(Veterinarian("Светлана"))


if os.path.exists("zoo.txt") & (input("Загрузить состояние зоопарка? (y/n): ") == "y"):
    zoo = load_zoo("zoo.txt")
else:  # if not os.path.exists("zoo.txt"):
    save_zoo(zoo, "zoo.txt")

animal_sound(zoo.animals)

for person in zoo.staff:
    if isinstance(person, ZooKeeper):
        person.feed_animal(zoo.animals[0])
    else:
        person.heal_animal(zoo.animals[1])
