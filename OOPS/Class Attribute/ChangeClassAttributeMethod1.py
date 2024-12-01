class Person:
    name="anonymous"

    def changeName(self,name):
        Person.name=name

p1=Person()
print(p1.name)
p1.changeName("Arthur")
print(p1.name)