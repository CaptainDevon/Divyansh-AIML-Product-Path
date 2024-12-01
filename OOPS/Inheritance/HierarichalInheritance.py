class Animal:
    def printAnimal(self):
        print("This is an animal")

class Herbivore(Animal):
    def printFeature(self):
        print("it eats grass")

class Carnivore(Animal):
    def printFeature(self):
        print("it eats meat")

h=Herbivore()
c=Carnivore()
h.printAnimal()
h.printFeature()

c.printAnimal()
c.printFeature()