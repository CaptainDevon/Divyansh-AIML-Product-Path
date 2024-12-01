class Herbivore:
    def printFeatureH(self):
        print("it eats grass")

class Carnivore:
    def printFeatureC(self):
        print("it eats meat")


class Omnivore(Herbivore,Carnivore):
    ...


o=Omnivore()
o.printFeatureH()
o.printFeatureC()
