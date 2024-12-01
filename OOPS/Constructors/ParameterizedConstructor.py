class Student:
    name=""
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('Adding new Student in the database')
        print("The student name is "+self.name)
        print("The student age is %d"%self.age)


s1=Student("Divyansh",20)
s2=Student("Shashank Chandra",21)