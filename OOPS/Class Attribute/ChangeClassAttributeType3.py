class Person:
    name="anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p=Person()
print(p.name)
p.changeName("Divyansh")
print(p.name)
