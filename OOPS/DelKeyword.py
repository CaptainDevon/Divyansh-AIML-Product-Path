class Student:
    def __init__(self,name):
        self.name=name

    def printint(self):
        print(self.name)


s1=Student("Divyansh")
print(s1)
del(s1)
print(s1)