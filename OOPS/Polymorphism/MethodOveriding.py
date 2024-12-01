class F:
    def printInfo(self):
        print("F")

class C(F):
    def printInfo(self):
        print("C")

c=C()
c.printInfo()