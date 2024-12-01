class Person:
    def __init__(self, *args):
        if len(args) == 2:  
            self.name=args[0]
            self.age = args[1]
        elif len(args) == 1 and isinstance(args[0], Person):  
            self.name = args[0].name
            self.age = args[0].age
        else:
            raise ValueError("Invalid arguments provided.")

    def display(self):
        print(f"{self.name} {self.age}")


p1 = Person("Divyansh", 20)

p2 = Person(p1)

p2.display()
