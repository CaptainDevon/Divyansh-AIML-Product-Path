class Animal:
    def printAnimal(self):
        print("This is an animal")

class Herbivore(Animal):
    def printFeature(self):
        print("it eats grass")

h1=Herbivore()
h1.printAnimal()
h1.printFeature()