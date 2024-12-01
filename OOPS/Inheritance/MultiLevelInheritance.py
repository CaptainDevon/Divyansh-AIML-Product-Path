class GrandFather:
    def printGF(self):
        print("GrandFather")

class Father(GrandFather):
    def printF(self):
        print("Father")

class Child(Father):
    def printC(self):
        print("Child")


c=Child()
c.printGF()
c.printF()
c.printC()