class Person:
    name="anonymous"

    def changeName(self,name):
        self.__class__.name=name

p1=Person()
print(p1.name)
p1.changeName("Arthur")
print(p1.name)